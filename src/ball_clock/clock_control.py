import json

from .ball_repository import BallRepository
from .five_minute_balls import FiveMinuteBall
from .hour_balls import HourBall
from .minute_balls import MinuteBall


MINUTES_TIP_SIZE = 5
FIVE_MINUTES_TIP_SIZE = 12
HOURS_TIP_SIZE = 13  # +1 for fixed ball


class ClockControl:
    def __init__(self, total_balls):
        self.minute_balls = MinuteBall()
        self.five_minute_balls = FiveMinuteBall()
        self.hour_balls = HourBall()
        self.ball_repository = BallRepository(total_balls)
        self.number_of_balls = total_balls
        self.total_half_days = 0

    def mode_one(self):
        current_half_day_count = self.total_half_days
        while True:
            self.advance_one_minute()
            if current_half_day_count < self.total_half_days:
                current_half_day_count = self.total_half_days
                if (
                    self.ball_repository.starting_order_values()
                    == self.ball_repository.current_order_values()
                ):
                    print(
                        "{} balls cycle after {} days".format(
                            self.ball_repository.total_balls, self.total_half_days / 2
                        )
                    )
                    break

    def mode_two(self, minute_count):
        self.advance_time(minute_count)

    def advance_time(self, minute_count):
        for x in range(minute_count):
            self.advance_one_minute()
        self.print_clock_ball_positions()

    def advance_one_minute(self):
        self.minute_balls.add_ball(self.ball_repository.ball_queue.pop(0))
        if self.minute_balls.occupied_size() == MINUTES_TIP_SIZE:
            self.five_minute_balls.add_ball(self.minute_balls.ball_queue.pop())
            while self.minute_balls.occupied_size() > 0:
                self.ball_repository.add_ball(self.minute_balls.ball_queue.pop())
            if self.five_minute_balls.occupied_size() == FIVE_MINUTES_TIP_SIZE:
                self.hour_balls.add_ball(self.five_minute_balls.ball_queue.pop())
                while self.five_minute_balls.occupied_size() > 0:
                    self.ball_repository.add_ball(
                        self.five_minute_balls.ball_queue.pop()
                    )
                if self.hour_balls.occupied_size() == HOURS_TIP_SIZE:
                    last_ball = self.hour_balls.ball_queue.pop()
                    while self.hour_balls.occupied_size() > 1:
                        self.ball_repository.add_ball(self.hour_balls.ball_queue.pop())
                    self.ball_repository.add_ball(last_ball)
                    self.total_half_days += 1

    def current_ball_time(self):
        hour = self.hour_balls.occupied_size()
        minute = (
            self.five_minute_balls.occupied_size() * 5
            + self.minute_balls.occupied_size()
        )
        ball_time = "{:02d}:{:02d}".format(hour, minute)
        return ball_time

    def print_clock_ball_positions(self):
        output = {
            "Min": self.minute_balls.ball_positions(),
            "FiveMin": self.five_minute_balls.ball_positions(),
            "Hour": self.hour_balls.ball_positions(),
            "Main": self.ball_repository.ball_positions(),
        }
        print(json.dumps(output))
