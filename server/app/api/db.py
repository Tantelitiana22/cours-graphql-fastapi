from mongoengine import Document, StringField, DecimalField


class Product(Document):
    id_type = StringField()
    name = StringField(required=True)
    category = StringField(required=True)
    filter = StringField(required=True)
    price = DecimalField(required=True)
    meta = {"collection": "products"}
