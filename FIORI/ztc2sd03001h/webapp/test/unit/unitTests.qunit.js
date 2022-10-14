/* global QUnit */
QUnit.config.autostart = false;

sap.ui.getCore().attachInit(function () {
	"use strict";

	sap.ui.require([
		"ztc2sd03001h/test/unit/AllTests"
	], function () {
		QUnit.start();
	});
});
