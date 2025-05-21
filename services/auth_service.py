from configs.env import get_settings
from sqlalchemy.orm import Session
from exceptions.app_exception import CognitoError, UserNotFoundError
from repositories.user_repository import UserRepository
from configs.logging_conf import logger

from schemas.request.auth_request import LoginRequest
from schemas.response.auth_response import LoginResponse
from utils.boto_client import boto_client, get_secret_hash

import botocore

settings = get_settings()
boto_client = boto_client()


class AuthService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def login(self, data: LoginRequest):
        try:
            logger.info(f">>>>>> Start login with user: {data.email}")

            if not self.user_repository.is_user_exists(data.email):
                raise UserNotFoundError()

            logger.info(">>>>>> Calling Cognito")
            response = boto_client.admin_initiate_auth(
                UserPoolId=settings.user_pool_id,
                ClientId=settings.client_id,
                AuthFlow="ADMIN_USER_PASSWORD_AUTH",
                AuthParameters={
                    "USERNAME": data.email,
                    "PASSWORD": data.password,
                    "SECRET_HASH": get_secret_hash(
                        data.email, settings.client_id, settings.client_secret
                    ),
                },
            )

            if response.get("ChallengeName"):
                response = LoginResponse(
                    challengeName=response["ChallengeName"],
                    session=response["Session"],
                )
                logger.info(
                    f">>>>>> End login with challenge name: {response.challengeName}"
                )

            return response

        except botocore.exceptions.ClientError as e:
            logger.error(
                f">>>>>> Error calling cognito: {e.response.get('Error', None)}"
            )
            raise CognitoError()
