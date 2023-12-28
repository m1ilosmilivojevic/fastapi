from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(input_password: str):
    return pwd_context.hash(input_password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)