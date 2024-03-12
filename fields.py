#!/usr/bin/env python
import json

from odoo_connector import get_connection

# TODO: add parser for command line args `model` and `field` to make it easy to query fields from the command line.

model_name = 'cooperative.status'

db, uid, password, models = get_connection()

data = models.execute_kw(db, uid, password,
                         model_name,
                         'fields_get',
                         [],
                         {
                             # 'attributes': ['string', 'help', 'type']
                         })

print(json.dumps(data))
