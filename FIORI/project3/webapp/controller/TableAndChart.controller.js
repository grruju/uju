sap.ui.define([
	"../lib/BaseController",
	"sap/ui/model/json/JSONModel"
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (Controller, JSONModel) {
        "use strict";

        return Controller.extend("sap.btp.usetemplate.controller.TableAndChart", {
            onInit: function () {
                const oComponent = this.getOwnerComponent(),
                      oRouter = oComponent.getRouter();

                this._setInitModel();
                oRouter.getRoute("TableAndChart")
                       .attachPatternMatched(this._onPatternMatched,this);
            },

            /**
             * Table And Chart View Init Model Setting
             */
            _setInitModel: function() {
                this.getView()
                    .setModel(
                        new JSONModel({
                            chart: []
                        }),
                        'tableAndChart'
                    )
            },

            /**
             * 해당 url 접근시 실행할 함수
             */
            _onPatternMatched: function() {
                const oView = this.getView(),
                      oModel = oView.getModel(),
                      oChart = this.byId('TAC_Chart');

                /**
                 * ../lib/BaseController -> _convertODataToJSON
                 */
                this._convertODataToJSON({
                    model: oModel,
                    path: '/Products',
                    filter: [],
                    jsonModel: oView.getModel('tableAndChart'),
                    busyControl: oChart,
                    callback: function(vResult, oJSONModel) {
                        let aChangedField = this._getChangeFieldList(["ProductName", "UnitPrice"]),
                            aChangedData = this._convertField(vResult, aChangedField);
                            
                        oJSONModel.setProperty('/chart', aChangedData);
                    }.bind(this)
                });
            },

            /**
             * 
             * @returns {array}
             */
            _getChangeFieldList: function(aParam) {
                return [{
                    field: aParam[0],
                    changeField: 'field1',
                },{
                    field: aParam[1],
                    changeField: 'field2'
                }];
            },

            _convertField: function(aData, aChangedData) {
                return aData.map((item) => {
                    let changedObject = {};

                    aChangedData.forEach((info) => { 
                        changedObject[info.changeField] = item[info.field]; 
                    });
                    return changedObject;
                });
            },

            /**
             * row Item 차트 출력
             */
            onTableRowPress: function(oEvent) {
                const bEvent = oEvent.getId() === "press";
                const oControl = oEvent.getSource(),
                      oModel = oControl.getModel(),
                      oContext = bEvent 
                             ? oControl.getBindingContext()
                             : oEvent.getParameter('rowBindingContext');
                
                let oChart = this.byId('TAC_Chart');


                /**
                 * ../lib/BaseController -> _convertODataToJSON
                 */
                this._convertODataToJSON({
                    model: oModel,
                    path: oContext.getPath(),
                    filter: [],
                    urlParameters: {
                        $expand: 'Order_Details'
                    },
                    jsonModel: oChart.getModel('tableAndChart'),
                    busyControl: oChart,
                    callback: function(vResult, oJSONModel) {
                        let aOrderDetails = vResult.Order_Details.results;

                        let aChangedField = this._getChangeFieldList(["OrderID", "UnitPrice"]),
                            aChangedData = this._convertField(aOrderDetails, aChangedField);
                            
                        oJSONModel.setProperty('/chart', aChangedData);
                        this._chartUpdate( oChart, vResult );
                    }.bind(this)
                });
            },

            /**
             * 차트 업데이트
             */
             _chartUpdate: function(chart, vResult) {
                
                var data = chart.getAggregation('dataset')
                var properties = chart.getVizProperties(); 
                var feeds = [
                    new sap.viz.ui5.controls.common.feeds.FeedItem(
                        {
                            'uid' : 'valueAxis',
                            'type' : 'Measure',
                            'values' : ['UnitPrice']
                        }
                    ),
                    new sap.viz.ui5.controls.common.feeds.FeedItem(
                        {
                            'uid' : 'categoryAxis',
                            'type' : 'Dimension',
                            'values' : ['OrderID']
                        }
                    )
                ];

                properties.title.text = vResult.ProductName + " - 오더 하위요소";
                data.getAggregation('measures')[0].setName('UnitPrice');
                data.getAggregation('dimensions')[0].setName('OrderID');
                
                chart.vizUpdate({
                    'data' : data,
                    'properties' : properties,
                    'feeds' : feeds
                });
            },

            /**
             * 버튼 Press 이벤트
             * 사용자가 해당 이벤트를 발생시키면 이전페이지로 갈수 있도록 한다.
             */
            onNavBackPress: function() {
                /**
                 * parameter - string
                 * 해당 페이지의 이전 페이지 routing name을 넣어준다.
                 */
                this.backPage("Main");
            }
        });
    });
