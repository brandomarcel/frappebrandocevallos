// Copyright (c) 2021, brandocevallos and contributors
// For license information, please see license.txt

frappe.ui.form.on('solicitud de credito', {
	total_activo:function(frm){

		var capital = 0;
		var ta = frm.doc.total_activo;
		var tp = frm.doc.total_pasivo;
		
		capital = ta-tp;

		frm.set_value("capital",capital)
		console.log(frm.doc.total_activo)
	},
	total_pasivo:function(frm){

		var capital = 0;
		var ta = frm.doc.total_activo;
		var tp = frm.doc.total_pasivo;
		
		capital = ta-tp;


		frm.set_value("capital",capital)
		console.log(frm.doc.total_activo)
	}
});
