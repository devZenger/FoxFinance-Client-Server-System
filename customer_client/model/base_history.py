from service import ServerRequest

from datetime import datetime, timedelta

from .model_utilites import check_date_input, format_time_to_de, format_time_to_en


class BaseHistory:

    def __init__(self, url_part):

        self.server_request = ServerRequest()
        self.url_part = url_part

        self._start_time = ""
        self._start_time_en = ""
        self._end_time = ""
        self._end_time_en = ""

        self.form_names = {"start_time": "Startdatum (tt.mm.jjjj) ",
                           "end_time": "Enddatum (tt.mm.jjjj) "}

        self.response = None

    @property
    def start_time(self):
        return self._start_time

    @property
    def start_time_en(self):
        return self._start_time_en

    @start_time.setter
    def start_time(self, input: str):
        input = input.strip()

        check, date, message = check_date_input(input)

        if message == "EN":
            self._start_time_en = date
            self.start_time = format_time_to_de(date)

        elif check:
            self._start_time = date
            self._start_time_en = format_time_to_en(date)
        else:
            raise ValueError(message)

    @property
    def end_time(self):
        return self._end_time

    @property
    def end_time_en(self):
        return self._end_time_en

    @end_time.setter
    def end_time(self, input: str):

        check, date, message = check_date_input(input)

        if message == "EN":
            self._end_time_en = date
            self._end_time = format_time_to_de(date)

        elif check:
            self._end_time = date
            self._end_time_en = format_time_to_en(date)
        else:
            raise ValueError(message)

    def get_information_by_timespan(self, token):

        status, self.response = self.server_request.get_with_parameters(self.url_part,
                                                                        token,
                                                                        self.start_time_en,
                                                                        self.end_time_en)

        return status

    def timespan_for_x_days(self, days: int):

        today = datetime.today()
        delta_date = today - timedelta(days=days)

        self.end_time = today.strftime("%Y-%m-%d")
        self.start_time = delta_date.strftime("%Y-%m-%d")
