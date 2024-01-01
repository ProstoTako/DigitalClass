import json
from datetime import datetime
from api import register_booking


class Booking:
    def __init__(self, room_name: str, start: datetime, end: datetime):
        if start >= end:
            raise ValueError
        self.room_name = room_name
        self.start = start
        self.end = end

    @property
    def duration(self) -> int:
        """returns the number of minutes allocated for the meeting"""
        seconds = (self.end - self.start).total_seconds()
        return int(seconds / 60)

    @property
    def start_date(self) -> str:
        """Booking start date in format YYYY-MM-DD"""
        return str(self.start.date())

    @property
    def end_date(self) -> str:
        """Booking end date in format YYYY-MM-DD"""
        return str(self.end.date())

    @property
    def start_time(self) -> str:
        """Booking start time in format HH:MM"""
        hour = f'0{self.start.hour}' if self.start.hour < 10 else f'{self.start.hour}'
        minute = f'0{self.start.minute}' if self.start.minute < 10 else f'{self.start.minute}'
        return hour + ':' + minute

    @property
    def end_time(self) -> str:
        """Booking end time in format HH:MM"""
        hour = f'0{self.end.hour}' if self.end.hour < 10 else f'{self.end.hour}'
        minute = f'0{self.end.minute}' if self.end.minute < 10 else f'{self.end.minute}'
        return hour + ':' + minute


def create_booking(room_name, start, end) -> str:
    print("Начинаем создание бронирования")
    created = None
    msg = None
    booking = None
    try:
        booking = Booking(room_name, start, end)
        result = register_booking(booking)
    except KeyError:
        created = False
        msg = "Комната не найдена"
    else:
        created = result
        msg = "Бронирование создано" if created else "Комната занята"
    finally:
        print("Заканчиваем создание бронирования")
        if created is not None:
            answer = {
                'created': created,
                'msg': msg,
                'booking': {
                    "room_name": booking.room_name,
                    "start_date": booking.start_date,
                    "start_time": booking.start_time,
                    "end_date": booking.end_date,
                    "end_time": booking.end_time,
                    "duration": booking.duration
                }
            }
            return json.dumps(answer)