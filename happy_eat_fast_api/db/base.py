from sqlalchemy.orm import DeclarativeBase

from happy_eat_fast_api.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
