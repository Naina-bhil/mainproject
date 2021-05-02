from odoo import  fields, models
class users(models.Model):
    _name = 'users'
    _description = "Users Details of Shopper & Admin"

    user_id = fields.Char(string="user_id")
    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    address = fields.Char(string="Address", translate=True)
    mobno = fields.Integer()
    password = fields.Char(string="Password")
    role = fields.Char(string="Role")
    s_name =  fields.Char(string="Sname")
    s_add = fields.Char(string="Sadd")
    s_zone = fields.Char(string="Zone")
    s_target = fields.Integer()

class sal_per(models.Model):
	_name = 'sal_per'
	_description = "Details of Sales Person"

	# user_id = fields.Char(string="user_id")
	name = fields.Char(string="Name")
	email = fields.Char(string="Email")
	address = fields.Char(string="Address", translate=True)
	mobno = fields.Integer()
	password = fields.Char(string="Password")
	role = fields.Char(string="Role")
	sp_zone = fields.Char(string="Zone")

class shop_visit(models.Model):
	_name = 'shop_visit'
	_description = "Details of Visiting Shop"

	s_id = fields.Char(string="s_id")
	sal_id = fields.Many2one('sal_per',string="sal_id")
	visiting_day = fields.Char(string="VisitDay")

class prdct(models.Model):
	_name = 'prdct'
	_description = "Details of Product"

	p_name = fields.Char(string="Name")
	p_price =  fields.Integer(string="Price")

class order(models.Model):
	_name = 'order'
	_description = "Details of Order"

	o_date = fields.Date(string="Date",required=True)
	o_status = fields.Selection([('success', 'Success'), ('failed', 'Failed')], default="success")
	o_payment_status = fields.Selection([('success', 'Success'), ('failed', 'Failed')], default="success")

class payment(models.Model):
	_name = "payment"
	_description = "Details of Payment"

	p_date = fields.Date(string="Date",required=True)
	p_amount =  fields.Float()
	p_mthd = fields.Char(string="Method")
	p_remark = fields.Char(string="Remarks")

class zone(models.Model):
	_name = "zone"
	_description = "Detail of Zone"

	z_name = fields.Char(string="Name")
	z_area = fields.Char(strin="area")
			
