import app.models.db as db
import speedtest
import datetime
from app.models import Device, Profile
from datetime import date, datetime
from app.utils import Converter, Formatter

class ProfileLogic:

    def get_upload_speed(self):
        st = speedtest.Speedtest()
        speed = st.upload()
        upload_size, upload_label = Converter.format_bytes(speed)
        print("upload size {0}, label {1}".format(Formatter.round_decimal(upload_size, 2), upload_label))
        return speed

    def get_download_speed(self):
        st = speedtest.Speedtest()
        speed = st.download()
        download_size, download_label = Converter.format_bytes(speed)
        print("download size {0}, label {1}".format(Formatter.round_decimal(download_size, 2), download_label))
        return speed

    def get_ping(self):
        servernames = []
        st = speedtest.Speedtest()
        st.get_servers(servernames)
        return st.results.ping

    def start_service_measure(self, device: Device):
        flag = True
        while flag:
            profile = Profile()
            profile.device = device
            profile.upload_speed = self.get_upload_speed()
            profile.download_speed = self.get_download_speed()
            profile.ping = self.get_ping()
            profile.read_date = date.today()
            profile.read_time = datetime.now().time()
            db.session.add(profile)
            db.session.commit()
            flag = False
