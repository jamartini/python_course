import requests
import datetime as dt
from smtplib import SMTP
import time

MY_LAT = -27.641399
MY_LNG = -52.270401
MY_EMAIL = "martini.jonatan.a@gmail.com"
MY_PASSWORD = "teovnuweeidygyms"
TO_EMAIL = "martini.j.andre@gmail.com"


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data_iss = iss_response.json()
    iss_longitude = float(data_iss['iss_position']['longitude'])
    iss_latitude = float(data_iss['iss_position']['latitude'])
    if (iss_longitude-5) <= MY_LNG <= (iss_longitude+5) and (iss_latitude-5) <= MY_LAT <= (iss_latitude+5):
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    sunrise_sunset = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sunrise_sunset.raise_for_status()
    data_sun = sunrise_sunset.json()
    sunrise = data_sun['results']['sunrise'].split("T")[1].split("+")[0].split(":")
    sunrise_int = [int(item) for item in sunrise]
    sunrise_int[0] -= 3
    sunset = data_sun['results']['sunset'].split("T")[1].split("+")[0].split(":")
    sunset_int = [int(item) for item in sunset]
    sunset_int[0] -= 3
    time_now = dt.datetime.now()
    time_now_list = [time_now.hour, time_now.minute, time_now.second]
    if sunset_int[0] < time_now_list[0] or time_now_list[0] < sunrise_int[0]:
        return True
    elif sunset_int == time_now_list[0] or time_now_list[0] == sunrise_int[0]:
        if sunset_int[1] < time_now_list[1] or time_now_list[1] < sunrise_int[1]:
            return True
        elif sunset_int == time_now_list[1] or time_now_list[1] == sunrise_int[1]:
            if sunset_int[2] < time_now_list[2] or time_now_list[2] < sunrise_int[2]:
                return True
    else:
        return False


while True:
    print(f"Is ISS visible? A:{is_iss_overhead()}")
    print(f"Is it night? A:{is_night()}")
    if is_iss_overhead() and is_night():
        connection = SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg="Subject:Look up!\n\nISS is right above you!"
        )
    time.sleep(60)
