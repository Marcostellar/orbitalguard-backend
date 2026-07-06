from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import WaitlistCreate
from app import crud

router = APIRouter(prefix="/waitlist", tags=["Waitlist"])


@router.post("/join")
def join(data: WaitlistCreate,
         db: Session = Depends(get_db)):
from app.models import Waitlist

@router.get("/")
def get_waitlist(db: Session = Depends(get_db)):

    users = db.query(Waitlist).order_by(Waitlist.id.desc()).all()

    return users
    existing = crud.get_email(db, data.email)

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    user = crud.create_waitlist(
        db,
        data.name,
        data.email
    )

    return {
        "success": True,
        "message": "Welcome aboard 🚀",
        "id": user.id
    }