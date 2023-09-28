from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from schemas import TagSchema, TagAndItemSchema
from models import StoreModel, TagModel, ItemModel
from db import db
from sqlalchemy.exc import SQLAlchemyError
blp = Blueprint("Tags", __name__, description="Operations on Tags")


@blp.route("/store/<int:store_id>/tag")
class TagsInStore(MethodView):

    @jwt_required()
    @blp.response(200, TagSchema(many=True))
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)

        return store.tags.all()

    @jwt_required()
    @blp.arguments(TagSchema)
    @blp.response(200, TagSchema)
    def post(self, tag_data, store_id):
        # if TagModel.query.filter_by(TagModel.store_id == store_id, name=tag_data["name"]).first():
        #     abort(400, message="A tag with that name already exists.")
        tag = TagModel(**tag_data, store_id=store_id)

        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=e)

        return tag


@blp.route("/tag/<int:tag_id>")
class Tag(MethodView):

    @jwt_required()
    @blp.response(200, TagSchema)
    def get(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        return tag

    @jwt_required()
    @blp.response(202, description="Deletes a tag if no item is linked to it.", example="{'message': 'Tag deleted'}")
    @blp.alt_response(400, description="Returned if the tag is assigned to one or more items. In this case tag is not deleted ")
    def delete(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)

        if not tag.items:
            db.session.delete(tag)
            db.session.commit()
            return {"message": "Tag deleted"}

        abort(400, message="Tag is assigned to one or more items.")


@blp.route("/item/<int:item_id>/tag/<int:tag_id>")
class LinkTagsToItems(MethodView):

    @jwt_required()
    @blp.response(201, TagSchema)
    def post(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)
        if tag in item.tags:
            abort(400, message="Item already has this tag.")

        item.tags.append(tag)

        try:
            db.session.add(item)
            db.session.commit()

        except SQLAlchemyError as e:
            abort(500, message="An error occured while inserting the tag.")
        return tag

    @jwt_required()
    @blp.response(200, TagAndItemSchema)
    def delete(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)
        if tag not in item.tags:
            abort(400, message="Item does not have this tag.")

        item.tags.remove(tag)

        try:
            db.session.add(item)
            db.session.commit()

        except SQLAlchemyError as e:
            abort(500, message="An error occured while removing the tag.")
        return {"message": "Tag removed from item.", "item": item, "tag": tag}
