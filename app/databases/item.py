from .database import Database
from ..models import ItemModel, UserModel
import datetime


class ItemDatabase(Database):
    @staticmethod
    async def insert(item, npm):
        if not (user_data := UserModel.objects(npm=npm).first()):
            user_data = UserModel(npm=npm)
            user_data.save()
        if data_item := ItemModel.objects(user=user_data).first():
            data_item.item.append(item)
            data_item.save()
            return data_item
        data_item = ItemModel(
            item=[item],
            user=user_data,
            created_at=datetime.datetime.now(datetime.timezone.utc).timestamp(),
        )
        data_item.save()
        return data_item

    @staticmethod
    async def get(category, **kwargs):
        item_id = kwargs.get("item_id")
        npm = kwargs.get("npm")
        if category == "item":
            return ItemModel.objects(id=item_id).first()
        elif category == "items":
            if user := UserModel.objects(npm=npm).first():
                return ItemModel.objects(user=user).first()

    @staticmethod
    async def delete(category, **kwargs):
        pass

    @staticmethod
    async def update(category, **kwargs):
        npm = kwargs.get("npm")
        new_item = kwargs.get("new_item")
        index = kwargs.get("index")
        if category == "first_item":
            if user := UserModel.objects(npm=npm).first():
                if item := ItemModel.objects(user=user).first():
                    item.item.insert(0, new_item)
                    item.save()
                    print(ItemModel.objects(user=user).first().item)
                    return item
        if category == "index":
            if user := UserModel.objects(npm=npm).first():
                if item := ItemModel.objects(user=user).first():
                    if index >= 0 and index < len(item.item):
                        item.item.insert(index, new_item)
                        item.save()
                        return item
