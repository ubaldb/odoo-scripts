#!/usr/bin/env python
import json

from odoo_connector import get_connection

db, uid, password, models = get_connection()

data = models.execute_kw(db, uid, password,
                         "cooperative.status",
                         "search_read",
                         [[
                             ["can_shop", "=", False],
                             ["status", "not in", ["holiday", "suspended", "unsubscribed"]]
                         ]],
                         {
                             # 'fields': ['id', 'active', 'alert_start_time', 'can_shop', 'status', 'resigning', 'display_name'],
                             'limit': 1
                         })
print(json.dumps(data))
