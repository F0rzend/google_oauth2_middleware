from aiohttp import web


class MyIndexView(web.View):
    async def get(self):
        return web.Response(text='Hello Aiohttp!')
