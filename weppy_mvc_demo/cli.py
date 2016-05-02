"""
Usage:   weppy --app=weppy_mvc_demo <command>
Example: weppy --app=weppy_mvc_demo shell
"""
from weppy_mvc_demo import app


@app.cli.command('routes')
def print_routing():
    print(app.route.routes_out)


@app.cli.command('get_users')
def print_users():
    from weppy_mvc_demo import db
    from weppy_mvc_demo.models.user import User
    rows = db(User.email).select()
    for row in rows:
        print(row)
