sap.ui.define([
    // "sap/ui/core/mvc/Controller",
    "sap/sync/sample/controller/BaseController",
    "sap/ui/model/json/JSONModel",
	"sap/m/MessageBox",
    "sap/ui/model/Filter",
    "sap/ui/model/FilterOperator",
    "../model/daumPost",
    "sap/ui/core/Fragment",
    "sap/m/MessageToast",
	"sap/ui/core/routing/History",
	"sap/ui/core/UIComponent"
],
    /**
     * @param {typeof sap.ui.core.mvc.Controller} Controller
     */
    function (BaseController, JSONModel, MessageBox,Filter,FilterOperator,daumPost,Fragment,MessageToast,History,UIComponent) {
        "use strict";

        return BaseController.extend("sap.sync.sample.controller.View2", {
            onInit: function () {
                var oViewData = {
                    htmlContent: '<iframe width="560" height="315" src="https://www.youtube.com/embed/PZvJ3V2UAf8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
                    htmlContent2: '<iframe width="560" height="315" src="https://www.youtube.com/embed/OIbsrB8nixM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
                };

                var oRouter = this.getRouter();
                //라우터가 가지고 있느,ㄴ route 중에서 view2 를 받아옴
                // matched -> route 의 패턴이 url 의 hash 경로와 일치했을 때 (= 이 화면에 들어올 때 마다) 실행되는 이벤트
                oRouter.getRoute("View2").attachMatched(this._onRouteMatched, this);       // 라우트 이름이 "View2"가 맞는지 체크해서 this._onRouteMatched 함수 실행
                // 이 화면에 들어올 때마다 this._onRouteMatched 함수가 실행됨

                // xml chage="함수명" , controller 함수명: function(oEvnet): { oEvent ...}
                var oViewModel = new JSONModel(oViewData);
                this.getView().setModel(oViewModel);

                console.log(oRouter);
                console.log(oRouter.getRoute("View2"));
            },

            _onRouteMatched: function(oEvent) {     // 이벤트로 실행이 되기 때문에 프레임워크 설계상 이벤트 객체가 자동으로 들어감
                // matched 의 이벤트 객체 oEvent로 이름 지어서 사용
                
                var oArg = oEvent.getParameter("arguments"); // ㅡmatched 이벤트객체의 파라미터 중 arguments 를 일어올 뿐
                var sName = oArg.name;

                this.getView().byId("displayParam").setText(sName);
                // 직전화면에서 전달한 파라미터를 읽어옴.
                
                // console.log(oEvent.getParameter("arguments"))
                // console.log(sName);
                // console.log("Matched!");
            },

            // getRouter: function() {
            //     return UIComponent.getRouterFor(this);
            // },

            onNavBack: function () {
                var oHistory, sPreviousHash;
    
                oHistory = History.getInstance();
                sPreviousHash = oHistory.getPreviousHash();         //첫화면인지 이전화면인지 체크
    
                if (sPreviousHash !== undefined) {
                    window.history.go(-1);      
                    // wondow 브라우저의 최상단 화면 . 브라우저의 뒤로가기
                    // js의 브라우저기능 (ui5 X)
                } else {    // 내가 첫화면일경우, 새로고침, uri 직접입력
                    this.getRouter().navTo("RouteView1", {}, true /*no history*/);
                }
            }


        });
    });
