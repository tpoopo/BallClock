class BallSlot:

    def __init__(self):
        self.ball_queue = []

    def add_ball(self, ball):
        self.ball_queue.append(ball)

    def occupied_size(self):
        return len(self.ball_queue)

    def ball_positions(self):
        return [b.ball_number for b in self.ball_queue]
