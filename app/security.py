from fastapi import Header, HTTPException
import os

ADMIN_API_KEY = os.getenv("ADMIN_API_KEY")


def verify_admin(x_api_key: str = Header(None)):
    if x_api_key != ADMIN_API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )