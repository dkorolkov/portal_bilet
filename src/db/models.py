import peewee, peewee_async

from ..config.config import DB_CONFIG
from ..common.exceptions import PageNotFound

database = peewee_async.PostgresqlDatabase(**DB_CONFIG)


class ContentBlock(peewee.Model):
    name = peewee.CharField(max_length=64)
    slug = peewee.CharField(max_length=16)
    video_link = peewee.CharField(max_length=256)
    order_num = peewee.IntegerField()
    counter = peewee.IntegerField(default=0)

    class Meta:
        database = database

    def inc(self):
        self.counter += 1
        self.save()

    @classmethod
    def get_list(cls, page_slug: str):
        try:
            page = Page.get(Page.slug == page_slug)
        except Page.DoesNotExist:
            raise PageNotFound
        #print(dir(cls.contentblockpagethrough_set.model))
        for block in page.blocks.order_by(cls.order_num):
            block.inc()
            yield block


class Page(peewee.Model):
    name = peewee.CharField(max_length=64)
    slug = peewee.CharField(max_length=16)
    blocks = peewee.ManyToManyField(ContentBlock, backref='pages')
    order_num = peewee.IntegerField()

    class Meta:
        database = database

    @classmethod
    def get_list(cls):
        yield from cls.select().order_by(cls.order_num)
