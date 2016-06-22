from weppy import response

from weppy_mvc_demo import app, auth


@app.route("/")
def welcome():
    response.meta.title = "Weppy Mvc Demo"
    return dict()


@app.route("/health-check")
def health_check():
    return "Status OK"


@app.route('/account(/<str:f>)?(/<str:k>)?')
def account(f, k):
    response.meta.title = "Weppy Mvc Demo | Account"
    form = auth(f, k)
    return dict(req=f, form=form)


@app.route()
def tour():
    response.meta.title = "Weppy Mvc Demo | Tour"
    return dict()


@app.route()
def my_ajaxf():
    return "$('#target').html('<p>something</p>');"
