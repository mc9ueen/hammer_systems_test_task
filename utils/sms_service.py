import time
from random import randrange


def send_sms(otp_code: str) -> None:
    time.sleep(randrange(1, 3))
    print(otp_code)
