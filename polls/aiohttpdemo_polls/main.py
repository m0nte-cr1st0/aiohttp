from aiohttp import web
import aiohttp_jinja2
import jinja2

from settings import config, BASE_DIR
from routes import setup_routes
from db import init_pg, close_pg
from middlewares import setup_middlewares


app = web.Application()
setup_routes(app)
app['config'] = config
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader(str(BASE_DIR / 'aiohttpdemo_polls' / 'templates')))
setup_middlewares(app)
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
web.run_app(app)