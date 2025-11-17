from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base   # ← ОБОВʼЯЗКОВИЙ ІМПОРТ !!!

class User(Base):
    tablename = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    telegram_id = Column(Integer, nullable=True)
    token = Column(String, unique=True)
    pubkey = Column(String, nullable=True)


class Message(Base):
    tablename = "messages"

    id = Column(Integer, primary_key=True, index=True)
    from_id = Column(Integer)
    to_id = Column(Integer)
    iv = Column(String)
    ciphertext = Column(String)
    msg_type = Column(String)
    ttl_sec = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
