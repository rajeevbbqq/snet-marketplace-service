from sqlalchemy import Column, VARCHAR, Float, TIMESTAMP, Integer
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Order(Base):
    __tablename__ = "order"
    id = Column("id", VARCHAR(255), primary_key=True)
    amount = Column("amount", Float, nullable=False)
    username = Column("username", VARCHAR(225), nullable=False)
    created_at = Column("created_at", TIMESTAMP(timezone=False))
    item_details = Column("item_details", JSON)


class Payment(Base):
    __tablename__ = "payment"
    payment_id = Column("payment_id", VARCHAR(255), primary_key=True)
    amount = Column("amount", Float, nullable=False)
    order_id = Column("order_id", VARCHAR(255), nullable=False)
    payment_details = Column("payment_details", JSON, nullable=False)
    payment_status = Column("payment_status", VARCHAR(225), nullable=False)
    created_at = Column("created_at", TIMESTAMP(timezone=False))
