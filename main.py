from app.logic.SpeedTest import SpeedTestLogic
from app.utils.Converter import Converter

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    size, label = Converter.format_bytes(SpeedTestLogic.get_upload_speed())
    print("size {0}, label {1}", size, label)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
