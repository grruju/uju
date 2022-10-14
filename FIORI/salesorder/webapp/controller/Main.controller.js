sap.ui.define([
    "sap/ui/core/mvc/Controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageToast",
    "sap/ui/model/Filter",
    "sap/ui/model/odata/v2/ODataModel"
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (Controller, JSONModel, MessageToast, Filter, ODataModel) {
        "use strict";
        /**
         * oEditRow : 상단 테이블의 row가 클릭될 때 생성됨
         * Header테이블에서 선택된 라인의 셀 정보를 저장하는 변수임.
         * 수정중에 다른 라인을 클릭해도 기존에 선택한 라인이 변경되지 않도록 글로벌로 선언함.
         */
        var oEditRow = null;
        var oEditItemRow = null;
        /**
         * # oCreatedRow : 생성 버튼을 눌렀을 때 생성됨.
         * 새로 생성된 라인을 지정하는 변수임.
         */
        var oCreatedRow = null;
        var oCreatedItemRow = null;


        /***************************************************************************************
         * 커스텀 데이터 설정
         */
        //Header테이블 네임 설정
        var sHeaderTable    = "table";
        //Item테이블 네임 설정
        var sItemTable      = "table2";
        //Header-Item Key 설정
        var sItemKey        = "Ornum";

        //View에서 필드 타입이 Input이어야 적용됨
        //Header 테이블의 수정 가능한 필드 지정
        var aHeaderEditable = [2, 3, 4];
        //Item테이블의 수정 가능한 필드 지정
        var aItemEditable   = [2, 3, 4, 5, 6, 7];

        //Header데이터를 Insert하기 전 생성할 기본값을 세팅
        function headerInit() {
            var oData = {
                /************************/
                Ornum   : "",        //키값을 Gateway에서 Number range로 생성하므로 빈 값 전달
                Ortype  : "판매",
                Empnm     : "강우주",
                Stats   : "대기"
                /************************/
            };return oData;
        }
        //Header에서 수정/저장되는 필드를 지정
        //Key필드 : getText(), Update필드: getValue()
        function headerUpdateField(targetRow){
            var oData = {
                /************************/
                Ornum   : targetRow[0].getText(),
                Ortype  : targetRow[1].getText(),
                Vencd   : targetRow[2].getValue(),
                Vennm   : targetRow[3].getValue(),
                // Ordat   : targetRow[4].getText(),
                // Drdat   : targetRow[5].getText(),
                Empnm   : targetRow[6].getText(),
                Stats   : targetRow[7].getText()
                /************************/
            };return oData;
        }

        //Item데이터를 Insert하기 전 생성할 기본값을 세팅
        function itemInit() {
            var oData = {
                /************************/
                Ornum : oEditRow[0].getProperty('text')
                /************************/
            };return oData;
        }
        //Item에서 수정/저장되는 필드를 지정
        //Key필드 : getText(), Update필드: getValue()
        function itemUpdateField(targetRow){
            var oData = {
                /************************/
                Ornum : targetRow[0].getText(),
                Itmnm : targetRow[1].getText(),
                Matcd : targetRow[2].getValue(),
                Matnm : targetRow[3].getValue(),
                Meinm : targetRow[4].getValue(),
                Meins : targetRow[5].getValue(),
                Price : targetRow[6].getValue(),
                Waers : targetRow[7].getValue()
                /************************/
            };return oData;
        }
        /**
         * 
         ***************************************************************************************/


        /**
         * 브라우저 종료/새로고침 시 임시로 생성된 row를 삭제하기 위한 변수
         */
        var bCreateMode = false;
        var oExitModel = new ODataModel("");
        var sExitPath = null;
        var bCreateItemMode = false;
        var oExitItemModel = new ODataModel("");
        var sExitItemPath = null;

        //Header테이블의 수정 가능한 필드를 지정
        function setInputEdit(cells, bFlag){
            aHeaderEditable.forEach(function(index){
                cells[index].setEditable(bFlag);
            });
        };
        //Item테이블의 수정 가능한 필드를 지정
        function setItemInputEdit(cells, bFlag){
            aItemEditable.forEach(function(index){
                cells[index].setEditable(bFlag);
            });
        };

        return Controller.extend("salesorder.controller.Main", {
            onInit: function () {
                var oTog = {
                    /**
                     * __Normal: 기본, __Create: 생성, __Edit: 수정, __Delete: 삭제,
                     * __CreateItem: 생성, __EditItem: 수정, __DeleteItem: 삭제
                     */
                    stat: "__Normal"
                }
                var oTogModel = new JSONModel(oTog);
                this.getView().setModel(oTogModel, "tog");

                //브라우저 종료 이벤트 생성
                window.addEventListener("beforeunload", function(){
                    if(bCreateMode == true){
                        oExitModel.remove(sExitPath);
                    }
                    if(bCreateItemMode == true){
                        oExitItemModel.remove(sExitItemPath);
                    }
                });
            },

            onRefresh: function(){
                this.getView().getModel().refresh(true); 
                MessageToast.show("새로고침 되었습니다.");
            },

            onSalesOrdersSelect: function(oEvent){
                var oTable = this.getView().byId(sHeaderTable);
                var oTable2 = this.getView().byId(sItemTable);
                var oModel = this.getView().getModel();
                var oToggleModel = this.getView().getModel("tog");

                if (oToggleModel.getProperty("/stat") === '__Normal') {
                    //선택된 row의 cell정보 저장
                    oEditRow = oTable.getSelectedItem().getAggregation('cells');
                    var sKey = oModel.getProperty(oEvent.getParameter("listItem").getBindingContextPath())[sItemKey];
                    oTable2.getBinding('items').filter(new Filter(sItemKey, "EQ", sKey));
                }else{
                    MessageToast.show("데이터 수정중에는\n선택할 수 없습니다.");
                }
            },

            onEditMode: function() {
                if (oEditRow == null) {
                    MessageToast.show("데이터를 선택해주세요.");
                    return;
                };

                var oToggleModel = this.getView().getModel("tog");
                oToggleModel.setProperty("/stat", "__Edit");
                
                setInputEdit(oEditRow, true);
            },

            onEditCancel: function() {
                var oToggleModel = this.getView().getModel("tog");
                oToggleModel.setProperty("/stat", "__Normal");
                
                setInputEdit(oEditRow, false);
                this.getView().getModel().refresh(true); 
            },

            onUpdateData: function(){
                var oModel = this.getView().getModel();
                var oTable = this.getView().byId(sHeaderTable);
                var oToggleModel = this.getView().getModel("tog");

                var sPath = oTable.getSelectedContextPaths()[0];

                oModel.update(sPath, headerUpdateField(oEditRow), {
                    success: function() {
                        MessageToast.show("변경 되었습니다.");
                    }
                });
                oToggleModel.setProperty("/stat", "__Normal");
                setInputEdit(oEditRow, false);
            },

            onCreateMode: function(){
                var oToggleModel = this.getView().getModel("tog");
                oToggleModel.setProperty("/stat", "__Create");
                var oModel = this.getView().getModel();
                var oTable = this.getView().byId(sHeaderTable);
                bCreateMode = true;

                //선택된 데이터 초기화 : 새로 라인을 생성한 후 재할당해야 함
                oEditRow = null;

                oModel.create("/SalesOrderSet", headerInit(), {
                    Success: function(){
                        MessageToast.show("데이터가 생성되었습니다.");
                    }
                });

                setTimeout(function(){
                    oTable = this.getView().byId(sHeaderTable);
                    oCreatedRow = oTable.getAggregation('items')[0].getAggregation('cells');
                    setInputEdit(oCreatedRow, true);

                    //브라우저가 종료될 때를 대비한 remove경로 생성
                    oExitModel = this.getView().getModel();
                    sExitPath = oTable.getAggregation('items')[0].getBindingContextPath();
                }.bind(this), 200);
            },

            onCreateData: function(){
                var oModel = this.getView().getModel();
                var oTable = this.getView().byId(sHeaderTable);
                var oToggleModel = this.getView().getModel("tog");

                debugger;

                var sPath = oTable.getAggregation('items')[0].getBindingContextPath();

                oModel.update(sPath, headerUpdateField(oCreatedRow), {
                    success: function() {
                        MessageToast.show("저장 되었습니다.");
                    }
                });

                oToggleModel.setProperty("/stat", "__Normal");
                setInputEdit(oCreatedRow, false);
                oCreatedRow = null;
                bCreateMode = false;
                sExitPath = null;
            },

            onCreateCancel: function(){
                var oToggleModel = this.getView().getModel("tog");
                oToggleModel.setProperty("/stat", "__Normal");

                var oModel = this.getView().getModel();
                var oTable = this.getView().byId(sHeaderTable);
                var sPath = oTable.getAggregation('items')[0].getBindingContextPath();

                oModel.remove(sPath, {
                    success: function(){
                        MessageToast.show("생성을 취소했습니다.");
                    }
                });

                oCreatedRow = null;
                bCreateMode = false;
                sExitPath = null;
            },

            onDeleteMode: function(){
                var oToggleModel = this.getView().getModel("tog");
                oToggleModel.setProperty("/stat", "__Delete");

                this.byId(sHeaderTable).setMode("Delete");
            },

            onDeleteCancel: function() {
                var oToggleModel = this.getView().getModel("tog");
                oToggleModel.setProperty("/stat", "__Normal");

                this.byId(sHeaderTable).setMode("SingleSelectMaster");
            },

            onDeleteData: function(oEvent) {
                var oModel = this.getView().getModel();
                var sPath = oEvent.getParameter("listItem").getBindingContextPath();
                var sKey = oModel.getProperty(sPath).Ornum;

                //Delete 요청 처리
                if(confirm("선택된 데이터 : "+ sKey +"\n삭제하시겠습니까?")){
                    oModel.remove(sPath, {
                        success: function(){
                            MessageToast.show("삭제 되었습니다.");
                        }
                    });
                }
            },

            //ITEM////////////////////////////////////////////////////////////////////////////////////////////////////

            onSalesOrderItemsSelect: function(){
                var oTable = this.getView().byId(sItemTable);
                var oToggleModel = this.getView().getModel("tog");

                if (oToggleModel.getProperty("/stat") === '__Normal') {
                    //선택된 row의 cell정보 저장
                    oEditItemRow = oTable.getSelectedItem().getAggregation('cells');
                }else{
                    MessageToast.show("데이터 수정중에는\n선택할 수 없습니다.");
                }
            },

            onItemEditMode: function() {
                if (oEditItemRow == null) {
                    MessageToast.show("데이터를 선택해주세요.");
                    return;
                };

                var oToggleModel = this.getView().getModel("tog");
                oToggleModel.setProperty("/stat", "__EditItem");
                
                setItemInputEdit(oEditItemRow, true);
            },

            onItemEditCancel: function() {
                var oToggleModel = this.getView().getModel("tog");
                oToggleModel.setProperty("/stat", "__Normal");
                
                setItemInputEdit(oEditItemRow, false);
                this.getView().getModel().refresh(true); 
            },

            onItemUpdateData: function(){
                var oModel = this.getView().getModel();
                var oTable = this.getView().byId(sItemTable);
                var oToggleModel = this.getView().getModel("tog");

                var sPath = oTable.getSelectedContextPaths()[0];

                oModel.update(sPath, itemUpdateField(oEditItemRow), {
                    success: function() {
                        MessageToast.show("변경 되었습니다.");
                    }
                });
                oToggleModel.setProperty("/stat", "__Normal");
                setItemInputEdit(oEditItemRow, false);
            },

            onItemCreateMode: function(){
                var oToggleModel = this.getView().getModel("tog");
                var oModel = this.getView().getModel();
                var oTable = this.getView().byId(sItemTable);

                if (!(oEditRow == null)) {
                    oToggleModel.setProperty("/stat", "__CreateItem");
                    bCreateItemMode = true;

                    //선택된 데이터 초기화 : 새로 라인을 생성한 후 재할당해야 함
                    oEditItemRow = null;
                    
                    oModel.create("/SalesOrderItemSet", itemInit(), {
                        Success: function(){
                            MessageToast.show("데이터가 생성되었습니다.");
                        }
                    });

                    setTimeout(function(){
                        oTable = this.getView().byId(sItemTable);
                        oCreatedItemRow = oTable.getAggregation('items')[0].getAggregation('cells');
                        setItemInputEdit(oCreatedItemRow, true);

                        //브라우저가 종료될 때를 대비한 remove경로 생성
                        oExitItemModel = this.getView().getModel();
                        sExitItemPath = oTable.getAggregation('items')[0].getBindingContextPath();
                    }.bind(this), 800);
                }else{
                    MessageToast.show("헤더 라인이\n선택되지 않았습니다.");
                }

            },

            onItemCreateData: function(){
                var oModel = this.getView().getModel();
                var oTable = this.getView().byId(sItemTable);
                var oToggleModel = this.getView().getModel("tog");

                var sPath = oTable.getAggregation('items')[0].getBindingContextPath();

                oModel.update(sPath, itemUpdateField(oCreatedItemRow), {
                    success: function() {
                        MessageToast.show("저장 되었습니다.");
                    }
                });

                oToggleModel.setProperty("/stat", "__Normal");
                setItemInputEdit(oCreatedItemRow, false);
                oCreatedItemRow = null;
                bCreateItemMode = false;
                sExitItemPath = null;
            },

            onItemCreateCancel: function(){
                var oToggleModel = this.getView().getModel("tog");
                oToggleModel.setProperty("/stat", "__Normal");

                var oModel = this.getView().getModel();
                var oTable = this.getView().byId(sItemTable);
                var sPath = oTable.getAggregation('items')[0].getBindingContextPath();

                oModel.remove(sPath, {
                    success: function(){
                        MessageToast.show("생성을 취소했습니다.");
                    }
                });

                oCreatedItemRow = null;
                bCreateItemMode = false;
                sExitItemPath = null;
            },

            onItemDeleteMode: function(){
                var oToggleModel = this.getView().getModel("tog");
                oToggleModel.setProperty("/stat", "__DeleteItem");

                this.byId(sItemTable).setMode("Delete");
            },

            onItemDeleteCancel: function() {
                var oToggleModel = this.getView().getModel("tog");
                oToggleModel.setProperty("/stat", "__Normal");

                this.byId(sItemTable).setMode("SingleSelectMaster");
            },

            onItemDeleteData: function(oEvent) {
                var oModel = this.getView().getModel();
                var sPath = oEvent.getParameter("listItem").getBindingContextPath();
                var sKey = oModel.getProperty(sPath).Ornum;

                //Delete 요청 처리
                if(confirm("선택된 데이터 : "+ sKey +"\n삭제하시겠습니까?")){
                    oModel.remove(sPath, {
                        success: function(){
                            MessageToast.show("삭제 되었습니다.");
                        }
                    });
                }
            },

        });
    });
