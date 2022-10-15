sap.ui.define([
	"../lib/BaseController"
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (Controller) {
        "use strict";

        return Controller.extend("sap.btp.usetemplate.controller.Main", {
            onInit: function () {
                
            },

            /**
             * 버튼 클릭 이벤트
             * 페이지 이동
             */
            onNextPage: function(oEvent, sRoutingName) {
                let oParameter = this._getNavDefaultSetting(sRoutingName);

                /**
                 * nextPage
                 * @param {object}
                 * - path {string} // 라우팅 네임
                 * - parameter {object} // hash parameter
                 */
                this.nextPage({
                    path: sRoutingName,
                    parameter: oParameter
                });
            },

            /**
             * 페이지에 맞는 기본 파라미터 세팅함수
             * @param {string} sName 
             * @returns {object}
             */
            _getNavDefaultSetting: function(sName){
                debugger;
                let oParameter = {};

                switch (sName) {
                    case "DynamicType":
                        oParameter.type = "bar";
                        break;
                
                    default:
                        break;
                }

                return oParameter;
            }
        });
    });
