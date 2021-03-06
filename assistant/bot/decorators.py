from functools import wraps
import logging

from telegram import Update
from sqlalchemy.sql import select, insert, update, delete

from assistant.database import Session
from assistant.database import User

logger = logging.getLogger()


def db_session(func):
    """ Pushes 'session' argument to a function """

    @wraps(func)
    def inner(*args, **kwargs):
        if "session" in kwargs:
            return func(*args, **kwargs)
        session = Session()
        kwargs.update({
            "session": session,
        })
        output = func(*args, **kwargs)
        return output
    return inner


def acquire_user(func):
    """
    Pushes 'user' argument to a function.
    Creates or updates User if needed.
    """

    @wraps(func)
    def inner(*args, **kwargs):
        if "user" in kwargs:
            return func(*args, **kwargs)

        update: Update = kwargs.get("update", args[0])
        session: Session = kwargs.get("session")

        user = session.query(User).get(update.effective_user.id)
        if user is None:
            user = User(
                tg_id=update.effective_user.id,
                tg_username=update.effective_user.username,
            )
            session.add(user)
            session.commit()

        if user.tg_username != update.effective_user.username:
            user.tg_username = update.effective_user.username
            session.commit()

        kwargs.update({
            "user": user,
        })
        return func(*args, **kwargs)

    return inner
