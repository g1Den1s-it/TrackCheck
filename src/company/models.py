from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from src.database import Base

class Company(Base):
    __tablename__ = "companies"

    company_id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    company_name = Column(String(124), nullable=False)
    company_address = Column(String(164), nullable=True)
    company_email = Column(String(124), unique=True, nullable=False)
    company_phone = Column(String(18), nullable=True)
    user1 = Column(Integer, nullable=True)
    user2 = Column(Integer, nullable=True)
    user3 = Column(Integer, nullable=True)

