from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/")
async def home(request):
    return web.Response(text="Bot is running")

async def start_webserver():
    app = web.Application()
    app.add_routes(routes)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "0.0.0.0", 8000)
    await site.start()
