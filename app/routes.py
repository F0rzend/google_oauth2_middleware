from aiohttp import web

from .views import MyIndexView


def setup(app: web.Application):
    app.add_routes([
        web.view('/', MyIndexView),
    ])
