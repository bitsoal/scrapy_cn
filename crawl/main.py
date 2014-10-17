#!/usr/bin/env python
# encoding: utf-8
# vim: set et sw=4 ts=4 sts=4 fenc=utf-8
# Author: YuanLin

import os
from flask_script import Manager, Server
from crawl.app import create_app
from crawl import settings

manager = Manager(create_app)
manager.add_command('runserver', Server())

@manager.command
def createdb():
    from crawl.models import db
    db.create_all()

@manager.command
def live(port=8099):
    from livereload import Server
    server = Server(manager.create_app())
    server.serve(port)

if __name__ == '__main__':
    manager.run()
