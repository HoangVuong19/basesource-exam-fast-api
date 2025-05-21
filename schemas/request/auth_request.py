from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    email: str = Field(..., description="Email address of the user")
    password: str = Field(..., description="User's password")
