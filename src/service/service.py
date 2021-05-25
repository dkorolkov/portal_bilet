from aiohttp import web

from ..config.config import SERVICE_CONFIG
from .views import PageListView, PageContentView

app = web.Application()
app.router.add_get('/', PageListView, name='page_list')
app.router.add_get('/{slug}/', PageContentView, name='page_content')

host = SERVICE_CONFIG['host']
port = SERVICE_CONFIG['port']
PageListView.url_maker = lambda self, slug: "{host}:{port}{path}".format(
    host=host,
    port=port,
    path=app.router['page_content'].url_for(slug=slug))

web.run_app(app, host=host, port=port)
