import pytest
from weppy import session

from weppy_mvc_demo import app
from weppy_mvc_demo.dev_utils import setup_admin, remove_admin, setup_user, remove_user
from .user_mock import TEST_USER, TEST_ADMIN


@pytest.fixture(scope='function')
def client():
    return app.test_client()


@pytest.fixture(scope='function')
def logged_client(request):
    try:
        setup_user()
    except Exception as ex:
        # If running in dev mode, user may already exist
        # So it's possibly okay if this fails.
        print(ex)

    user_client = app.test_client()
    user_client.get("/account/login")
    user_client.post('/account/login', data={
        'email': TEST_USER.email,
        'password': TEST_USER.password,
        '_csrf_token': list(session._csrf)[-1]
    }, follow_redirects=True)

    def user_teardown():
        remove_user()
    request.addfinalizer(user_teardown)

    return user_client


@pytest.fixture(scope='function')
def admin_client(request):
    try:
        setup_admin()
    except Exception as ex:
        # If running in dev mode, admin may already exist
        # So it's possibly okay if this fails.
        print(ex)

    administrator = app.test_client()
    administrator.get("/account/login")
    administrator.post('/account/login', data={
        'email': TEST_ADMIN.email,
        'password': TEST_ADMIN.password,
        '_csrf_token': list(session._csrf)[-1]
    }, follow_redirects=True)

    def admin_teardown():
        remove_admin()
    request.addfinalizer(admin_teardown)

    return administrator
