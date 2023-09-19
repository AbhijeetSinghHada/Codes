from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token, get_jwt, jwt_required
from passlib.hash import pbkdf2_sha256 as sha256
from blocklist import BLOCKLIST

from schemas import UserSchema
from models import UserModel

from db import db
blp = Blueprint("Users", __name__, description="Operations on Users")


@blp.route("/register")
class UserRegister(MethodView):

    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data['username']).first():
            abort(400, message="A user with that username already exists.")

        user = UserModel(username=user_data["username"],
                         password=sha256.hash(user_data["password"]))

        try:
            db.session.add(user)
            db.session.commit()
        except:
            abort(500, message="An error occurred while creating the user.")

        return user


@blp.route("/user/<int:user_id>")
class User(MethodView):

    @jwt_required()
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    @jwt_required()
    @blp.response(202, description="Deletes a user.", example="{'message': 'User deleted'}")
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}


@blp.route("/login")
class Login(MethodView):

    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.username == user_data.get("username")).first()

        if user and sha256.verify(user_data.get("password"), user.password):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}

        abort(401, message="Invalid user credentials")


@blp.route("/logout")
class Logout(MethodView):

    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out"}
