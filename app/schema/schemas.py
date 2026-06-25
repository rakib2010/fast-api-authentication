from datetime import datetime
from pydantic import BaseModel

# User Registration Request
class UserRegistrationRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    password: str


# User Login Request
class UserLoginRequest(BaseModel):
    email: str
    password: str


# User Login Response
class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'


# User Profile/Registration Response
class UserProfileResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    created_at: datetime
    updated_at: datetime













