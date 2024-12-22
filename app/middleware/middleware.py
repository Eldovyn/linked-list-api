from flask import request, jsonify
from functools import wraps


def npm_middleware():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if "X-NPM" not in request.headers:
                return jsonify({"error": "Unauthorized"}), 401

            npm = request.headers.get("X-NPM")

            request.npm = npm
            return func(*args, **kwargs)

        return wrapper

    return decorator
