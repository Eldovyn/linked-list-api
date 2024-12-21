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
    async def update_item(item, npm):
        errors = {}
        if not item:
            errors["item"] = "Item is required"
        if errors:
            return {"errors": errors, "message": "invalid item"}, 400
        data_item = await ItemDatabase.insert(item, npm)


def sync_create_item(item, npm):
    return asyncio.run(ItemController.create_item(item, npm))
