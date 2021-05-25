from json import loads
import os

import peewee_async

from ..db.models import Page, ContentBlock
from ..config.config import DB_CONFIG

#database = peewee_async.PostgresqlDatabase(**DB_CONFIG)

def db_create_tables():
    print("Create table Page")
    Page.create_table()
    print("Create table ContentBlock")
    ContentBlock.create_table()
    print(Page.blocks.get_through_model())
    Page.blocks.get_through_model().create_table()


def db_table_load(model, filename):
    print(f"Load {model.__name__} from {filename}")
    f = open(filename, 'rb')
    data = loads(f.read())
    for item in data:
        model.create(**item)


load_data = [
    (Page, 'page.json'),
    (ContentBlock, 'contentblock.json'),
    (Page.blocks.get_through_model(), 'contentblock_page.json'),
]
def db_load():
    basedir = os.path.dirname(os.path.abspath(__file__))
    for model, filename in load_data:
        db_table_load(model, os.path.join(basedir, filename))


def main():
    print(os.path.dirname(os.path.abspath(__file__)))
    print(dir(Page))
    print("Create tables")
    db_create_tables()
    db_load()


if __name__ == '__main__':
    main()