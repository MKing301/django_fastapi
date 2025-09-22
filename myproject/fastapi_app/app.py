from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
# import requests
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
from .auth import verify_jwt_token

app = FastAPI()

# # This is a mock token verification, replace it with actual Django token/session verification
# def verify_token(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
#     # Verify token logic (can be JWT or session-based with Django)
#     if token != "valid-token":  # Replace with actual verification logic
#         raise HTTPException(status_code=401, detail="Unauthorized")
#     return token

@app.get("/protected")
def protected_route(user=Depends(verify_jwt_token)):
    return {"msg": f"Hello, {user['user_id']}"}

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI"}

# @login_required
# def call_fastapi(request):
#     token = request.session.get('_auth_user_id')  # Fetch the user ID or token
#     headers = {"Authorization": f"Bearer {token}"}
#     response = requests.get("http://127.0.0.1:8001/protected", headers=headers)

#     return JsonResponse(response.json())