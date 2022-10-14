sap.ui.define([
    "sap/ui/core/mvc/Controller",
    "sap/ui/model/json/JSONModel",
	"sap/m/MessageBox",
    "sap/ui/model/Filter",
    "sap/ui/model/FilterOperator",
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (Controller, JSONModel, MessageBox,Filter,FilterOperator) {
        "use strict";

        return Controller.extend("sap.sync.sample.controller.View1", {
            onInit: function () {
                var oViewData = {
                    students: [
                        {
                            name: "Lee",
                            score1: "F",
                            score2: "B",
                            result: ""
                        },
                        {
                            name: "Kim",
                            score1: "B",
                            score2: "B",
                            result: ""
                        },
                        {
                            name: "Woo",
                            score1: "D",
                            score2: "A",
                            result: ""
                        },
                        {
                            name: "Kang",
                            score1: "F",
                            score2: "C",
                            result: ""
                        },
                        {
                            name: "Hwang",
                            score1: "A",
                            score2: "A",
                            result: ""
                        },
                        {
                            name: "Jo",
                            score1: "C",
                            score2: "B",
                            result: ""
                        },
                    ],
                    searchValue: ""     // 검색창 프로퍼티
                };

                var oViewModel = new JSONModel(oViewData);
                this.getView().setModel(oViewModel);
 
            },
            onSearch: function() {
                var oViewModel = this.getView().getModel();    // JSONModel
                var sSearchText = oViewModel.getProperty("/searchValue");   // 모델에서 프로퍼티 값을 받아옴

                var oTable = this.getView().byId("uiTable");    // ui.table 자체
                var oBinding = oTable.getBinding("rows");       // ui.table 의 바인딩 정보 <-- [필터 적용대상]

                var aFilter = [];       // 필터를 담을 배열 선언

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
        });
    });
