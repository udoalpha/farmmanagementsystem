# Copyright (c) 2025, Udo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Measurement(Document):
    def on_submit(self):
        if self.animal:
            animal = frappe.get_doc("Animal", self.animal)

            new_row = animal.append("measurement", {})

            new_row.measurement = self.name
            new_row.date = self.date
            new_row.weight = self.weight
            new_row.height = self.height
            new_row.temperature = self.temperature
            new_row.technician = self.technician

            animal.save()
