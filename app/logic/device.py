import socket
import struct
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
        device.private_ip = cls.get_default_gateway_linux()
        device.mac = cls.get_mac_by_ip(device.private_ip)
        device.name = cls.get_random_name()
        cls.get_geo_data(device)
        return device

    @classmethod
    def get_default_gateway_linux(cls):
        """Read the default gateway directly from /proc."""
        with open("/proc/net/route") as fh:
            for line in fh:
                fields = line.strip().split()
                if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                    # If not default route or not RTF_GATEWAY, skip it
                    continue

                return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))

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
