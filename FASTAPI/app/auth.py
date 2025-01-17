from passlib.context import CryptContext
from datetime import datetime,timedelta
from jose import JWTError, jwt
import redis 

redis_client = redis.Redis(host="redis", port=6379, decode_responses=True)

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify(hashed_password,plain_password):
    return pwd_cxt.verify(hashed_password,plain_password)

def get_hashed_password(password):
    return pwd_cxt.hash(password)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM )\
     
    return encoded_jwt
