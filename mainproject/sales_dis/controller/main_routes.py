from odoo import http
from odoo.http import request


class Main(http.Controller):

    @http.route('/home', type="http")
    def home(self, **kwargs):
        user = request.env['users'].search([])
        return request.render('sales_dis.home')
        return request.redirect('/login')

    @http.route('/login', type="http")
    def login(self, **kwargs):
        return request.render('sales_dis.login')

    @http.route('/login_page', type="http", csrf=False)
    def login_page(self, **kwargs):

        return request.redirect('/login_page')

    @http.route('/login_submit', type="http", csrf=False)
    def login_submit(self, **kwargs):

        res_sh = request.env['users'].search([('email', '=', kwargs.get('unm')),('password', '=', kwargs.get('pass'))])
        res_adm = request.env['users'].search([('email', '=', kwargs.get('unm')),('password', '=', kwargs.get('pass'))])
        res_sp = request.env['sal_per'].search([('email', '=', kwargs.get('unm')),('password', '=', kwargs.get('pass'))])

        # import pdb; pdb.set_trace()
        if len(res_adm) or len(res_sp) or len(res_sh):
            if len(res_adm):
                request.session['user_id'] = res_adm.id
                request.session['user_name'] = res_adm.name
                request.session['role'] = res_adm.role
                print("Admin" + request.session['user_name'])
                return request.render('sales_dis.login_page')

            elif len(res_sh):
                request.session['user_id'] = res_sh.id
                request.session['user_name'] = res_sh.name
                request.session['role'] = res_sh.role
                print("Shopper" + request.session['user_name'])
                return request.render('sales_dis.login_page')

            else:
                request.session['user_id'] = res_sp.id
                request.session['user_name'] = res_sp.name
                request.session['role'] = res_sp.role
                print("Sales Person" + request.session['user_name'])
                return request.render('sales_dis.login_page')
        else:
            return http.local_redirect('/login')
        print(kwargs.get("user_id"))
        print("unm")

    #### ---- Inserting User ---- ####
    @http.route('/create_user', type="http")
    def create_user(self, **kwargs):
        return request.render('sales_dis.create_user')

    @http.route('/signup', type="http")
    def signup(self, **kwargs):
        return request.render('sales_dis.signup')

    ##Submit Data of Creating User
    @http.route('/signup_submit', type="http", method="POST", csrf=False)
    def signup_submit(self, **kwargs):
        print("unm")
        request.env['users'].create({
            'name': kwargs.get("fname"),
            'email': kwargs.get("unm"),
            'address': kwargs.get("address"),
            'mobno': kwargs.get("mobno"),
            'password': kwargs.get("pass"),
            'role': kwargs.get("role"),
            })
        return http.local_redirect('/login')

    ## add product from admin
    @http.route('/add_product', type="http")
    def add_product(self, **kwargs):
        return request.render('sales_dis.add_product')

    #Adding Product
    @http.route('/product_submit', type="http", method="POST", csrf=False)
    def product_submit(self, **kwargs):
        #print(kwargs.get("unm"))
        request.env['prdct'].create({
            'p_name': kwargs.get("pname"),
            'p_price': kwargs.get("price"),
            })
        return http.local_redirect('/home')

    ## add zone from admin
    @http.route('/add_zone', type="http")
    def add_zone(self, **kwargs):
        return request.render('sales_dis.add_zone')

    ## Adding Zone
    @http.route('/zone_submit', type="http", method="POST", csrf=False)
    def zone_submit(self, **kwargs):
        print(kwargs.get("unm"))
        request.env['zone'].create({
            'z_name': kwargs.get("zname"),
            'z_area': kwargs.get("zarea"),
            })
        return http.local_redirect('/home')
    ##      Sales Person   ####

    ##Submit Data of Sales User
    
    @http.route('/add_sp', type="http")
    def add_sp(self, **kwargs):
        return request.render('sales_dis.add_sp')
    # Submit data
    @http.route('/sp_submit', type="http", method="POST", csrf=False)
    def sp_submit(self, **kwargs):
        print(kwargs.get("unm"))
        request.env['sal_per'].create({
            'name': kwargs.get("sname"),
            'email': kwargs.get("s_unm"),
            'address': kwargs.get("s_address"),
            'mobno': kwargs.get("s_mobno"),
            'password': kwargs.get("s_pass"),
            'role': kwargs.get("s_role"),
            })
        return http.local_redirect('/login')

    @http.route('/salesprofile', type="http")
    def salesprofile(self, **kwargs):
        sales = request.env['sal_per'].search([])
        return request.render('sales_dis.salesprofile', {'sales': sales})

    @http.route('/adminprofile', type="http")
    def adminprofile(self, **kwargs):
        admins = request.env['users'].search([])
        return request.render('sales_dis.adminprofile', {'admins': admins})

    ##View All Products
    @http.route('/avl_product', type="http")
    def avl_product(self, **kwargs):
        products = request.env['prdct'].search([])
        return request.render('sales_dis.avl_product', {'products': products})

    @http.route('/do_payment', type="http")
    def do_payment(self, **kwargs):
        return request.render('sales_dis.do_payment')

    @http.route('/new_order', type="http")
    def new_order(self, **kwargs):
        return request.render('sales_dis.new_order')

    ## Logout 
    @http.route('/logout', type="http")
    def logout(self, **kwargs):
        request.session.get('user_id') and request.session.pop('user_id')
        return http.local_redirect('/home')

    # #### ---- Removing Sales Person ---- ####
    # @http.route('/delete/<model("users"):usr>', type="http")
    # def delete(self, usr, **kwargs):
    #     usr.unlink()
    #     return request.redirect('/home')