import app.models.db as db
import speedtest
import datetime
import socket
from app.models import Device, Profile
from datetime import date, datetime
from app.utils import Converter, Formatter


class ProfileLogic:

    def get_upload_speed(self):
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            speed = st.upload()
            upload_size, upload_label = Converter.format_bytes(speed)
            print("upload size {0}, label {1}".format(Formatter.round_decimal(upload_size, 2), upload_label))
            return speed
        except Exception as e:
            print.error('error checking upload speed: ' + str(e))
            return 0

    def get_download_speed(self):
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            speed = st.download()
            download_size, download_label = Converter.format_bytes(speed)
            print("download size {0}, label {1}".format(Formatter.round_decimal(download_size, 2), download_label))
            return speed
        except Exception as e:
            print.error('error checking download speed: ' + str(e))
            return 0

    def get_ping(self):
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            return st.results.ping
        except Exception as e:
            print.error('error checking ping: ' + str(e))
            return 0

    def check_internet_connection(self):
        try:
            IPaddress = socket.gethostbyname(socket.gethostname())
            if IPaddress == "127.0.0.1":
                print("No internet, your localhost is " + IPaddress)
                return False
            else:
                print("Connected, with the IP address: " + IPaddress)
                return True
        except Exception as e:
            print.error('error checking internet connection: ' + str(e))
            return False

    def start_service_measure(self, device: Device):
        flag = self.check_internet_connection()
        if flag:
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
        else:
            print("implementar el guardado de los datos offline")
