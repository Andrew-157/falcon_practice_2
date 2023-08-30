import falcon

from .images import Resource, ImageStore


def create_app(image_store: ImageStore) -> falcon.App:
    image_resource = Resource(image_store=image_store)
    app = falcon.App()
    app.add_route('/images', image_resource)
    return app


def get_app() -> falcon.App:
    image_store = ImageStore('.')
    return create_app(image_store=image_store)
