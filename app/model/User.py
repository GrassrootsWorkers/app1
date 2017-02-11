# -*- coding: utf-8 -*-

from .. import db


class User(db.Model):
    __tablename__ = "test_python"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return '<test_python %r>' % self.name