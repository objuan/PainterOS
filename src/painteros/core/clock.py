from dataclasses import dataclass


@dataclass
class SimulationClock:

    time: float = 0.0
    delta_time: float = 0.0

    running: bool = False
    paused: bool = False

    speed: float = 1.0

    def start(self):
        self.running = True
        self.paused = False

    def stop(self):
        self.running = False
        self.time = 0.0
        self.delta_time = 0.0

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def tick(self, dt: float):

        if not self.running:
            return

        if self.paused:
            return

        self.delta_time = dt * self.speed
        self.time += self.delta_time
