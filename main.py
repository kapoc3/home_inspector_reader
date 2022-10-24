from app.logic import ProfileLogic, DeviceLogic
import app.models.db as db
import schedule
import time

def job():
    try:
        print("I'm working...")
        db.Base.metadata.create_all(db.engine)
        device = DeviceLogic.load_or_save_device()
        profile_logic = ProfileLogic()
        profile_logic.start_service_measure(device)
    except Exception as e:
        print.error('error executong job: ' + str(e))

if __name__ == '__main__':

    #job()
    schedule.every(1).minutes.do(job)

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except Exception as e:
            print.error('error checking upload speed: ' + str(e))

