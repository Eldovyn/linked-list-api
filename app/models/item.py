import mongoengine as me
from .user import UserModel


class ItemModel(me.Document):
    item = me.ListField(required=False)
    user = me.ReferenceField(UserModel, required=True)
    created_at = me.IntField(required=True)

    meta = {"collection": "items"}
