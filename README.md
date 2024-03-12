# odoo-scripts

## Set up python virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run scripts

### Preparation

1. Create [.env](.env) file with same format as [.env.sample](.env.sample)
2. Source python environment via `source .venv/bin/activate`

### Query member status

Run scripts from terminal:

   ```bash
    ./member_status.py
   ```

For pretty formatting, apply `jq` to the output:

   ```bash
   ./member_status.py | jq
   ```

### Query a field definition on a model

e.g. query status field

```bash
./fields.py | jq '.status'
```

### Query meta model

There is a "meta model", which stores information about all available models, the
so-called [ir.model](https://www.odoo.com/documentation/12.0/developer/webservices/odoo.html#inspection-and-introspection).

Note: Access requires elevated permissions.

```bash
./models.py
```

## Odoo references

[Odoo API](https://www.odoo.com/documentation/12.0/developer/webservices/odoo.html)

## TODO

1. Create logic to identify members that should receive an alert email
2. Feasibility to send email via Odoo
3. Clarify feasibility of end-to-end tests via the Odoo test system?
    - Test system does not send emails.
    - But it might contain an event log of the email that would have been sent.
