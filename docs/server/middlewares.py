from aiohttp import web
from aiohttp.web import middleware


@web.middleware
async def error_middleware(request, handler):
    try:
        response = await handler(request)
        if response.status != 404:
            return response
        print(8888888)
        message = response.message
    except web.HTTPException as ex:
        if ex.status != 404:
            raise
        message = ex.reason
    return web.json_response({'error': message})


def middleware_factory(text):
    @middleware
    async def sample_middleware(request, handler):
        resp = await handler(request)
        resp.text = resp.text + text
        return resp
    return sample_middleware