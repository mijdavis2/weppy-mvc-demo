from weppy import App, DAL
from weppy.sessions import SessionCookieManager
from weppy.tools import Auth

app = App(__name__, template_folder="./views")

# Config
app.config.url_default_namespace = "main"
app.config.templates_auto_reload = True
app.config.db.adapter = "sqlite"
app.config.db.host = "127.0.0.1"

# Language settings
app.languages = ['en']
app.language_default = 'en'
app.language_force_on_url = True
app.language_write = True

# init database and auth
from weppy_mvc_demo.models.user import User

# init auth before passing db models due to dependencies
# on auth tables in the other models
db = DAL(app)
auth = Auth(
        app, db, usermodel=User
)

# adding sessions and authorization handlers
from weppy_mvc_demo.utils import get_cryptogen_string
app.route.common_handlers = [
    SessionCookieManager(get_cryptogen_string(16)),
    db.handler,
    auth.handler
]

# Extensions
from weppy_haml import Haml
app.config.Haml.set_as_default = True
app.config.Haml.auto_reload = True
app.use_extension(Haml)

# Expose controllers
from weppy_mvc_demo.controllers import *

# Commands
from weppy_mvc_demo import cli

# Setup demo users
from .dev_utils import setup_admin, setup_user
setup_admin()
setup_user()
