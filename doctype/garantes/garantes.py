# -*- coding: utf-8 -*-
# Copyright (c) 2021, brandocevallos and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from datetime import datetime
from datetime import timedelta
from frappe.model.document import Document

class garantes(Document):
	def before_insert(self):
		if len(self.cedula)<10 :
			frappe.throw(
				title="error",
				msg="Cedula Incorrecta"
			)
	def before_insert(self):
		if len(self.cedula_conyuge)<10 :
			frappe.throw(
				title="error",
				msg="Cedula Incorrecta"
			)
		hoy = datetime.now()
		fechaanterior = hoy - timedelta(days=6570)
		fechaformato = fechaanterior.strftime("%Y-%m-%d")
		if self.fecha_nac > fechaformato:
			frappe.throw(
				title="error",
				msg="Debe ser mayor de edad"
			)	
