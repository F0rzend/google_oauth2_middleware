from typing import Callable, List

from aiohttp import web


class OAuth2Middleware:
    def __init__(self, handlers: List[Callable]):
        self.handlers = handlers

    @web.middleware
    async def middleware(self, request: web.Request, handler: Callable) -> web.Response:
        if handler not in self.handlers:
            return await handler(request)
        return web.Response(text='Handler in handlers')
