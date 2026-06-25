import datetime
import jwt
import bcrypt



DATABASE_URL = 'postgresql+asyncpg://postgres:147963@localhost:5432/my_db'
SECRET_KEY = "D9r5AgJtWhAqquS8X52U0dFSRZc9pJvahXQy914dEw3"
ALGORITHM = "HS256"


#Token encode/Decode

BD_TZ = datetime.timezone(datetime.timedelta(hours=6))

def encode_access_token(user_id: int, email: str):
    exp = datetime.datetime.now(tz=BD_TZ) + datetime.timedelta(minutes=30)
    payload = {
        "user_id": user_id,
        "email": email,
        "exp": exp,
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token



def decode_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload









#Password Hash, hash verify

def hash_password(password: str): #To make password unique
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")


def verify_password(password: str, hashed_password: str):
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
















