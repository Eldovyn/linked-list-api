from flask import request, jsonify


def npm_middleware():
    def decorator(func):
        def wrapper(*args, **kwargs):
            if "X-NPM" not in request.headers:
                return jsonify({"error": "Unauthorized"}), 401

            npm = request.headers.get("X-NPM")
            try:
                npm = int(npm)
            except:
                return jsonify({"error": "Unauthorized"}), 401
            request.npm = npm
            response = func(*args, **kwargs)

            return response

        return wrapper

    return decorator
