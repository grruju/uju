sap.ui.define([
	"../lib/BaseController",
    "sap/ui/model/json/JSONModel"
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (Controller, JSONModel) {
        "use strict";

        return Controller.extend("sap.btp.usetemplate.controller.PDFExample", {
            onInit: function () {
                this._setInitModel();
            },

            /**
             * 해당 페이지 기본 모델 세팅
             */
            _setInitModel: function() {
                this.getView()
                    .setModel(
                        new JSONModel({
                            "orderNo": ' 20091201',
                            "name": '김정호',
                            "companyRegNumber": '777-77-12345',
                            "mutual": 'SYNC1기',
                            "supplierName": "홍길동",
                            "businessLocation": '서울특별시 관악구 신림동 OO빌딩5층',
                            "jobGroup": '도소매',
                            "event": 'OO류',
                            "phone": '010 - 8835 - ****'
                        }),
                        'pdf'
                    )
            },

            /**
             * PDF 팝업창이 열린 뒤 발생하는 이벤트
             * 영수증에 각 데이터를 세팅하는 작업.
             * @param {obejct} oEvent 
             */
            onAfterOpen: function(oEvent) {
                const oControl = oEvent.getSource(),
                      oPdfModel = oControl.getModel('pdf'),
                      oProperty = oPdfModel.getProperty('/');
                
                oControl.setBusy(true);

                Object.keys(oProperty)
                      .forEach((property) => {
                            document.getElementById(property)
                                    .innerHTML = oProperty[property];
                      });

                oControl.setBusy(false);
            },

            /**
             * PDF 팝업창 열기
             */
            onPDFDialolgOpen: function() {
                /**
                 * ../lib/BaseController -> _loadFragment
                 */
                this._loadFragment({
                    fragmentName: "PDFDialog",
                    handler: function(oFragment) {

                        this.getView().addDependent(oFragment);
                        oFragment.open();

                    }.bind(this),
                    controller: this
                });
            },

            /**
             * 팝업창 닫기
             * @param {objst} oEvent 
             * @param {string} sFragmentName 
             */
            onDialogClose: function(oEvent, sFragmentName) {
                this._oFragments[sFragmentName].close();
            },

            /**
             * PDF 다운로드
             */
            onDownload: function() {
                const oDialog = this._oFragments["PDFDialog"],
                      oContent = oDialog._$content.context;

                html2canvas(oContent).then((canvas) => {
                    // 캔버스를 이미지로 변환
                    const imgData = canvas.toDataURL("image/png");
                  
                    const doc = new jsPDF({
                      orientation: "p",
                      unit: "mm",
                      format: "a4",
                    });
                  
                    doc.addImage(imgData, "PNG", 0, 0);
                  
                    doc.save("receipt.pdf");
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
