from typing import Optional

from pydantic import BaseModel, Field


class LoginResponse(BaseModel):
    idToken: Optional[str] = Field(None, description="ID token from Cognito")
    accessToken: Optional[str] = Field(None, description="Access token from Cognito")
    refreshToken: Optional[str] = Field(None, description="Refresh token from Cognito")
    expiresIn: Optional[int] = Field(
        None, description="Token expiration time in seconds"
    )
    session: Optional[str] = Field(
        None, description="Session ID for challenge response"
    )
    challengeName: Optional[str] = Field(None, description="challenge name")
