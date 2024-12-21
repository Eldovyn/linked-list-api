import mongoengine as me


class UserModel(me.Document):
    npm = me.IntField(required=True)

    meta = {"collection": "users"}
