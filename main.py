from app.logic.SpeedTest import SpeedTestLogic
from app.utils import Converter, Formatter

if __name__ == '__main__':
    upload_size, upload_label = Converter.format_bytes(SpeedTestLogic.get_upload_speed())
    print("upload size {0}, label {1}".format(Formatter.round_decimal(upload_size, 2), upload_label))
    download_size, download_label = Converter.format_bytes(SpeedTestLogic.get_download_speed())
    print("download size {0}, label {1}".format(Formatter.round_decimal(download_size, 2), download_label))
