from __future__ import annotations


class SimulationClock:

    def __init__(self) -> None:

        self.simulation_time = 0.0
        self.delta_time = 0.0

        self.frame = 0

        self.speed = 1.0

        self.running = False
        self.paused = False

    def start(self):

        self.running = True
        self.paused = False

    def stop(self):

        self.running = False
        self.paused = False

        self.simulation_time = 0.0
        self.delta_time = 0.0
        self.frame = 0

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
        self.simulation_time += self.delta_time
        self.frame += 1

    def step(self, dt: float):

        self.delta_time = dt
        self.simulation_time += dt
        self.frame += 1