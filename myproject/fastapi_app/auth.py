from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

SECRET_KEY = "django-insecure-bw-v@7ks(^$_nr5h&2i)(s&0k(p(3nuz%#ta%wuf#wa3!hbe)c"
ALGORITHM = "HS256"

auth_scheme = HTTPBearer()

def verify_jwt_token(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")
