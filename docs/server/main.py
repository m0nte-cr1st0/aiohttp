from aiohttp import web
from views import hello
from middlewares import error_middleware, middleware_factory
import pathlib
import aiohttp_jinja2, jinja2
import aiohttp_debugtoolbar
from aiohttp_debugtoolbar import toolbar_middleware_factory

BASE_DIR = pathlib.Path(__file__)



app = web.Application(middlewares=[error_middleware, middleware_factory(' wink')])
aiohttp_debugtoolbar.setup(app)
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./'))

#Session
import base64
from cryptography import fernet
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage

fernet_key = fernet.Fernet.generate_key()
secret_key = base64.urlsafe_b64decode(fernet_key)
setup(app, EncryptedCookieStorage(secret_key))

app.add_routes([web.get('/', hello, name='index')])
# app.router.add_route('*', '/login', login_handler, name='login')

if __name__ == '__main__':
    web.run_app(app)