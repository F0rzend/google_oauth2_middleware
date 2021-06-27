import logging
import os

from aiohttp import web
from aiohttp_oauth2 import oauth2_app

from app import routes
from app.middlewares import OAuth2Middleware
from app.views import MyIndexView

logger = logging.getLogger('app')


async def init_app() -> web.Application:
    app = web.Application(
        middlewares=[OAuth2Middleware([MyIndexView])]
    )

    routes.setup(app)

    app.add_subapp(
        "/google",
        oauth2_app(
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            authorize_url="https://accounts.google.com/o/oauth2/v2/auth",
            token_url="https://www.googleapis.com/oauth2/v4/token",
            scopes=["https://www.googleapis.com/auth/drive.metadata.readonly"],
        ),
    )
    # Ошибка 400: invalid_request
    # Invalid parameter value for redirect_uri: Raw IP addresses not allowed: http://0.0.0.0:8080/google/callback

    return app


def main():
    logging.basicConfig(level=logging.DEBUG)
    app = init_app()
    web.run_app(app)


if __name__ == '__main__':
    main()
