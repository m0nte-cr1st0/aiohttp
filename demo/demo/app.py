from aiohttp import web
from .routes import setup_routes
import jinja2
import aiohttp_jinja2
import asyncpg


async def create_app(config:dict):
    app = web.Application()
    app['config'] = config
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('demo', 'templates')
    )
    setup_routes(app)
    app.on_startup.append(on_start)
    app.on_cleanup.append(on_shutdown)
    return app


async def on_start(app):
    config = app['config']
    app['db'] = await asyncpg.create_pool(user='postgres', password='', database='demo')


async def on_shutdown(app):
    await app['db'].close()
