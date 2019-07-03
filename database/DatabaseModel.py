from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Boolean, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from config import database_uri


Base = declarative_base()

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    make = Column(String(20))
    model = Column(String(20))
    trim = Column(String(2))
    year = Column(Integer)
    km = Column(Integer)
    color = Column(String(30))
    specs = Column(String(20))
    first_price = Column(Integer)
    phone = Column(String(20))
    pc = Column(Integer)
    country = Column(String(50))
    location = Column(Text)
    quality_deal = Column(String(50))
    price_difference = Column(Integer)
    url = Column(Text)
    timestamp = Column(TIMESTAMP)
    listing_id = Column(String(20))
    updated = Column(Boolean)
    update_timestamp = Column(TIMESTAMP)
    removed_timestamp = Column(TIMESTAMP)
    days_on_market = Column(Integer)
    days_posted = Column(Integer)
    status = Column(String(50))


class Session(Base):
    __tablename__ = 'session'
    id = Column(Integer, primary_key=True)
    session = Column(String(16))


class Url(Base):
    __tablename__ = 'url'
    id = Column(Integer, primary_key=True)
    listing_id = Column(String(20))
    url = Column(Text)
    processed = Column(Boolean)
    active = Column(Boolean)
    session_id = Column(Integer, ForeignKey('session.id'))
    source = Column(String(50))
    updated = Column(Boolean)
    timestamp = Column(TIMESTAMP)

class Models(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    make = Column(String(100))
    model = Column(String(100))
    year = Column(String(100))
    trim = Column(String(100))
    engine_volume = Column(String(100))
    specs = Column(String(100))
    short_specs = Column(String(100))
    transmission = Column(String(100))
    short_transmission = Column(String(100))
    min_price = Column(Integer)
    max_price = Column(Integer)

class Trims(Base):
    __tablename__ = 'trims'
    id = Column(Integer, primary_key=True)
    make = Column(String(100))
    model = Column(String(100))
    year = Column(String(100))
    trim = Column(String(100))
    engine_volume = Column(String(100))
    specs = Column(String(100))
    short_specs = Column(String(100))
    transmission = Column(String(100))
    short_transmission = Column(String(100))
    min_price = Column(Integer)
    max_price = Column(Integer)
    type = Column(String(100))
    hash_code = Column(String(100), unique=True)

def create_DB():
    engine = create_engine(database_uri)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_DB()

