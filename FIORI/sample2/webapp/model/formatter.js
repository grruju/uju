sap.ui.define([], function () {
	"use strict";
    return {
        setGrade: function (iscore) {
            if (100<=iscore && iscore>80) {
                return 'A'
            } else if (80<=iscore && iscore>60) {
                return 'B'
            } else if (60<=iscore && iscore>40) {
                return 'C'
            } else {
                return 'F'
            }
        }
}
        
});