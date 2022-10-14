sap.ui.define([
    "sap/ui/core/mvc/Controller",
    "sap/ui/model/json/JSONModel",
	"sap/m/MessageBox",
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (Controller, JSONModel, MessageBox) {
        "use strict";

        return Controller.extend("sap.sync.sample.controller.View1", {
            onInit: function () {
                var oViewData = {
                    value1 : "",
                    value2 : "",
                    result : "",
                    dateString : "",
                    input10 : "",
                    results : [
                        {
                            string : "1"
                        },
                        {
                            string : "2"
                        },
                        {
                            string : "3"
                        },
                        {
                            string : "4"
                        },
                        {
                            string : "5"
                        },
                        {
                            string : "6"
                        },
                        {
                            string : "7"
                        },
                        {
                            string : "8"
                        },
                        {
                            string : "9"
                        }
                    ],
                    
                    results2 : [
                        {
                            string2 : "1"
                        },
                        {
                            string2 : "2"
                        },
                        {
                            string2 : "3"
                        },
                        {
                            string2 : "4"
                        },
                        {
                            string2 : "5"
                        },
                        {
                            string2 : "6"
                        },
                        {
                            string2 : "7"
                        },
                        {
                            string2 : "8"
                        },
                        {
                            string2 : "9"
                        }
                    ]
                };

                var oViewModel = new JSONModel(oViewData);
                this.getView().setModel(oViewModel);

            },

            onTestbyId: function () {
                var oInput1   = this.getView().byId("input1");
                var oInput2   = this.getView().byId("input2");
                var oInput3   = this.getView().byId("result");
                var oInput4   = this.getView().byId("result2");

                var iValue1 = oInput1.getValue();
                var iValue2 = oInput2.getValue();

                var iResult
                var iResult2

                console.log("log : ", iValue1, iValue2);
                
                if (iValue1 == "" || iValue1 == "undefined") {
                    iValue1 = 0
                }
                if (iValue2 == "" || iValue2 == "undefined") {
                    iValue2 = 0
                }

                if (iValue1 > iValue2) {
                    iResult = ">";
                    iResult2 = "숫자1의 값 " + iValue1 + " 는 숫자2의 값 " + iValue2 + "보다 큰 값입니다.";
                } else if (iValue1 < iValue2) {
                    iResult = "<";
                    iResult2 = "숫자1의 값 " + iValue1 + " 는 숫자2의 값 " + iValue2 + "보다 작은 값입니다."
                } else if (iValue1 == iValue2) {
                    iResult = "=";
                    iResult2 = "숫자1의 값 " + iValue1 + " 는 숫자2의 값 " + iValue2 + "와 같은 값입니다."
                }
                oInput3.setValue(iResult)
                oInput4.setValue(iResult2)
                console.log("log : ", iResult, iResult2);
            },

            onTestModel: function() {
                // 1- 모델을 읽어옴
                var oViewModel = this.getView().getModel();
                var sInputValue1 = oViewModel.getProperty("/sValue1"),
                    sInputValue2 = oViewModel.getProperty("/sValue2");

                // 2- 문자열 값을 숫자로 변경 parseInt()
                var iNum1 = parseInt(sInputValue1),
                    iNum2 = parseInt(sInputValue2);

                var sRlt = "";
                // 3- 조건 판별
                if(iNum1 === iNum2) {
                    sRlt = "=";
                } else if (iNum1 > iNum2) {
                    sRlt = ">";
                } else if (iNum1 < iNum2) {
                    sRlt = "<";
                }

                oViewModel.setProperty("/sResult", sRlt);
            },
            onDateChange: function(oEvent) {

                // var oDatePicker = oEvent.getSource();
                // console.log(oDatePicker.getDateValue(), oDatePicker.getValue());

                var oViewModel = this.getView().getModel();
                var oDatePicker = oEvent.getSource();
                var oDate = oDatePicker.getDateValue(); // Date 형식의 값을 추출

                var sYear = (oDate.getFullYear().toString());
                var sMonth = ("00" + (oDate.getMonth()+1).toString()).slice(-2);
                var sDate = ("00" + (oDate.getDate().toString())).slice(-2);

                var sDate = sYear+'-'+sMonth+'-'+sDate;

                oViewModel.setProperty("/dateString", sDate);

            },

            onSuccessMessageBoxPress: function () {
                var oViewModel = this.getView().getModel();
                var sInputValue1 = oViewModel.getProperty("/sValue10");
                var iNum = parseInt(sInputValue1)
                var aResults = [];
                    for (var i = 1; i < 10; i++) {
                        var iResult = iNum * i;
                        var sStr = iNum + " X " + i + " = " + iResult + "\n";
                        aResults.push(sStr);
                    }
                    oViewModel.setProperty("/TextArea", aResults.join(""));
            },

            onCalc: function() {
                var oViewModel = this.getView().getModel();
                var sInputValue1 = oViewModel.getProperty("/sValue10");
                var iNum = parseInt(sInputValue1)

                for (var i = 1; i < 10; i++) {
                    var iResult = iNum * i;
                    var sStr = iNum + " X " + i + " = " + iResult;

                    var sPath = "/results/" + (i-1) + "/string";
                    oViewModel.setProperty(sPath, sStr);
                }
            },

            onStar: function () {
                var oViewModel = this.getView().getModel();
                var sInputValue1 = oViewModel.getProperty("/sValue10");
                var iNum = parseInt(sInputValue1);
                

                for (var i = 1; i < 10; i++) {
                    var sStr = "";
                    var jMax = (i > iNum) ? (iNum - (i - iNum)) : i;

                    var jMax;

                    if (i > iNum) {
                        jMax = (iNum - (i-iNum)) > 0 ? (2*iNum -i) : 1;
                    } else {
                        jMax = i;
                    }

                    for(var j=1; j<=jMax ; j++) {
                        sStr = sStr + "*";
                        console.log(sStr)
                    }
                    

                    var sPath = "/results2/" + (i-1) + "/string2";
                    oViewModel.setProperty(sPath, sStr);
                }
            }

        });
    });
