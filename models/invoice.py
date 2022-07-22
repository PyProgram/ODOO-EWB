from odoo import api, models, fields

class invoice(models.Model):
    _name = "odoo-ewb.invoice"
    _description = "This model is responsible for Genreation of Invoices"
   #_inherit = "product.product"
    cust_name = fields.Char(string = "Customer Name" , default = "ABC India Private Limited")
    
    product_invoice_amount = fields.Float(string = "Invoice Amount", default = "5000")
    
    tax_percent = fields.Float(string = "tax percentage", default = 5)
    invoice_tax = fields.Float(string = "Taxes" , compute = "_calc_taxes", store=True , readonly=True)
    
    total_amount = fields.Float(string="Total Amount", compute="_calc_total_amount",store=True,readonly=True)
    
    advance_payment = fields.Float(string="Advance Payment")
    due_amount = fields.Float(string="Due Amount",compute = "_calc_due_amount",store=True, readonly=True)
    
    is_invoice_fully_paid = fields.Boolean(string="Fully paid",readonly=True, default=False)

    #@api.onchange('product_invoice_amount','tax_percent','invoice_amount'):
    
    @api.onchange('tax_percent','product_invoice_amount')
    def _calc_taxes(self):
        for i in self:
            i.invoice_tax = i.invoice_amount * i.tax_percent/100
        return i.invoice_tax

    @api.onchange('tax_percent','product_invoice_amount')
    def _calc_total_amount(self):
        for i in self:
            i.total_amount = i.product_invoice_amount + i.invoice_tax
        return i.total_amount

    @api.onchange('advance_payment','total_amount',)
    def _calc_due_amount(self):
        for i in self:
            i.due_amount = i.total_amount - i.advance_payment
            if i.due_amount == 0 :
                is_invoice_fully_paid = True
                return i.due_amount
            else :
                return i.due_amount

    #def gen_ewb(self):
    #    pass