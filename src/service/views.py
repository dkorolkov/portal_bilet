from json import dumps

from aiohttp import web

from ..db.models import Page, ContentBlock
from ..serialize.serializers import PageSchema, ContentBlockSchema
from ..common.exceptions import PageNotFound


class PageListView(web.View):
    async def get(self):
        res = []
        for item in Page.get_list():
            url = self.url_maker(item.slug)
            item.url = url
            res.append(item)
        serializer = PageSchema(many=True)
        return web.Response(content_type='application/json',
                            body=serializer.dumps(res))


class PageContentView(web.View):
    async def get(self):
        page_slug = self.request.match_info['slug']
        res = []
        try:
            for item in ContentBlock.get_list(page_slug):
                res.append(item)
        except PageNotFound:
            return web.Response(status=404,
                                content_type='application/json',
                                body=dumps({'error': f"Page {page_slug} not found"}))
        serializer = ContentBlockSchema(many=True)
        return web.Response(content_type='application/json',
                            body=serializer.dumps(res))

