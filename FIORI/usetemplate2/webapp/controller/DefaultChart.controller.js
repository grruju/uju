sap.ui.define([
	"../lib/BaseController"
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (Controller) {
        "use strict";

        return Controller.extend("sap.btp.usetemplate.controller.DefaultChart", {
            onInit: function () {
                /**
                 * 기본 차트 속성 설정 및 데이터 팝업 세팅
                 */
                this.setVizFrameSetting({
                    controlid: 'staticChart',
                    popoverid: "staticPopover"
                });
            },

            /**
             * 버튼 Press 이벤트
             * 사용자가 해당 이벤트를 발생시키면 이전페이지로 갈수 있도록 한다.
             */
            onNavBackPress: function() {
                /**
                 * parameter - string
                 * 해당 페이지의 이전 페이지 routing name을 넣어준다.
                 */
                this.backPage("Main");
            }
        });
    });
