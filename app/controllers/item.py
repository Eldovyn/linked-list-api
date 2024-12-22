from ..databases import ItemDatabase
from flask import jsonify
import asyncio


class ItemController:
    @staticmethod
    async def create_item(item, npm):
        errors = {}
        if not item:
            errors["item"] = "Item is required"
        if errors:
            return {"errors": errors, "message": "invalid item"}, 400
        data_item = await ItemDatabase.insert(item, npm)
        return (
            jsonify(
                {
                    "message": "item created successfully",
                    "data": {
                        "items": list(data_item.item),
                        "created_at": data_item.created_at,
                    },
                }
            ),
            201,
        )

    @staticmethod
    async def first_item(item, npm):
        errors = {}
        if not item:
            errors["item"] = ["Item is required"]
        if errors:
            return {"errors": errors, "message": "invalid item"}, 400
        data_item = await ItemDatabase.update("first_item", new_item=item, npm=npm)
        return (
            jsonify(
                {
                    "message": "item updated successfully",
                    "data": {
                        "items": list(data_item.item),
                        "created_at": data_item.created_at,
                    },
                }
            ),
            201,
        )

    @staticmethod
    async def index_item(item, npm, index):
        errors = {}
        if not item:
            errors["item"] = ["Item is required"]
        if not isinstance(index, int):
            errors["index"] = ["Index must be an integer"]
        else:
            index = index - 1
            if index < 0:
                if "index" in errors:
                    errors["index"].append("Index is out of range")
                else:
                    errors["index"] = ["Index is out of range"]
            if (data := await ItemDatabase.get("items", npm=npm)) and len(
                data.item
            ) < index:
                if "index" in errors:
                    errors["index"].append("Index is out of range")
                else:
                    errors["index"] = ["Index is out of range"]
        if errors:
            return {"errors": errors, "message": "invalid input"}, 400
        data_item = await ItemDatabase.update(
            "index", new_item=item, npm=npm, index=index + 1
        )
        return (
            jsonify(
                {
                    "message": "item updated successfully",
                    "data": {
                        "items": list(data_item.item),
                        "created_at": data_item.created_at,
                    },
                }
            ),
            201,
        )

    @staticmethod
    async def get_items(npm):
        if data := await ItemDatabase.get("items", npm=npm):
            return (
                jsonify(
                    {
                        "message": "items retrieved successfully",
                        "data": {
                            "items": list(data.item),
                            "created_at": data.created_at,
                        },
                    }
                ),
                200,
            )
        return (
            jsonify(
                {
                    "message": "items not found",
                }
            ),
            404,
        )


def sync_create_item(item, npm):
    return asyncio.run(ItemController.create_item(item, npm))


def sync_first_item(item, npm):
    return asyncio.run(ItemController.first_item(item, npm))


def sync_get_items(npm):
    return asyncio.run(ItemController.get_items(npm))


def sync_index_item(item, npm, index):
    return asyncio.run(ItemController.index_item(item, npm, index))
