import app.models.db as db
from sqlalchemy import Column, Integer, String, Float, UniqueConstraint


class Device(db.Base):
    __tablename__ = 'device'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    public_ip = Column(String)
    private_ip = Column(String)
    default_gateway = Column(String)
    mac = Column(String)
    city = Column(String)
    country = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    region = Column(String)
    UniqueConstraint("mac", name="uix_mac")

    def __str__(self):
        return self.mac
