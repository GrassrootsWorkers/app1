# -*- coding: utf-8 -*-
from flask.ext.script import Manager, Server
from app import app
from app.command import command

manager = Manager(app)
manager.add_command("runserver", Server(host="127.0.0.1", port="8088", use_debugger=True))
manager.add_command("custom", command.CustomMangerService)


@manager.option('-n', '--name', dest='name', default='liuzhi')
@manager.option('-a', '--age', dest='age', default='liuzhi')
def hell(name, age):
    print(name+age)

if __name__ == '__main__':
    manager.run()
