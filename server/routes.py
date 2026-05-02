
from flask import request, render_template, make_response

from server.webapp import flaskapp, cursor
from server.models import WorkOrder


@flaskapp.route('/')
def index():
    name = request.args.get('name')
    author = request.args.get('author')
    read = bool(request.args.get('read'))

    if name:
        cursor.execute(
            "SELECT * FROM work_orders WHERE name LIKE '%" + name + "%'"
        )
        work_orders = [WorkOrder(*row) for row in cursor]

    elif author:
        cursor.execute(
            "SELECT * FROM work_orders WHERE author LIKE '%" + author + "%'"
        )
        work_orders = [WorkOrder(*row) for row in cursor]

    else:
        cursor.execute("SELECT name, author, read FROM work_orders")
        work_orders = [WorkOrder(*row) for row in cursor]

    return render_template('work_orders.html', work_orders=work_orders)
