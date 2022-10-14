sap.ui.define([
    "sap/ui/core/mvc/Controller",
    "sap/ui/model/json/JSONModel",
    "sap/m/MessageToast",
    "sap/ui/model/Filter"
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (Controller, JSONModel, MessageToast, Filter) {
        "use strict";

        return Controller.extend("ztc2sd03001h.controller.View1", {
            onInit: function () {
                var oData = {
                    salesOrderNum : null,
                    salesOrderMemo : null
                };
                var oModel = new JSONModel(oData);
                this.getView().setModel(oModel, "view");
            },
            onCreate: function(){
                var oModel = this.getView().getModel();
                debugger;

                // var oViewModel = this.getView().getModel("view");
                // var sSonum = oViewModel.getProperty("/salesOrderNum");
                // var sMemo  = oViewModel.getProperty("/salesOrderMemo");
                
                // var oCreateData = {
                //     Sonum : sSonum,
                //     Memo : sMemo
                // };

                // oModel.create("/SalesOrderSet", oCreateData, {
                //     success: function() {
                //         oViewModel.setProperty("/salesOrderNum", null);
                //         oViewModel.setProperty("/salesOrderMemo", null);
                //         MessageToast.show("저장 되었습니다.");
                //     }
                // });
            },

            onPressEdit: function() {
                this.byId("table").setMode("SingleSelectMaster");
            },

            onPressDel: function(){
                this.byId("table").setMode("Delete");
            },

            onPressItem: function(oEvent){
                var sPath = oEvent.getParameter("listItem").getBindingContextPath();
                var oModel = this.getView().getModel();

                var oData = oModel.getProperty(sPath);
                var oViewModel = this.getView().getModel("view");

                oViewModel.setProperty("/salesOrderNum", oData.Sonum);
                oViewModel.setProperty("/salesOrderMemo", oData.Memo);
            },

            onUpdate: function(){
                var oModel = this.getView().getModel();
                var oViewModel = this.getView().getModel("view");
                
                var sSonum = oViewModel.getProperty("/salesOrderNum");
                var sMemo  = oViewModel.getProperty("/salesOrderMemo");

                var oData = {
                    Sonum : sSonum,
                    Memo : sMemo
                };

                var sPath = "/SalesOrderSet('" + sSonum + "')";

                oModel.update(sPath, oData, {
                    success: function() {
                        MessageToast.show("변경 되었습니다.");
                    }
                });
            },

            onRefresh: function(){
                this.getView().getModel().refresh(true); 
                MessageToast.show("새로고침 되었습니다.");
            },

            onSalesOrdersSelect: function(oEvent){
                var oTable = this.getView().byId('SalesOrderItems');
                var oModel = this.getView().getModel();
                var sKey = oModel.getProperty(oEvent.getParameter("listItem").getBindingContextPath()).Ornum;

                oTable.getBinding('items').filter(new Filter("Ornum", "EQ", sKey));
                debugger;
            }
        });
    });