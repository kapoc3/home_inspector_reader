import speedtest


class SpeedTestLogic:

    @classmethod
    def get_upload_speed(cls,):
        st = speedtest.Speedtest()
        speed = st.upload()
        return speed
