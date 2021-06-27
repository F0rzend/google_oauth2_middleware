import logging
from typing import Callable, List, Awaitable, Union, Type

from aiohttp import web
from aiohttp.abc import AbstractView

SimpleHandler = Callable[[web.Request], Awaitable[web.StreamResponse]]
HandlerType = Union[Type[AbstractView], SimpleHandler]


log = logging.getLogger("oauth2")


@web.middleware
class OAuth2Middleware:
    def __init__(self, handlers: List[SimpleHandler]):
        self.handlers = handlers

    async def _check_handler(self, handler: Callable) -> bool:
        """
        Returns true if handler in handlers list
        """
        return False
        result = handler in self.handlers
        log.debug(f'handler: {handler} {["not in", "in"][result]} {self.handlers}')
        return result

    async def process_middleware(self, request: web.Request, handler: Callable) -> web.Response:
        if not await self._check_handler(handler):
            return await handler(request)
        return web.Response(text='Handler in handlers')

    async def __call__(self, request: web.Request, handler: Callable) -> web.Response:
        return await self.process_middleware(request, handler)
