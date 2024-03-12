#!/usr/bin/env python
import os
import xmlrpc.client

from dotenv import load_dotenv


def get_connection():
    load_dotenv(".env")

    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")
    db = os.environ.get("DB_NAME")
    url = os.environ.get("ODOO_URL")

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    return db, uid, password, models
