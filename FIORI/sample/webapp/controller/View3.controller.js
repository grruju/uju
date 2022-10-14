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

        return BaseController.extend("sap.sync.sample.controller.View3", {
            bState: true,
            onInit: function () {
                var oModel = {
                    orders: [
                        {
                            orderNum: "001",
                            productNo: "001",
                            product: "f800gt",
                            price: "2000000",
                            warehouse: "A창고"
                        },
                        {
                            orderNum: "021",
                            productNo: "002",
                            product: "r1200gt",
                            price: "300000",
                            warehouse: "C창고"
                        },
                        {
                            orderNum: "015",
                            productNo: "003",
                            product: "s1000rr",
                            price: "250000",
                            warehouse: "A창고"
                        },
                        {
                            orderNum: "007",
                            productNo: "004",
                            product: "r1250gs",
                            price: "1000",
                            warehouse: "B창고"
                        },
                        {
                            orderNum: "066",
                            productNo: "004",
                            product: "cbr600rr",
                            price: "1000",
                            warehouse: "R창고"
                        },
                        {
                            orderNum: "003",
                            productNo: "004",
                            productName: "r1200rs",
                            price: "1000",
                            warehouse: "A창고"
                        }
                    ]
                }
                
                var oModel = new JSONModel(oModel);
                this.getView().setModel(oModel);
                
                var oRouter = this.getRouter();
                oRouter.getRoute("goView3").attachMatched( this._onRouteMatched.bind(this) );
                
            },

            _onRouteMatched: function(oEvent) {
                // 화면을 이동해서 왔을 때 busy를 꺼줌, 전체적인 틀을 다 잡고나서 디테일을 추가할 때
                this.getView().setBusy(false);

            },

            onPressItem:function(oEvnet){
                // 콘솔에서 속성 확인 하기 ************************************************************
                console.log(oEvnet.getSource())
                console.log(oEvnet.getSource().getBindingContextPath())
                console.log(this.getView().getModel().getProperty(oEvnet.getSource().getBindingContextPath()))
                console.log(this.getView().getModel().getProperty(oEvnet.getSource().getBindingContextPath()).orderNum)
                // ***********************************************************************************


                var oModel = this.getView().getModel();

                // 내가 누른 행(인덱스)의 경로 ex) '/orders/0'
                var sPath = oEvnet.getSource().getBindingContextPath();
                var oRowData = oModel.getProperty(sPath);   // 내가 선택한 행의 [전체] 데이터

                var sProduct = oRowData.warehouse;
                var sorderNum = oRowData.orderNum;

                var oParam = {
                    order : sorderNum
                }

                this.getView().setBusy(true);
                // setTimeout(function(){this.getView().setBusy(false);},2000);      // 1초 후에는 setBusy 를 해제해라
                this.getRouter().navTo("objectPage", oParam);
                
                
                // MessageToast로 상품명 띄워주기
                // var msg = sProduct
                // MessageToast.show(msg);

                
            },

            // onViewSetting : function() {
            //     this._openDialog();
            // },

            // handleConfirm: function(oEvent) {
            //     // viewSettingDialog 의 컨펌 이벤트 파라미터로 사용자의 설정값을 받아옴
            //     var sSortPath = oEvent.getParameter("sortItem").getKey();
            //     var bDesc = oEvent.getParameter("sortDescending");
            //     var sGroupPath = oEvent.getParameter("groupItem").getKey();
            //     var bGroupDesc = oEvent.getParameter("groupDescending");
            //     var oTable = this.getView().byId("table");
            //     var oModel = oTable.getBinding("items");

            //     var oSorter = new Sorter(sSortPath, bDesc, function(oContext) {
            //     var name = oContext.getProperty(sGroupPath);
            //             return {
            //                 key: name,
            //                 text: name
            //             };
            //         });
            //     oModel.sort(oSorter);   // 테이블에 반영
                
            // },
            onViewSetting : function() {
                this._openDialog();
            },

            handleConfirm : function(oEvent) {
                // viewSettingDialog 의 컨펌 이벤트 파라미터로 사용자의 설정값을 받아옴
                var sSortPath = oEvent.getParameter("sortItem").getKey();
                var bDesc = oEvent.getParameter("sortDescending");
                var sGroupPath = oEvent.getParameter("groupItem").getKey();
                var bGroupDesc = oEvent.getParameter("groupDescending");
                var oTable = this.getView().byId("table");
                var oModel = oTable.getBinding("items");

                var oSorter = new Sorter(sSortPath, bDesc, function(oContext) {
					var name = oContext.getProperty(sGroupPath);
                    console.log(sGroupPath);
					return {
						key: name,
						text: name
					};
				});
                oModel.sort(oSorter);   // 테이블에 반영
                console.log(oModel);
                
            },

            _openDialog : function (sPage, fInit) {
                var oView = this.getView();
    
                // creates requested dialog if not yet created
                if (!this._mDialogs) {
                    this._mDialogs = Fragment.load({
                        id: oView.getId(),
                        name: "sap.sync.sample.view.Dialog",
                        controller: this
                    }).then(function(oDialog){
                        oView.addDependent(oDialog);
                        if (fInit) {
                            fInit(oDialog);
                        }
                        return oDialog;
                    });
                }
                this._mDialogs.then(function(oDialog){
                    // opens the requested dialog
                    oDialog.open(sPage);
                });
            },


            // _openDialog : function (sPage, fInit) {
            //     var oView = this.getView();

            //     // creates requested dialog if not yet created
            //     if (!this._mDialogs) {
            //         this._mDialogs = Fragment.load({
            //             id: oView.getId(),
            //             name: "sap.sync.sample.view.Dialog",
            //             controller: this
            //         }).then(function(oDialog){
            //             oView.addDependent(oDialog);
            //             if (fInit) {
            //                 fInit(oDialog);
            //             }
            //             return oDialog;
            //         });
            //     }
            //     this._mDialogs.then(function(oDialog){
            //         // opens the requested dialog
            //         oDialog.open(sPage);
            //     });
            // },

            onCheck: function(oEvent) {
                var oButton = oEvent.getSource();   // 버튼
                var oInput1 = this.getView().byId("input1");
                var oInput2 = this.getView().byId("input2");
                var oInput3 = this.getView().byId("input3");
                var sValue1 = oInput1.getValue();
                var sValue2 = oInput2.getValue();
                var sValue3 = oInput3.getValue();

                // 체크대상 인풋창 id 목록
                var aInputIds = ["input1", "input2", "input3"];
                var iLength = aInputIds.length; // 배열의 길이
                // for (var i=0; i<iLength; i++) {
                //     var sId = aInputIds[i]; // 배열에서 id를 하나씩 꺼내옴
                //     var oInput = this.getView().byId(sId);
                //     var sValue = oInput.getValue();
                //     if (this.bState && oInput.getRequired() && sValue === "") {
                //         oInput.setValueState("Error");
                //         oInput.setValueStateText("필수값입니다");
                //     } else {
                //         oInput.setValueState("None");
                //     }
                // }

                // 배열을 뒤지면서 내부 펑션을 배열 요소 개수만큼
                // (index 위치의 element와 index가 바뀌면서) 수행
                var that = this; // 1) that 도 컨트롤러 라는 객체
                // aInputIds.forEach(function(element, index){
                //     // console.log(element, index);
                //     var sId = element; // aInputIds[i]; // 배열에서 id를 하나씩 꺼내옴
                //     var oInput = this.getView().byId(sId);
                //     var sValue = oInput.getValue();
                //     if (that.bState && oInput.getRequired() && sValue === "") {
                //         oInput.setValueState("Error");
                //         oInput.setValueStateText("필수값입니다");
                //     } else {
                //         oInput.setValueState("None");
                //     }
                // }.bind(this)); // 2) .bind(this) this scope를 맞춰줌
                // * forEach 사용시 주의할 점 (순차함수가 아님!!)
                // 사이클을 다 안돌고 아래 코드를 실행시킬 경우가 있음

                var oBox = this.getView().byId("box1");
                oBox.getItems().forEach(function(element){ // 박스 안의 아이템을 하니씩 체크
                    // console.log(element instanceof Input); // 왼쪽이 오른쪽으로부터 만들어진 인스턴스 인지 boolean 값으로 체크 , 친자검증
                    // if (element instanceof Input) {           // Input으로 만든 인스턴스만 필수값 체크 로직을 타도록 걸러주는 역할. 버튼의 속성이 들어오는것을 방지.
                    //     var oInput = element; // this.getView().byId(sId);
                    //     var sValue = oInput.getValue();
                    //     if (that.bState && oInput.getRequired() && sValue === "") {
                    //         oInput.setValueState("Error");
                    //         oInput.setValueStateText("필수값입니다");
                    //     } else {
                    //         oInput.setValueState("None");
                    //     }
                    // }

                    //3번쨰 방법
                    try {
                        var oInput = element; // this.getView().byId(sId);
                        var sValue = oInput.getValue();
                        if (that.bState && oInput.getRequired() && sValue === "") {
                            oInput.setValueState("Error");
                            oInput.setValueStateText("필수값입니다");
                        } else {
                            //에러가 발생하면 실행 - 조건이 에러발생시
                            oInput.setValueState("None");
                        }    
                    } catch(error) {
                        console.log(error);
                    } finally {}
                })

                // // validation check 입력값 검증
                // // if (this.bState && sValue.length < 2){
                // if (this.bState && oInput1.getRequired() && sValue.length === 0) {
                //     oInput1.setValueState("Error");  // UI5 기본 코드 Error 상태로 변경.
                //     oInput1.setValueStateText("필수값입니다!.")
                // } else{
                //     oInput1.setValueState("None");
                // }

                // if (this.bState && oInput2.getRequired() && sValue.length === 0) {
                //     oInput2.setValueState("Error");  // UI5 기본 코드 Error 상태로 변경.
                //     oInput2.setValueStateText("필수값입니다!.")
                // } else{
                //     oInput2.setValueState("None");
                // }

                // if (this.bState && oInput3.getRequired() && sValue.length === 0) {
                //     oInput3.setValueState("Error");  // UI5 기본 코드 Error 상태로 변경.
                //     oInput3.setValueStateText("필수값입니다!.")
                // } else{
                //     oInput3.setValueState("None");
                // }

                if (this.bState) {
                    oButton.setText("초기화")
                } else {
                    oButton.setText("제출")
                }

                this.bState = !this.bState;
            },

            // onSearch: function() {
            //     var oInput = this.getView().byId("searchInput")
            //     var sInput = oInput.getValue();
                
            //     var oTable = this.getView().byId("table");    // table 자체
            //     var oModel = oTable.getBinding("items");       // table 의 바인딩 정보 <-- [필터 적용대상]
            //     console.log("items",oModel)
            //     var aFilter = [];       // 필터를 담을 배열 선언
            //     // debugger;
            //     // ------------------------------------------------------------------------------------ 선언부

            //     var oFilterObject = {
            //         path: "orderNum",
            //         operator: FilterOperator.Contains,
            //         value1: sInput
            //     };
            //     var oSearchFilter = new Filter(oFilterObject);      // 필터생성
            //     console.log(oSearchFilter)
            //     aFilter.push(oSearchFilter);                        // index 0(첫번째 위치) 속성값으로 넣어줌

                
            //     oModel.filter(aFilter)
            onSearch: function() {
                var oInput = this.getView().byId("searchInput"),
                    sValue = oInput.getValue(),
                    oTable = this.getView().byId("table"),
                    oBinding = oTable.getBinding("items"),
                    aFilter = [];

                var oSearchNumFilter = new Filter({
                    path: "orderNum", operator: FilterOperator.Contains, value1: sValue
                });

                var oSearchProductFilter = new Filter({
                    path: "product", operator: FilterOperator.Contains, value1: sValue
                });

                aFilter.push(oSearchNumFilter);
                aFilter.push(oSearchProductFilter);
                var aFilters = new Filter(aFilter); // 필터를 담은 배열을 필터로 전환
                oBinding.filter(aFilters);
            },

            
            
        });
    });
