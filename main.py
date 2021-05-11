from app.logic import ProfileLogic, DeviceLogic
from app.utils import Converter, Formatter
import app.models.db as db
import schedule
import time

def kap():
    #db.Base.metadata.create_all(db.engine)
    #device = DeviceLogic.load_or_save_device()
    #profile_logic = ProfileLogic()
    #profile_logic.start_service_measure(device)
    print('kapoc')

def job():
    print("I'm working...")
    db.Base.metadata.create_all(db.engine)
    device = DeviceLogic.load_or_save_device()
    profile_logic = ProfileLogic()
    profile_logic.start_service_measure(device)

if __name__ == '__main__':
    #schedule.every(60).seconds().do(kap)
    schedule.every(2).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


