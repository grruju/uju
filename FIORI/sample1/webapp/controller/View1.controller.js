sap.ui.define([             //(1)라이브러리를 컨트롤러에서 사용할 때 종속성을 등록해서 사용
    "sap/ui/core/mvc/Controller",       // 모든 UI5 프레임워크 내에서 구동하는 컨트롤러 기능을 가진 원본
    "sap/ui/model/json/JSONModel",
    "../model/formatter",
    "sap/ui/model/Filter",
    "sap/ui/model/FilterOperator",
    "sap/ui/model/Sorter",
    "sap/ui/core/Fragment",
    "sap/m/Dialog",
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (Controller, JSONModel, formatter, Filter, FilterOperator, Sorter, Fragment, Dialog) {  // (1) define에서 등록한 라이브러리의 이름을 등록해서 내부에서 그 이름 그대로 사용
        "use strict";

        // controller 의 extend 메소드를 이용해서 지금 이 컨트롤러 -> .extend("...") 이 파일을 확장해서 사용
        // .extend("[컨트롤러 파일명]", { [ 내 컨트롤러 로직 코드  (우리가 작성하는 장소 , 노트)]})
        return Controller.extend("sap.sync.ui5training.controller.View1", {
            // "sap/ui/core/mvc/Controller"의 설계구조, onInit : void
            // onInit, onExit, onBeforRendering, onAfterRendering 이 네개의 메소드(함수)는 이 뷰가 동작할때 자동으로 각자의 조건에 맞게 알아서 동작
            formatter: formatter,
            onInit: function () {       // 화면이 처음 그려질 때, 브라우저가 이 화면을 처음 만들어 낼때만
                // 주로 뷰를 컨트롤 하기 위한 모델(JSONModel)을 여기에 선언

                var oInput = this.getView().byId("IdNameInput")
                console.log(oInput)

                var oData = {
                    operator: [
                        {
                            keyName: "add",
                            valueName: "+"
                        },
                        {
                            keyName: "min",
                            valueName: "-"
                        },
                        {
                            keyName: "mul",
                            valueName: "*"
                        },
                        {
                            keyName: "div",
                            valueName: "/"
                        }
                    ],
                    score: [
                        {
                            mName: "A",
                            score1: "100",
                            score2: "100",
                            score3: "100",
                            avg: "100"
                        },
                        {
                            mName: "B",
                            score1: "100",
                            score2: "100",
                            score3: "100",
                            avg: "100"
                        },
                        {
                            mName: "C",
                            score1: "100",
                            score2: "100",
                            score3: "100",
                            avg: "100"
                        },
                        {
                            mName: "D",
                            score1: "100",
                            score2: "100",
                            score3: "100",
                            avg: "100"
                        }
                    ],
                    comboItems: [
                        {
                            key: "add", text: "+"
                        },
                        {
                            key: "min", text: "-"
                        },
                        {
                            key: "mul", text: "*"
                        },
                        {
                            key: "div", text: "/"
                        },
                    ],
                    students: [
                        {
                            name: "Alpha",
                            iscore: 100,
                            grade: "A",
                            pass: true
                        },
                        {
                            name: "Delta",
                            iscore: 50,
                            grade: "D",
                            pass: false
                        },
                        {
                            name: "Charlie",
                            iscore: 60,
                            grade: "C",
                            pass: true
                        },
                        {
                            name: "Bravo",
                            iscore: 80,
                            grade: "B",
                            pass: true
                        },
                        {
                            name: "Echo",
                            iscore: 30,
                            grade: "E",
                            pass: false
                        }
                    ],
                    dialogModel: [
                        {
                            name: "name1", count:10
                        },
                        {
                            name: "name2", count:9
                        },
                        {
                            name: "name3", count:12
                        },
                    ]
                }
                var oModel = new JSONModel(oData)
                this.getView().setModel(oModel)     // view 에 모델을 연결

                var oData1 = {
                    bVisible: true,
                    bDesc: true,
                    bTableDesc: false,
                    cDesc: true,
                    bEditable: true,
                    bButtEnable: false,
                    cVisible: true,
                    enabled: false
                }
                var oViewModel = new JSONModel(oData1)
                this.getView().setModel(oViewModel, "oView")


                console.log("************************************")
                console.log("json this.getView().getModel()", this.getView().getModel())
                console.log("json this.getView().oModel", this.getView().setModel(oModel))
                console.log("json this.getView().oViewModel", this.getView().setModel(oViewModel, "oView"))
                console.log("json oViewModel.getProperty()", oViewModel.getProperty("/bVisible"))
                // console.log("json oViewModel()" , oViewModel())

                // console.log("json 속성값 가져오기" , oViewModel.getProperty("/bButtEnable"))
                console.log("************************************")
            },

            onEnableButton: function () {
                var oInput1 = this.getView().byId("input1")
                var oInput2 = this.getView().byId("input2")

                var oSelectBox = this.getView().byId("sign")
                var sSelectKey = oSelectBox.getSelectedKey()

                var iValue1 = oInput1.getValue()
                var iValue2 = oInput2.getValue()
                var oViewModel = this.getView().getModel("oView");

                var bFlag = false;

                // if (iValue1 == "" && iValue2 == "" || iValue1 == null && iValue2 == null || iValue1 == undefined && iValue2 == undefined || ( (iValue1 != null && typeof iValue1 == "object" && !Object.keys(iValue1).length) && (iValue2 != null && typeof iValue2 == "object" && !Object.keys(iValue2).length) )){
                if (iValue1 == "" && iValue2 == "" || iValue1 == null && iValue2 == null || iValue1 == undefined && iValue2 == undefined || iValue2 == 0 && sSelectKey == "div") {
                    console.log("null 값 체크")
                    bFlag = false
                } else {
                    console.log("else")
                    bFlag = true
                }
                // console.log(this.getView().getModel().bVisible("oView"))
                console.log(bFlag)
                console.log("json 속성값 가져오기", oViewModel.oData.enabled)
                console.log("json 속성값 가져오기", oViewModel.setProperty("/bButtEnable"))
                oViewModel.setProperty("/bButtEnable", bFlag);
                // this.onF()  함수안에서 함수를 호출할때 this.함수명

            },

            onCalc: function () {
                var oViewModel = this.getView().getModel("oView")
                // console.log(oViewModel)
                // var oViewData = oViewModel.getData()
                // oViewData.setProperty("/bVisible",false)


                var oInput1 = this.getView().byId("input1")
                var oInput2 = this.getView().byId("input2")
                var oInput3 = this.getView().byId("input3")
                var sSign = this.getView().byId("sign")

                var oSelectBox = this.getView().byId("sign")
                var sSelectKey = oSelectBox.getSelectedKey()
                console.log(sSelectKey)

                // switch (sSelectKey) {
                //     case 'add':
                //         sSign.setValue(iResult);
                //       break;
                //     case 'min':
                //         sSign.setValue(iResult);
                //       break;
                //     case 'mul':
                //         sSign.setValue(iResult);
                //       break;
                //     case 'div':
                //         sSign.setValue(iResult);
                //       break;
                //     default:
                //       alert( "어떤 값인지 파악이 되지 않습니다." );
                //   }
                //   console.log(sSign)


                var sNum1 = oInput1.getValue()
                var sNum2 = oInput2.getValue()

                console.log(sNum2, sNum1)

                console.log(typeof sNum2)

                var iResult

                if (sSelectKey == "add") {
                    iResult = parseInt(sNum1) + parseInt(sNum2)
                    console.log("+", iResult)
                } else if (sSelectKey == "min") {
                    iResult = parseInt(sNum1) - parseInt(sNum2)
                    console.log("-", iResult)
                } else if (sSelectKey == "mul") {
                    iResult = parseInt(sNum1) * parseInt(sNum2)
                    console.log("*", iResult)
                } else if (sSelectKey == "div") {
                    iResult = parseInt(sNum1) / parseInt(sNum2)
                    console.log("/", iResult)
                }

                oInput3.setValue(iResult)

                console.log(oInput3)

            },

            onChange: function (oEvent) {
                // oEvent.getSource() = oInput1                        <-- 이벤트를 호출한 객체
                // var oInput1 = this.getView().byId("input1")
                // console.log(oEvent.getSource().getValue())
                // console.log(oEvent.getParameter("value"))
                var oInput1 = this.getView().byId("input1")             // Input2 입력창
                var oInput2 = this.getView().byId("input2")             // Input2 입력창
                var oInput3 = this.getView().byId("input3")             // 결과 인풋창

                var sValue1 = oInput1.getValue()             // ************* 현재 위치하는 필드의 값을 불러옴 ****************
                // var sValue1 = oEvent.getParameter("value")
                var sValue2 = oInput2.getValue()

                var oSelectBox = this.getView().byId("sign")
                var sSelectKey = oSelectBox.getSelectedKey()
                console.log(sSelectKey)

                var iResult;

                if (sValue1.length === 0) {
                    sValue1 = 0
                } else if (sValue2.length === 0) {
                    sValue2 = 0
                } else if (sValue1.length === 0 && sValue2.length === 0) {
                    sValue1 = 0
                    sValue2 = 0
                }

                if (sSelectKey == "add") {
                    iResult = parseInt(sValue1) + parseInt(sValue2)
                } else if (sSelectKey == "min") {
                    iResult = parseInt(sValue1) - parseInt(sValue2)
                } else if (sSelectKey == "mul") {
                    iResult = parseInt(sValue1) * parseInt(sValue2)
                } else if (sSelectKey == "div") {
                    iResult = parseInt(sValue1) / parseInt(sValue2)
                }

                oInput3.setValue(iResult)

                this.onEnableButton()
            },

            onCheck: function (oEvent) {
                var oInput33 = this.getView().byId("input33")
                console.log(oEvent.getSource().getParent());
                console.log(oEvent.getSource().getParent().getParent());
                // console.log(
                //     oInput33.getValue(),
                //     oEvent.getSource(),
                //     oEvent.getParameter("value"),
                //     )

            },


            onSearch: function (oEvent) {
                var oTable = this.getView().byId("uiTable"),
                    oSearchInput = this.getView().byId("searchInput"),
                    oStartScoreInput = this.getView().byId("scoreStart"),
                    oEndScoreInput = this.getView().byId("scoreEnd");
                var sStartScoreValue = oStartScoreInput.getValue(),
                    sEndScoreValue = oEndScoreInput.getValue(),
                    sSearchValue = oSearchInput.getValue();
                var oModel = oTable.getBinding("rows"); // JSONModel 자체에 필터를 걸면 그 데이터 자체가 변형
                // 테이블이 가지고 있는 바인딩 정보에 필터를 추가 / xml path: '', filters: '배열' <-
                var aFilter = []; // filter 를 담을 배열 하나 선언


                if (sStartScoreValue.length !== 0 && sEndScoreValue.length !== 0) {
                    var iStart = parseInt(sStartScoreValue)
                    var iEnd = parseInt(sEndScoreValue)
                    var oFilter = new Filter({
                        path: "iscore",
                        operator: FilterOperator.BT,
                        value1: iStart,
                        value2: iEnd,
                        caseSensitive: false        //문자열 검색시 대소문자도 판별하는 기능. false:대소문자 구별 없음, true:대소문자 구별.
                    })

                    // aFilter.push(new Filter("name", FilterOperator.Contains, "Alpha"));
                    aFilter.push(oFilter)
                } else if (sStartScoreValue.length !== 0) {
                    // 최소값에 입력이 있을경우.
                    var iStart = parseInt(sStartScoreValue)
                    var iEnd = parseInt(sEndScoreValue)
                    var oFilter = new Filter({
                        path: "iscore",
                        operator: FilterOperator.GE,
                        value1: iStart,
                        // value2: iEnd,
                        caseSensitive: false
                    });
                    aFilter.push(oFilter)
                } else if (sEndScoreValue.length !== 0) {
                    // 최대값에 입력이 있을경우.
                    var iStart = parseInt(sStartScoreValue)
                    var iEnd = parseInt(sEndScoreValue)
                    var oFilter = new Filter({
                        path: "iscore",
                        operator: FilterOperator.LE,
                        //  value1: iStart,
                        value1: iEnd,
                        caseSensitive: false
                    });
                    aFilter.push(oFilter)
                };

                if (sSearchValue.length !== 0) {
                    var oFilter = new Filter({
                        path: "name",
                        operator: FilterOperator.EQ,
                        value1: sSearchValue,
                        caseSensitive: false        //문자열 검색시 대소문자도 판별하는 기능. false:대소문자 구별 없음, true:대소문자 구별.
                    })

                    // aFilter.push(new Filter("name", FilterOperator.Contains, "Alpha"));
                    aFilter.push(oFilter)
                }
                // push 배열에 항목을 추가할 때 js 문법(메소드)

                // new Filter("name", FilterOperator.Contains, "lee")
                // ( sPath, 조건, sQuery(검색문) )

                oModel.filter(aFilter)

            },

            onSort: function () {
                var oTable = this.getView().byId("uiTable"),
                    oModel = oTable.getBinding("rows");
                var oViewModel = this.getView().getModel();
                // var bDesc = this.getView().getModel().getProperty("/bDesc");
                var bDesc = oViewModel.getProperty("/bDesc");
                console.log(bDesc)

                if (bDesc) {
                    oViewModel.setProperty("/bDesc", !bDesc);    // !ture = false
                } else {    // bDesc === false
                    oViewModel.setProperty("/bDesc", true);
                }

                var oSorter = new Sorter("name", bDesc);

                oModel.sort(oSorter);

            },

            _tableSearch: function () {
                var oTable = this.getView().byId("table"),
                    oModel = oTable.getBinding("items");       // == oInput = this.getView().byId("search01")
                var oInput = this.getView().byId("search01"),       // 검색입력창
                    sValue = oInput.getValue();                     // 검색텍스트값

                var aFilter = [];   // 1) arry TYPE 필터를 담을 빈 배열 선언
                var oSearchFilter;

                // // 2) 원하는 조건의 경로와 필터 하나를 생성
                // var oSearchFilter = new Filter(
                //     {
                //         path: 'name',                         // 리스트 내부 프로퍼티 경로(컬럼)
                //         operator: FilterOperator.Contains,    // FilterOperator 라는 이미 정해진 라이브러리 선택에서 사용
                //         value1: sValue                        // 필수값, 찾고자 하는 키워드
                //     }
                // ); // path, operator, value 필수 속성(프로퍼티) 

                // // 3) aFilter 라는 배열에 생성한 필터를 넣어줌
                // aFilter.push(oSearchFilter);

                if (sValue !== "") {
                    oSearchFilter = new Filter(
                        {
                            path: 'name',
                            operator: FilterOperator.Contains,
                            value1: sValue
                        }
                    );

                    aFilter.push(oSearchFilter);
                }

                console.log("oSearchFilter : ",oSearchFilter)
                // oModel.filter(aFilter); // 최종) 테이블의 바인딩 정보에 필터를 적용
                return oSearchFilter
            },

            // onTableSort: function () {
            //     var oTable = this.getView().byId("table"),
            //         oModel = oTable.getBinding("items");

            //     var oSoter = new Sorter("name",true)   // 기본은 오름차순, 두번째 생략하면 오름차순. new Sorter("name",false)
            //     // (경로와 정렬방식(기본값이 false/생략하면 aesc))
            //     oModel.sort(oSoter);
            // }

            onTableSort: function () {
                var oTable = this.getView().byId("table"),
                    oModel = oTable.getBinding("items");
                var oViewModel = this.getView().getModel(),
                    bTableDesc = oViewModel.getProperty("/bTableDesc");
                // var cDesc = oViewModel.getProperty("/cDesc");

                // if (bTableDesc) { // bTableDesc == true
                //     oViewModel.setProperty("/bTableDesc", !bTableDesc);    // !ture = false
                // } else {
                //     oViewModel.setProperty("/bTableDesc", true);
                // }

                oViewModel.setProperty("/bTableDesc", !bTableDesc);

                var oSorter = new Sorter("name",bTableDesc)   // 기본은 오름차순, 두번째 생략하면 오름차순. new Sorter("name",false)
                // (경로와 정렬방식(기본값이 false/생략하면 aesc))
                oModel.sort(oSorter);
            },

            _tableNumberFilter: function() {
                var oTable = this.getView().byId("table"),
                    oModel = oTable.getBinding("items");
                var oInputMin = this.getView().byId("inputNum1"),
                    oInputMax = this.getView().byId("inputNum2");
                var sMinValue = oInputMin.getValue(),
                    sMaxValue = oInputMax.getValue();

                var aFilter = [];
                var oFilter;

                if (sMinValue !== "" && sMaxValue !== "") {
                    oFilter = new Filter ({
                            path: "iscore",
                            operator: FilterOperator.BT,
                            value1: parseInt(sMinValue),
                            value2: parseInt(sMaxValue)
                    });
                    aFilter.push(oFilter);
                } else if (sMinValue !== "") {
                    oFilter = new Filter ({
                            path: "iscore",
                            operator: FilterOperator.GE,
                            value1: parseInt(sMinValue)
                    });
                    aFilter.push(oFilter);
                    console.log(oFilter)
                } else if (sMaxValue !== "") {
                    oFilter = new Filter ({
                            path: "iscore",
                            operator: FilterOperator.LE,
                            value1: parseInt(sMaxValue)
                    });
                    aFilter.push(oFilter);
                }

                // oModel.filter(aFilter);
                return oFilter;
            },

            onTotalSearch: function() {
                var oTable = this.getView().byId("table"),
                    oModel = oTable.getBinding("items");       // == oInput = this.getView().byId("search01")
                var aFilter = [];
                var oFilter = [];

                var oInputFilter1 = this._tableSearch();
                var oInputFilter2 = this._tableNumberFilter();

                if (oInputFilter1) {            // 필터값 undefined 가르기
                    aFilter.push(oInputFilter1);        //  path "name"
                }
                if (oInputFilter2) {
                    aFilter.push(oInputFilter2);        //  path "iscore"
                }
                // path 가 다른 필터 여러개가 조합되면 AND 조건으로 검색
                oModel.filter(aFilter);
            },

            onCreateDialog: function () {
                if (!this.pDialog) {        // 기본구조. pDialog 가 이미 존재하면 생성안함.
                    this.pDialog = this.loadFragment({
                        name: "sap.training.sync.training.view.Hello"
                    });
                } 
                this.pDialog.then(function(oDialog) {
                    oDialog.open(); // 다이얼로그를 켜줌
                });
            },

            onCloseDialog: function() {
                var oDialog = this.getView().byId("helloDialog")
                
                oDialog.close();
            },
            
            onCreateDialog2: function() {
                if (!this.pDialog) {    // this.pDialog 가 이미 존재하면 생성안함
                    // this.pDialog = this.loadFragment({
                    //     name: "sap.sync.ui5training.view.Hello"
                    // });

                    this.pDialog = new Dialog({
                        title: "Sample Dialog",
                        content: new sap.m.List({
                            items: {
                                path: "/dialogModel",
                                template: new sap.m.StandardListItem({
                                    title: "{name}",
                                    counter: "{count}"
                                })
                            }
                        })
                    })
                    this.getView().addDependent(this.pDialog);
                }

                this.pDialog.open();
                // this.pDialog.then(function(oDialog) {
                //     oDialog.open(); // 다이얼로그를 켜줌
                // });
            },

            onCloseDialog: function() {
                var oDialog = this.getView().byId("helloDialog");

                oDialog.close();
            }

        });
    });
