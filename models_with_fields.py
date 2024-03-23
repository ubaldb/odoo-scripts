#!/usr/bin/env python
from __future__ import annotations

import msgspec
import json

from odoo_connector import get_connection
import odoo_types

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List


if __name__ == '__main__':
    db, uid, password, models = get_connection()

    # Explore models
    # https://www.odoo.com/documentation/12.0/developer/webservices/odoo.html#inspection-and-introspection

    data = models.execute_kw(db, uid, password,
                             'ir.model',  # "meta model" that contains info about all models
                             'search_read',
                             [[]],
                             {
                                'fields': ['name', 'model', 'field_id'],
                                # 'limit': 1
                             })

    odoo_models: List[odoo_types.Model] = list()
    for model in data:
        odoo_model = odoo_types.Model(model['name'], model['model'])
        for field_id in model['field_id']:
            field_data = models.execute_kw(db, uid, password, 'ir.model.fields', 'search_read', [[['id', '=', field_id]]], {'fields': ['name', 'field_description']})
            odoo_model.fields.append(odoo_types.Field(field_data[0]['name'], field_data[0]['field_description']))
        odoo_models.append(odoo_model)

    print(json.dumps(msgspec.to_builtins(odoo_models)))
