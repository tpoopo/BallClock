from src.ball_clock import ClockControl
from src.ball_clock.ball import Ball
from src.ball_clock.ball_repository import BallRepository
from src.ball_clock.minute_balls import MinuteBall

def test_clock_control_advance_one_minute_ball_advancement():
    ball_repo = BallRepository(30)
    min_ball = MinuteBall()
    ball_repo.ball_queue = [Ball(5), Ball(6), Ball(7), Ball(8), Ball(9)]
    min_ball.ball_queue = [Ball(11)]
    cc = ClockControl(30)
    cc.ball_repository = ball_repo
    cc.minute_balls = min_ball
    cc.advance_one_minute()
    assert ball_repo.current_order_values() == [6, 7, 8, 9]
    assert min_ball.ball_positions() == [11, 5]

