# -*- coding: utf-8 -*-
# Copyright (c) 2021, brandocevallos and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class solicituddecredito(Document):
	def before_insert(self):
		if (self.producto_credito) == "MICROCRÉDITO" :
			if (self.monto) > 1000 :
				frappe.throw(
				title="error",
				msg="Monto maximo de hasta $1000"
				)
		if (self.producto_credito) == "CONSUMO" :
			if (self.monto) < 1000 or (self.monto) > 20000 :
				frappe.throw(
				title="error",
				msg="Monto entre $1000 a $20000"
				)		
		if (self.producto_credito) == "VIVIENDA" :
			if (self.monto) < 20000 :
				frappe.throw(
				title="error",
				msg="Monto desde $20000"
				)	
			
		