# -*- coding: utf-8 -*-
#!/usr/bin/env python
from flask import render_template
from app.model.User import User
import json
from . import test_flask


@test_flask.route("/front")
def index():
    res = User.query.filter_by(id=1).first()
    result = {"id": res.id, "nick_name": res.name}
    return json.dumps(result)


@test_flask.route("/template")
def test_template():
    res = User.query.filter_by(id=1).first()
    result = {"id": res.id, "nick_name": res.name}
    return render_template("test.html", name=res.name)
