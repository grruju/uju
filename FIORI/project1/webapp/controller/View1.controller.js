sap.ui.define([
    "sap/ui/core/mvc/Controller",
	"sap/m/MessageToast",
    "sap/ui/model/json/JSONModel",

],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (Controller, MessageToast, JSONModel) {
        "use strict";

        return Controller.extend("project1.controller.View1", {
            onInit: function () {
                var oData = {
                    "htmlcontent" : null
                };
                this.getView().setModel(new JSONModel(oData), "view");
                var that = this; //function을 호출할 때 this를 사용하기 위해 변수에 저장
                //Rich Text Editor - html에디터
                //xml에서 그리면 문제가 종종 발생함
                //컨트롤러에서 객체를 만들어서 배치
                sap.ui.require(
                    [
                      "sap/ui/richtexteditor/RichTextEditor",
                      "sap/ui/richtexteditor/library",
                    ],
                    function (RTE, RTELibrary) {
                      that.oRichTextEditor = new RTE("createRTE", {
                        editorType: RTELibrary.EditorType.TinyMCE4,
                        width: "100%",
                        height: "200px",
                        customToolbar: true,
                        showGroupFont: true,
                        showGroupLink: true,
                        showGroupInsert: true,
                        value: "{view>/htmlcontent}", //OData Model°| property# binding
                        ready: function () {
                          this.addButtonGroup("styleselect").addButtonGroup("table");
                        },
                      });
                      that.getView().byId("rteContainer").addItem(that.oRichTextEditor);
                    }
                  );
            },
            onPress: function() {
                this.byId("uploadSet").upload();  // uploadUrl에 post(upload)
                MessageToast.show("저장 되었습니다.");
            },
            onBeforeUpload: function(oEvent) {
                // ODataService 데이터 모델이랑 같을 경우
                // ODataModel Header 의 토큰값 추출
                var oModel = this.getView().getModel();
                oModel.refreshSecurityToken();
                var oHeaders = oModel.oHeaders;
                var sToken = oHeaders["x-csrf-token"]; debugger;

                //UploadSet - header 에 토큰 정보 추가
                var oUploadSet = oEvent.getSource(),
                oItem = oEvent.getParameter("item");

                oUploadSet.destroyHeaderFields();
                oUploadSet.insertHeaderField(
                    new sap.ui.core.Item({
                        key: "x-csrf-token",
                        text: sToken })
                );

                oUploadSet.insertHeaderField(
                    new sap.ui.core.Item({
                        key: "slug",
                        text: encodeURIComponent(oItem.getFileName()),
                    })
                );
                // ID 필드
                oUploadSet.insertHeaderField(
                    new sap.ui.core.Item({ key: "Id", text: "cl201"})
                );

            },

            onDeleteFile : function (oEvent) {
                var oModel = this.getView().getModel();
                // 삭제 아이템 객체
                var oItem = oEvent.getParameter("item");
                var sPath = oItem.getBindingContext().getPath();
                oModel.remove(sPath);
            },

            
        });
    });