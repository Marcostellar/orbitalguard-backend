from sqlalchemy.orm import Session

from app.models import Waitlist


def get_email(db: Session, email: str):

    return db.query(Waitlist).filter(
        Waitlist.email == email
    ).first()


def create_waitlist(db: Session, name: str, email: str):

    person = Waitlist(
        name=name,
        email=email
    )

    db.add(person)

    db.commit()

    db.refresh(person)

    return person