import speedtest


class SpeedTestLogic:

    @classmethod
    def get_upload_speed(cls,):
        st = speedtest.Speedtest()
        speed = st.upload()
        return speed

    @classmethod
    def get_download_speed(cls,):
        st = speedtest.Speedtest()
        speed = st.download()
        return speed
