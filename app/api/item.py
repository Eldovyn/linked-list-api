from flask import Blueprint, request
from ..controllers import sync_create_item
from ..middleware import npm_middleware

item_api = Blueprint("item_api", __name__)


@item_api.post("/linked-list/item")
@npm_middleware()
def create_item():
    json = request.json
    item = json.get("item")
    return sync_create_item(item, request.npm)


@item_api.patch("/linked-list/item")
@npm_middleware()
def update_item():
    json = request.json
    item = json.get("item")
    return sync_create_item(item, request.npm)
