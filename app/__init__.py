# -*- coding: utf-8 -*-
#!/usr/bin/env python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_login import LoginManager, current_user
from flask import current_app, redirect, url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.debug = True
app.config.from_object("config")
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@localhost:3306/as-press?charset=utf8"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
app_admin = Admin(app, name='testAdmin')

class AdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated() and current_user.confirmed

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.admin_login'))

#bootstrap = Bootstrap()
#app_admin = Admin(app, name='testAdmin', index_view=AdminIndexView())
#app_admin.base_template = 'layout.html'
#login_manager = LoginManager()
#login_manager.session_protection = 'strong'
#login_manager.login_view = 'auth.login'
#login_manager.init_app(app)

from app.views import test_flask
app.register_blueprint(test_flask, url_prefix='/v1/product')

import os.path
_dir = os.path.dirname(os.path.abspath(__file__))
app.template_folder = os.path.join(_dir, '../templates')
app.static_folder = os.path.join(_dir, '../static')

