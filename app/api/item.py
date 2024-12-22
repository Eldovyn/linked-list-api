from flask import Blueprint, request
from ..controllers import (
    sync_create_item,
    sync_first_item,
    sync_get_items,
    sync_index_item,
)
from ..middleware import npm_middleware

item_api = Blueprint("item_api", __name__)


@item_api.get("/linked-list/items")
@npm_middleware()
def get_items():
    npm = request.npm
    return sync_get_items(npm)


@item_api.post("/linked-list/last-item")
@npm_middleware()
def create_item():
    json = request.json
    item = json.get("item")
    npm = request.npm
    return sync_create_item(item, npm)


@item_api.patch("/linked-list/first-item")
@npm_middleware()
def update_item():
    json = request.json
    item = json.get("item")
    npm = request.npm
    return sync_first_item(item, npm)


@item_api.patch("/linked-list/index-item")
@npm_middleware()
def index_item():
    json = request.json
    item = json.get("item")
    index = json.get("index")
    npm = request.npm
    return sync_index_item(item, npm, index)
