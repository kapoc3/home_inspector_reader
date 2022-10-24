import app.models.db as db
import datetime
from sqlalchemy import (Column, Integer, String, Float, DATE, TIME, DATETIME, BOOLEAN, ForeignKey)
from sqlalchemy.orm import relationship


class Profile(db.Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    read_date = Column(DATE, default=datetime.date)
    read_time = Column(TIME)
    upload_speed = Column(Float, comment="b/s")
    download_speed = Column(Float, comment="b/s")
    ping = Column(Float, comment="b/s")
    device_id = Column(Integer, ForeignKey('device.id'), comment="device identifier")
    device = relationship("Device")


class OfflineProfile(db.Base):
    __tablename__ = 'offline_profile'
    id = Column(Integer, primary_key=True)
    offline_datetime = Column(DATETIME)
    device_id = Column(Integer, ForeignKey('device.id'))
    device = relationship("Device")


class Synchronizer(db.Base):
    __tablename__ = 'synchronizer'
    id = Column(Integer, primary_key=True)
    date_sync = Column(DATETIME)
    result = Column(String)
    message_error = Column(String)
    device_id = Column(Integer, ForeignKey('device.id'))
    device = relationship("Device")