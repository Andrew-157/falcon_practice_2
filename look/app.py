import os

import falcon

from .images import Resource, ImageStore


def create_app(image_store: ImageStore) -> falcon.App:
    image_resource = Resource(image_store=image_store)
    app = falcon.App()
    app.add_route('/images', image_resource)
    return app


def get_app() -> falcon.App:
    storage_path = os.environ.get('LOOK_STORAGE_PATH', '.')
    image_store = ImageStore(storage_path=storage_path)
    return create_app(image_store=image_store)
