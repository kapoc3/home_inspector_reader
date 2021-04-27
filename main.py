from app.logic.SpeedTest import SpeedTestLogic
from app.utils.Converter import Converter

if __name__ == '__main__':
    size, label = Converter.format_bytes(SpeedTestLogic.get_upload_speed())
    print("size {0}, label {1}", size, label)
