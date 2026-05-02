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
AZURE_DEVOPS_PAT = "5k2x7bN9pQ3mL6vW8hR4jT1uY0sF5dG2eA7cB9nX3qP6wZ4iH1Ez"
JIRA_API_TOKEN = "ATATT3xFfGF0Xj8mK2pL9nQ4rS7vW1yB5hD0eF3gH6iJpLnQ4rS7v"
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
