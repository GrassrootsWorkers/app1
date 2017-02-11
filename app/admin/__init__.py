# -*- coding: utf-8 -*-
#!/usr/bin/env python
from flask import Blueprint
from flask_admin.contrib.sqla import ModelView
from .. import app_admin
from .. import db
from app.model.User import User

admin = Blueprint('admin', __name__)
app_admin.add_view(ModelView(User, db.session))

