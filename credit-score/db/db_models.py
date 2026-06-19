from sqlalchemy import ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import Optional


class Base(DeclarativeBase):
    pass 

class UserApplication(Base):
    __tablename__ = "user_application"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    income: Mapped[int] = mapped_column(Integer)
    credit_score: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, default=None)
    existing_debt: Mapped[int] = mapped_column(Integer)
    application_created: Mapped[str] = mapped_column(DateTime)
    
    def __repr__(self) -> str:
        return f'User(id={self.id!r}, name={self.name!r}, income={self.income}, credit_score={self.credit_score!r}, existing_debt={self.existing_debt!r}, application_created={self.application_created!r}), '
    
class ApplicationEvents(Base):
    __tablename__ = "application_events"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name_id: Mapped[int] = mapped_column(ForeignKey("user_application.id"))
    decision_viewed: Mapped[str] = mapped_column(String(50))
    decision_generated: Mapped[str] = mapped_column(String(200))
    
    def __repr__(self) -> str:
        return f'User(id={self.id!r}, decision_viewed={self.decision_viewed!r}, decision_generated={self.decision_generated!r}),'