sap.ui.define([
	"../lib/BaseController",
    "sap/viz/ui5/controls/VizFrame",
	"sap/m/MessageBox"
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (Controller,VizFrame,MessageBox) {
        "use strict";

        return Controller.extend("sap.btp.usetemplate.controller.DynamicCreate", {
            onInit: function () {
                
            },


            /**
             * 버튼 press 이벤트
             * 동적 차트 생성
             */
            onCreateChart: function() {
                let oPanel = this.byId('contentPanel');

                if(oPanel.getContent().length){
                    return MessageBox.error("생성된 차트를 먼저 지우고 생성하세요.")
                }

                oPanel.addContent(
                    new VizFrame(
                        {
                            uiConfig: { applicationSet:'fiori'},
                            vizType: 'bar',
                            dataset: new sap.viz.ui5.data.FlattenedDataset({
                                data: "{/Products}",
                                dimensions: new sap.viz.ui5.data.DimensionDefinition({
                                    name: "ProductName",
                                    value: "{ProductName}"
                                }),
                                measures: new sap.viz.ui5.data.MeasureDefinition({
                                    name: "UnitPrice",
                                    value: "{UnitPrice}"
                                })
                            }),
                            feeds: [
                                new sap.viz.ui5.controls.common.feeds.FeedItem({
                                    uid: "valueAxis",
                                    type: "Measure",
                                    values: ["UnitPrice"]
                                }),
                                new sap.viz.ui5.controls.common.feeds.FeedItem({
                                    uid: "categoryAxis",
                                    type: "Dimension",
                                    values: ["ProductName"]
                                })
                            ]
                        }
                    )
                );
            },

            /**
             * 버튼 press 이벤트
             * fragment를 동적으로 생성한다.
             */
            onAddFragmentChart: function() {
                let oPanel = this.byId('contentPanel');

                if(oPanel.getContent().length){
                    return MessageBox.error("생성된 차트를 먼저 지우고 생성하세요.")
                }
                
                /**
                 * ../lib/BaseController -> _loadFragment
                 */
                this._loadFragment({
                    fragmentName: "chart",
                    handler: function(oFragment) {

                        oPanel.addContent(oFragment);

                    }.bind(this),
                    controller: this
                });
            },

            /**
             * 버튼 press 이벤트
             * 차트 지우기
             */
            onRemoveChart: function() {
                /**
                 * ../lib/BaseController -> getControl
                 */
                let oPopOver = this.getControl({
                    alias: 'DynamicCreate',
                    controlid: 'staticPopover'
                });

                this.byId('contentPanel').removeAllContent();
                
                if(oPopOver){
                    oPopOver.destroy();
                }

                MessageBox.success("차트를 성공적으로 지웠습니다.");
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
            },

            /**
             * @override
             */
            onExit: function() {
                this.byId('contentPanel').removeAllContent();
            }
        });
    });
