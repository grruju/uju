sap.ui.define([
    // "sap/ui/core/mvc/Controller",
    "sap/sync/sample/controller/BaseController",
    "sap/ui/model/json/JSONModel",
	"sap/m/MessageBox",
    "sap/ui/model/Filter",
    "sap/ui/model/FilterOperator",
    "../model/daumPost",
    "sap/ui/core/Fragment",
    "sap/m/MessageToast",
	"sap/ui/core/routing/History",
	"sap/ui/core/UIComponent",
    "sap/ui/model/Sorter",
    "sap/m/Input"
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (BaseController, JSONModel, MessageBox,Filter,FilterOperator,daumPost,Fragment,MessageToast,History,UIComponent,Sorter,Input) {
        "use strict";
        return BaseController.extend("sap.sync.sample.controller.View4", {
            bState: true,
            onInit: function () {
                var oData = {
                    orders: [
                        {
                            orderNum: "001",
                            productNo: "001",
                            product: "f800gt",
                            price: "2000000",
                            warehouse: "A창고",
                            customer: "1성"
                        },
                        {
                            orderNum: "021",
                            productNo: "002",
                            product: "r1200gt",
                            price: "300000",
                            warehouse: "C창고",
                            customer: "2성"
                        },
                        {
                            orderNum: "015",
                            productNo: "003",
                            product: "s1000rr",
                            price: "250000",
                            warehouse: "A창고",
                            customer: "3성"
                        },
                        {
                            orderNum: "007",
                            productNo: "004",
                            product: "r1250gs",
                            price: "1000",
                            warehouse: "B창고",
                            customer: "4성"
                        },
                        {
                            orderNum: "066",
                            productNo: "004",
                            product: "cbr600rr",
                            price: "1000",
                            warehouse: "R창고",
                            customer: "5성"
                        },
                        {
                            orderNum: "003",
                            productNo: "004",
                            productName: "r1200rs",
                            price: "1000",
                            warehouse: "A창고",
                            customer: "6성"
                        }
                    ],
                    customers : [
                        {
                            customerName: "1성", contract: "010-0000-1010", email: "1sung@sangsung.com",
                            address: "서초 1성", post: "00301"
                        },{
                            customerName: "2성", contract: "010-0000-1020", email: "2sung@sangsung.com",
                            address: "서초 2성", post: "00302"
                        },{
                            customerName: "3성", contract: "010-0000-1030", email: "3sung@sangsung.com",
                            address: "서초 3성", post: "00303"
                        },{
                            customerName: "4성", contract: "010-0000-1040", email: "4sung@sangsung.com",
                            address: "서초 4성", post: "00304"
                        },{
                            customerName: "5성", contract: "010-0000-1050", email: "5sung@sangsung.com",
                            address: "서초 5성", post: "00305"
                        },{
                            customerName: "6성", contract: "010-0000-1060", email: "6sung@sangsung.com",
                            address: "서초 6성", post: "00306"
                        }
                    ],
                    customer: {}
                }
                
                var oModel = new JSONModel(oData);
                this.getView().setModel(oModel);

                var oRouter = this.getRouter();
                oRouter.getRoute("objectPage").attachMatched( this._onRouteMatched.bind(this) );
            },

            _onRouteMatched: function(oEvent){
                this.getView().setBusy(false);
                var oArg = oEvent.getParameter("arguments");
                console.log(oArg)
                var sOrderNum = oArg.order;
                console.log(sOrderNum)
                var oModel = this.getView().getModel();
                var aOrderData = oModel.getProperty("/orders");
                var aCustomerData = oModel.getProperty("/customers");
                var sCustomerName = "";

                for (var i=0; i<aOrderData.length; i++){
                    if(aOrderData[i].orderNum === sOrderNum) {
                    // 내가 지금 화면으로 넘어올 때 전달받은 주문번호가 실제 데이터에 있는지 찾고 있는 조건
                        sCustomerName = aOrderData[i].customer; 
                        // 실제 데이터안에서 그 주문건의 고객정보를 읽어오기
                        for (var j=0; j<aCustomerData.length; j++){
                            if(sCustomerName === aCustomerData[j].customerName) {
                                oModel.setProperty("/customer", aCustomerData[j])
                                console.log(oModel)
                                break;
                            }
                        }
                        i = aOrderData.length; // for문 중단시키기, 한번 찾았으면 더 이상 반복할 필요x
                        break; // 실행 중단
                    }
                    if( i === aOrderData.length-1){
                    MessageToast.show("주문정보가 잘못됐습니다.")
                    }
                } 
            },
            
        });
    });
