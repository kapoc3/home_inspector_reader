import socket
import netifaces
import requests
import app.models.db as db
from app.models import Device
import string
import random
from ip2geotools.databases.noncommercial import DbIpCity
from getmac import get_mac_address


class DeviceLogic:
    @classmethod
    def get_device_information(cls):
        device = Device()
        device.public_ip = cls.get_public_ip()
        device.private_ip = cls.get_private_ip()
        device.default_gateway = cls.get_default_gateway()
        device.mac = cls.get_mac_by_ip(device.private_ip)
        device.name = cls.get_random_name()
        cls.get_geo_data(device)
        return device

    @classmethod
    def get_default_gateway(cls):
        gateways = netifaces.gateways()
        default_gateway = gateways['default'][netifaces.AF_INET][0]
        return default_gateway

    @classmethod
    def get_private_ip(cls):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            # doesn't even have to be reachable
            s.connect(('10.254.254.254', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    @classmethod
    def get_public_ip(cls):
        r = requests.get(r'http://jsonip.com')
        public_ip = r.json()['ip']
        return public_ip

    @classmethod
    def get_mac_by_ip(cls, private_ip: str):
        ip_mac = get_mac_address(ip=private_ip)
        return ip_mac

    @classmethod
    def get_random_name(cls):
        letters = string.ascii_letters
        name = random.choice(string.ascii_letters)
        return name

    @classmethod
    def get_geo_data(cls, device: Device):
        response = DbIpCity.get(device.public_ip, api_key='free')
        device.latitude = response.latitude
        device.longitude = response.longitude
        device.city = response.city
        device.country = response.country
        device.region = response.region

        return device

    @classmethod
    def load_or_save_device(cls):
        device = DeviceLogic.get_device_information()
        ##TODO check if device exist in remote repository and initialice data from remotye source

        query = db.session.query(Device).filter(Device.mac == device.mac).one_or_none()
        if not query:
            db.session.add(device)
            db.session.commit()

        return query
