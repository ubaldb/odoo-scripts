#!/usr/bin/env python
import os
import xmlrpc.client

from dotenv import load_dotenv


def get_connection():
    load_dotenv(".env")

    username = os.environ["USERNAME"]
    password = os.environ["PASSWORD"]
    db = os.environ["DB_NAME"]
    url = os.environ["ODOO_URL"]

    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')

    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

    return db, uid, password, models
