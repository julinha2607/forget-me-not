from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from sqlalchemy import DateTime, Boolean

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__="tasks"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        nullable = False,
        index = True)

    title: Mapped[str] = mapped_column(
        String(45),
        nullable = False)
    
    description: Mapped[Optional[str]] = mapped_column(String(120))

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=true),
        nullable = False,
        default=lambda: datetime.now(timezone.utc), #Using a lambda function to create the default value for this column
        index=True
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=true),
        nullable = False, 
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    is_done: Mapped[bool] = mapped_column(
        Boolean,
        nullable = False,
        default= False,
        index = True)
    
    datetime_conclusion: Mapped[Optional[datetime]] = mapped_column (
        DateTime(timezone=true), 
        nullable= True
    )
