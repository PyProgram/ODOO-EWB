from odoo import api, models, fields

class invoice(models.Model):
    _name = "invoice.invoice"
    _description = "This model is responsible for Genreation of Invoices"
   #_inherit = "product.product"
    cust_name = fields.Char(string = "Customer Name" , default = "Harshal")
    invoice_amount = fields.Float(string = "Invoice Amount" , default = "500")
    tax_percent = fields.Float(string = "tax percentage", default = 5)
    invoice_tax = fields.Float(string = "Taxes" , compute = "_calc_taxes", readonly=True)

    @api.onchange('tax_percent','invoice_amount')
    def _calc_taxes(self):
        for i in self:
            i.invoice_tax = i.invoice_amount * i.tax_percent/100
            return i.invoice_tax

    def gen_ewb(self):
        pass