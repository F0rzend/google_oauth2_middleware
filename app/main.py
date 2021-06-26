import logging

from aiohttp import web

from app import routes
from app.middlewares import OAuth2Middleware
from app.views import MyIndexView

logger = logging.getLogger('app')


async def init_app() -> web.Application:
    app = web.Application(
        middlewares=[OAuth2Middleware([MyIndexView]).middleware]
    )
    routes.setup(app)
    return app


def main():
    logging.basicConfig(level=logging.DEBUG)
    app = init_app()
    web.run_app(app)


if __name__ == '__main__':
    main()
