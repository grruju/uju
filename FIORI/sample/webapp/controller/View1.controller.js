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
	"sap/ui/core/UIComponent",
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (BaseController, JSONModel, MessageBox,Filter,FilterOperator,daumPost,Fragment,MessageToast,UIComponent) {
        "use strict";

        return BaseController.extend("sap.sync.sample.controller.View1", {
            onInit: function () {
                var oModel = '';
                var mode = '';


                oModel = new sap.ui.model.odata.ODataModel("proxy/https/edu.bgis.co.kr:8443/sap/opu/odata/sap/ZC201_0001_SRV");
                sap.ui.getCore().setModel(oModel);

                var oViewData = {
                    students: [
                        {
                            name: "Lee",
                            score1: "F",
                            score2: "B",
                            result: "",
                            address : ""
                        },
                        {
                            name: "Kim",
                            score1: "B",
                            score2: "B",
                            result: "",
                            address : ""
                        },
                        {
                            name: "Woo",
                            score1: "D",
                            score2: "A",
                            result: "",
                            address : ""
                        },
                        {
                            name: "Kang",
                            score1: "F",
                            score2: "C",
                            result: "",
                            address : ""
                        },
                        {
                            name: "Hwang",
                            score1: "A",
                            score2: "A",
                            result: "",
                            address : ""
                        },
                        {
                            name: "Jo",
                            score1: "C",
                            score2: "B",
                            result: "",
                            address : ""
                        },
                    ],
                    grade: [
                        {
                            key : "A"

                        },
                        {
                            key : "B"
                        },
                        {
                            key : "C"
                        },
                        {
                            key : "D"
                        },
                        {
                            key : "E"
                        },
                        {
                            key : "F"
                        }
                    ],
                    searchValue: "",     // 검색창 프로퍼티
                    addres: ""
                };

                var oViewModel = new JSONModel(oViewData);
                this.getView().setModel(oViewModel);

                // var oTable = this.getView().byId("uiTable");
                // var oTemplate =
                // oTable.setRowActionTemplate(oTemplate);

                
            },
            onSearch: function() {
                var oViewModel = this.getView().getModel();    // JSONModel
                var sSearchText = oViewModel.getProperty("/searchValue");   // 모델에서 프로퍼티 값을 받아옴

                var oTable = this.getView().byId("uiTable");    // ui.table 자체
                var oBinding = oTable.getBinding("rows");       // ui.table 의 바인딩 정보 <-- [필터 적용대상]

                var aFilter = [];       // 필터를 담을 배열 선언
                debugger;
                // ------------------------------------------------------------------------------------ 선언부

                var oFilterObject = {
                    path: 'name',
                    operator: FilterOperator.Contains,
                    value1: sSearchText
                };
                var oSearchFilter = new Filter(oFilterObject);      // 필터생성
                aFilter.push(oSearchFilter);                        // index 0(첫번째 위치) 속성값으로 넣어줌
                console.log(aFilter)

                oBinding.filter(aFilter);
            },
            
            onCheck: function() {
                // 1) 국어가 B 이상일 때만 "합격" / "불합격"
                // 2) 국어와 수학이 모두 B 이상만 "합격" / "불합격"
                var oViewModel = this.getView().getModel();
                var iLength = oViewModel.getProperty("/students").length       // ******************************** 배열하나 속성 ****************************
                // console.log(iLength);

                // students 하위의 배열을 하나씩 체크하면서 result 프로퍼티를 바꿈
                for ( var i=0; i<iLength ; i++) {

                    var sPath1 = "/students/"+ i +"/score1"   // 읽어와서 체크할 대상(국어)
                    var sPath2 = "/students/"+ i +"/score2"   // 읽어와서 체크할 대상(수학)
                    var sPath3 = "/students/"+ i +"/result"   // 변경할 대상

                    var sScore1 = oViewModel.getProperty(sPath1);
                    var sScore2 = oViewModel.getProperty(sPath2);

                    if (( sScore1 === "A" || sScore1 ==="B") && (sScore1 === "A" || sScore1 ==="B" )) {
                        oViewModel.setProperty(sPath3, "합격")
                    } else {
                        oViewModel.setProperty(sPath3, "불합격")
                    }

                }

            },

            onRegist: function() {
                var oInputNmae = this.getView().byId("nameInput");
                var sName = oInputNmae.getValue();

                var oViewModel = this.getView().getModel();
                var sScore1 = oViewModel.getProperty("/score1Input");
                var sScore2 = oViewModel.getProperty("/score2Input");
                var aStudents = oViewModel.getProperty("/students");
                var sAddress = oViewModel.getProperty("/address");      // 모델의 프로퍼티로 읽어옴

                var oPage = this.getView().byId("page");
                debugger;
                // var oAddressInput = oPage.getContent()[0].getItems()[3].getItems()[1];
                // var sAddress = oAddressInput.getValue();             // 객체에서 읽어옴

                // console.log(oPage);
                console.log("onRegistonRegistonRegistonRegistonRegistonRegist")

                var oPerson = {name: sName, score1: sScore1, score2: sScore2, result: "", address: sAddress };
                aStudents.push(oPerson);
                console.log(aStudents);

                oViewModel.setProperty("/students", aStudents)

                //처리결과를 메세지토스트로 사용자에게 알려줌
                var msg = "정상적으로 등록되었습니다."
                MessageToast.show(msg);

                // this.pDialog.setBusy(true);
                
                this.onCloseDialog();

            },

            onDelete: function() {
                var oTable = this.getView().byId("uiTable");
                // var aIndices = oTable.getSelectedIndices();
                // single mode
                var iIndex = oTable.getSelectedIndices()[0]; // array[몇번째 인덱스]
                console.log(iIndex);

                var oViewModel = this.getView().getModel();
                var aStudents = oViewModel.getProperty("/students"); // 테이블 데이터(배열) 가져와서
                
                // ********** 자바 스크립트 삭제 함수 **************************
                // var delStudents = aStudents.shift();   // 배열에 저장된 데이터 중 첫 번째 인덱스에 저장된 데이터를 삭제합니다.(js)
                var delStudents = aStudents.splice(iIndex, 1);   // 배열 객체의 지정 데이터를 삭제하고, 그 구간에 새 데이터를 삽입할 수 있습니다.(js)
                                                                 // splice(start , deleteCount , itemN)
                                                                // (배열의 변경을 시작할 인덱스, 배열에서 제거할 요소의 수, 배열에 추가할 요소.)

                console.log(delStudents);
                oViewModel.setProperty("/students", aStudents)      // 처리(지운) 결과를 모델에 다시 반영
                // ***********************************************************

                

            },

            onPopupAddress: function(oEvent) {
                var oInput = oEvent.getSource();
                new daum.Postcode({
                    oncomplete: function(data) {        // controller - onInit 을 쓰는것과 비슷
                        // 내가 처리하고자 하는 기능을 oncomplete 에 추가
                        // console.log(data);
                        var sAddress = data.address;        // 주소 텍스트
                        oInput.setValue(sAddress);          // 인풋창에 값 반영

                    }
                }).open();
            },

            onRegistPopup: function () {
                if (!this.pDialog){
                    this.pDialog = this.loadFragment({
                        name: "sap.sync.sample.view.Regist"
                    })
                }

                this.pDialog.then(function(oDialog) {
                    oDialog.open(); // 다이얼로그를 켜줌
                    oDialog.setBusy(true)
                    // js 내장 함수 setTimeout([func],지연시간)
                    setTimeout(function(){oDialog.setBusy(false);},2000);      // 1초 후에는 setBusy 를 해제해라

                })
            },

            onCloseDialog: function() {
                var oDialog = this.getView().byId("helloDialog")
                
                oDialog.close();
            },

            // getRouter: function() {
            //     return UIComponent.getRouterFor(this);
            // },

            onNavToView2: function() {
                var oTable = this.getView().byId("uiTable");
                var iIndex = oTable.getSelectedIndices()[0]; // array[몇번째 인덱스]
                var oViewModel = this.getView().getModel();
                var sPath = "/students/" + iIndex + "/name"; //students 의 iIndex 의 name 을 가져옴. /students/?/name
                var sName = oViewModel.getProperty(sPath);

                if (iIndex  === undefined) {      // 테이블에서 아무것도 선택 안했을 때
                    // MessageBox 선택하라고 사용자에게 경고창 팝업
                    this.onWarning2MessageBoxPress();
                } else {
                    this.getRouter().navTo("View2", {name: sName});     //manifest.json route의 'name' 값
                }
                
            },

            onNavToView3: function() {
                    // this.getRouter().navTo("goView3", {}, true);
                    this.getRouter().navTo("goView3");
                
            },

            onWarning2MessageBoxPress: function () {
                var sText = "목록에서 학생 한명을 선택해주세요."
                MessageBox.warning(sText,
                    {
                        actions: [MessageBox.Action.OK, MessageBox.Action.CANCEL],
                        emphasizedAction: MessageBox.Action.OK
                
                    }
                );
            }

            // daumPosstApi: function (_this, postcodeElemId, addressElemID) {

            // },

        });
    });
