from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask.json import jsonify
from flask_restful import Api
from .routes import register_routes

from .shared.db import db


def create_app(env = None):
    from app.config import config_by_name
    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    CORS(app)

    api = Api(app)
    register_routes(api);

    jwt = JWTManager(app)

    db.app = app
    db.init_app(app)
    db.create_all()

    

    @app.route("/health")
    def healthy():
        return jsonify("healthy")

    #TODO: add auth and jwt

    # @jwt.additional_claims_loader
    # def add_claims_to_jwt(identity):
    #     """
    #     This method is used to attach the information of the user to the JWT access token.
    #     """
    #     user = UserServices.retrieve_by_user_id(identity, app)
    #     if user:
    #         return {
    #             "user_id": user.user_id,
    #             "username": user.username,
    #             "email": user.email,
    #         }
    #     return {"description": "User is not logged in", "error": "not_logged_in"}, 401

    # callback to chick if the jwt exists in the jwt blocklist database
    # @jwt.token_in_blocklist_loader
    # def check_if_token_revoked(jwt_header, jwt_payload):
    #     jti = jwt_payload["jti"]
    #     token = db.session.query(
    #         TokenBlocklistModel.id).filter_by(jti=jti).scalar()
    #     return token is not None

    # @jwt.expired_token_loader  # going to be called when the toke expires
    # def expired_token_callback(jwt_header, jwt_payload):
    #     return (
    #         jsonify({"description": "The token has expired",
    #                 "error": "token_expired"}),
    #         401,
    #     )

    # # going to be called when the authentication is not jwt for example auth using jwt instead of Bearer when using flask_jwt_extended
    # @jwt.invalid_token_loader
    # def invalid_token_callback(error):
    #     return jsonify({"description": error, "error": "invalid_token"}), 401

    # @jwt.unauthorized_loader  # going to be called when they don't send us a jwt at all
    # def missing_token_callback(reason):
    #     return jsonify({"description": reason, "error": "authorization_required"}), 401

    # # going to be called when the token is not fresh and a fresh one is needed
    # @jwt.needs_fresh_token_loader
    # def token_not_fresh_callback(jwt_header, jwt_payload):
    #     return (
    #         jsonify(
    #             {
    #                 "description": "The token is not fresh",
    #                 "error": "fresh_token_required",
    #             }
    #         ),
    #         401,
    #     )

    # # the toke has been revoked for example if the user is logged out
    # @jwt.revoked_token_loader
    # def revoked_token_callback(jwt_header, jwt_payload):
    #     return (
    #         jsonify(
    #             {"description": "The token has been revoked", "error": "token_revoked"}
    #         ),
    #         401,
    #     )

    return app
