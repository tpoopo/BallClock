from .ball import Ball


class BallRepository:
    def __init__(self, total_balls):
        self.ball_queue = []
        self.total_balls = total_balls
        self.initialize_balls(total_balls)
        self.starting_ball_order = self.ball_queue.copy()

    def add_ball(self, ball):
        self.ball_queue.append(ball)

    def initialize_balls(self, number):
        balls = [Ball(i) for i in range(1, number + 1)]
        for b in balls:
            self.ball_queue.append(b)

    def starting_order_values(self):
        return [x.ball_number for x in self.starting_ball_order]

    def current_order_values(self):
        return [x.ball_number for x in self.ball_queue]

    def ball_positions(self):
        return [b.ball_number for b in self.ball_queue]
