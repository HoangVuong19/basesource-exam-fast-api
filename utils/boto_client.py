import base64
import hmac
import hashlib
from configs.env import get_settings
import boto3

settings = get_settings()


def get_secret_hash(username, client_id, client_secret):
    key = bytes(client_secret, "utf-8")
    message = bytes(f"{username}{client_id}", "utf-8")
    return base64.b64encode(
        hmac.new(key, message, digestmod=hashlib.sha256).digest()
    ).decode()


cognito_client = None


def boto_client():

    global cognito_client

    if not cognito_client:
        cognito_client = boto3.client(
            "cognito-idp",
            region_name=settings.region_name,
        )
    return cognito_client


def boto_client_s3():
    return boto3.client(
        "s3",
        region_name=settings.region_name,
    )
