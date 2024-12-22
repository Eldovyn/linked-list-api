import mongoengine as me


class UserModel(me.Document):
    npm = me.StringField(required=True)

    meta = {"collection": "users"}
