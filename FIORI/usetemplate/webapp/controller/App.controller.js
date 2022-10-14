sap.ui.define([
	"../lib/BaseController"
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (Controller) {
        "use strict";

        return Controller.extend("sap.btp.usetemplate.controller.App", {
            onInit: function () {
                let oAppModel, bPhone;

                bPhone = sap.ui.Device.support.touch;
                
                let sWidth = sap.ushell.services.AppConfiguration.getMetadata.fullWidth
                           ? "exit-full-screen" 
                           : "full-screen";
                
                oAppModel = this.getOwnerComponent().getModel("app");
                oAppModel.setData({
                    screenSizeButton: "sap-icon://" + sWidth,
                    phone: bPhone,
                    styleClass: bPhone ? "sapUiSizeCozy" : "sapUiSizeCompact"
                });

                this.getView().addStyleClass(oAppModel.getProperty("/styleClass"));
            }
        });
    });
