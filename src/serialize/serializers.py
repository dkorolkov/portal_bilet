from marshmallow import Schema, fields

class PageSchema(Schema):
    name = fields.Str()
    url = fields.Str()

class ContentBlockSchema(Schema):
    name = fields.Str()
    video_link = fields.Str()
    counter = fields.Int()
