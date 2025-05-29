from fastapi import Depends , status , HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError , jwt
from datetime import datetime , timedelta
from . import schemas , database , models
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'login' )

#SECRET KEY 
#ALGORITHM
#EXPIRATION TIME

SECRET_KEY = "c3e68a1fc0b8eedbcf594c4f74531f85728f100a214fcf4f59b10b9fd4ebc295"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data : dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp" : expire})

    encoded_jwt = jwt.encode(to_encode , SECRET_KEY , algorithm = ALGORITHM)

    return encoded_jwt


def verify_access_token(token : str , credentials_exception):
    try:
        print(token)
        payload = jwt.decode(token , SECRET_KEY , algorithms = [ALGORITHM])
        print(payload)

        id : str = payload.get("user_id")

        if id is None:
            raise credentials_exception 
    
        token_data  = schemas.TokenData(id = id) 
        print(token_data)
        print(type(token_data))

    except JWTError: 
        raise credentials_exception
    
    
    return token_data
    
def get_current_user(token : str = Depends(oauth2_scheme) , db : Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED , \
                                          detail = f"Could not validate credentials" , \
                                            headers = {"WWW-Authentic" : "Bearer"})
    
    token = verify_access_token(token , credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user 