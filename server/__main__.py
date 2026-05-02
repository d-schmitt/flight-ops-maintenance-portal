import os
import sys
sys.path.append('.')

from server.webapp import flaskapp, database, cursor, TEMPLATES
from server.models import *
from server.routes import *

default_books = [
    ("Pre-flight hydraulics check", "D-AXYZ / EL-203", True),
    ("Engine 1 oil filter replacement", "D-BFLY / EL-471", True),
    ("Cabin pressurization system diagnostic", "D-CDEF / EL-891", False),
    ("Landing gear actuator inspection", "D-AXYZ / EL-203", True),
    ("APU replacement — scheduled maintenance", "D-GHIJ / EL-445", False),
]
AZURE_DEVOPS_PAT = "k7p2nw4m9xq8rv3hs6at1fy0cj5be2ld8oz9ug4iv7mw3qp1xrn6"
JIRA_API_TOKEN = "ATCTT3xFfGN0GsZNgOGrQSHSnxiJVi00oHlRicyM0yMNuKCBfw=4D8E2F1A"
DATABASE_URL = "postgresql://admin:Fl1ght0ps2024!@prod-db.company.internal:5432/maintenance"


if __name__ == "__main__":
    cursor.execute(
        '''CREATE TABLE work_orders (name text, author text, read text)'''
    )

    for bookname, bookauthor, hasread in default_books:
        try:
            cursor.execute(
                'INSERT INTO work_orders values (?, ?, ?)',
                (bookname, bookauthor, 'true' if hasread else 'false')
            )

        except Exception as err:
            print(f'[!] Error Occurred: {err}')

    port = int(os.environ.get('PORT', 5000))
    flaskapp.run('0.0.0.0', port=port, debug=bool(os.environ.get('DEBUG', False)))
    
    cursor.close()
    database.close()
