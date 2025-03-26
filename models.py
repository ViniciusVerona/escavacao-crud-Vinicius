from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ExcavationPoint(Base):
    __tablename__ = 'excavation_points'

    id = Column(Integer, primary_key=True, index=True)
    point_type = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    altitude = Column(Float)
    srid = Column(String)
    description = Column(Text)
    discovered_at = Column(DateTime, default=datetime.utcnow)
    registered_by = Column(String)
