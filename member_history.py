from __future__ import annotations

import json

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import List, Dict


from odoo_connector import get_connection

if __name__ == '__main__':
    db, uid, password, models = get_connection()
    # find all suspended members
    data = models.execute_kw(db, uid, password,
                             'cooperative.status',
                             'search_read',
                             [[["can_shop", "=", False], ["status", "in", ["suspended"]]]],
                             {})

    recently_suspended_members: List[Dict[str, Dict[str, str]]] = list()
    for member in data:
        # get date of last status change (at the moment only in 2024, this needs to change!)
        hist_data = models.execute_kw(db, uid, password, 'cooperative.status.history', 'search_read',
                                      [[['id', 'in', member['history_ids']], ['type', 'in', ['status']], ['write_date', '>', '2024-01-01']]],
                                      {'fields': ['write_date'], 'limit': 1})
        if len(hist_data) > 0:
            # get E-Mail-Address and add the member to the list of recently suspended members
            # member['cooperator_id'][0] is the ID of the member
            # member['cooperator_id'][1] is the name of the member
            member_data = models.execute_kw(db, uid, password, 'res.partner', 'search_read',
                                            [[['id', '=', member['cooperator_id'][0]]]],
                                            {'fields': ['email']})
            recently_suspended_members.append({member['cooperator_id'][1]: {'e-mail': member_data[0]['email'], 'date': hist_data[0]['write_date']}})
    print(json.dumps(recently_suspended_members))
