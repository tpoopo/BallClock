from .ball import Ball
from .ball_slot import BallSlot


class HourBall(BallSlot):
    def __init__(self):
        super().__init__()
        self.add_ball(Ball(0))

    def ball_positions(self):
        # Don't count the "Fixed" ball in hour slot
        return [b.ball_number for b in self.ball_queue[1:]]
