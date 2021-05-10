from app.logic import SpeedTestLogic, DeviceLogic
from app.utils import Converter, Formatter
from tortoise import Tortoise, fields, run_async
import app.models.db as db

async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        db_url='sqlite://database/home_inspector.db',
        modules={'models': ['app.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()

#async def process_device():
    #device = DeviceLogic.get_device_information()
    #asyncio.set_event_loop(asyncio.new_event_loop())
    #device = await run_async(DeviceLogic.save_device(device))


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    DeviceLogic.load_or_save_device()
    upload_size, upload_label = Converter.format_bytes(SpeedTestLogic.get_upload_speed())
    print("upload size {0}, label {1}".format(Formatter.round_decimal(upload_size, 2), upload_label))
    download_size, download_label = Converter.format_bytes(SpeedTestLogic.get_download_speed())
    print("download size {0}, label {1}".format(Formatter.round_decimal(download_size, 2), download_label))


