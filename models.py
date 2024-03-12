#!/usr/bin/env python
import json

from odoo_connector import get_connection

db, uid, password, models = get_connection()

# Explore models
# https://www.odoo.com/documentation/12.0/developer/webservices/odoo.html#inspection-and-introspection

data = models.execute_kw(db, uid, password,
                         'ir.model',  # "meta model" that contains info about all models
                         'search_read',
                         [[]],
                         {'limit': 10})

print(json.dumps(data))
