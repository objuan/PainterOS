PainterOS

Physics Based AI Painting Engine

Roadmap

✔ Physics Engine

✔ Canvas Engine

✔ Brush Engine

✔ Renderer

✔ Vision

✔ Robot

✔ AI

Installation

Architecture

Examples

License


            PainterApplication
                        │
        ┌───────────────┼────────────────┐
        │               │                │
   ServiceContainer  EventBus      SimulationClock
        │               │                │
        ├───────────────┼────────────────┤
        │               │                │
 ResourceManager  PluginManager   Configuration
        │
        ▼
                 Canvas Engine
        ┌───────────────────────────────┐
        │ PigmentLayer                  │
        │ WetnessLayer                  │
        │ ThicknessLayer                │
        │ HeightLayer                   │
        │ TemperatureLayer              │
        │ AbsorbencyLayer               │
        └───────────────────────────────┘
                        │
                Physics Engine
                        │
        ┌───────────────┼────────────────┐
        │               │                │
 Brush Model     Paint Transfer     Drying
                        │
                   Renderer
                        │
                 Future ROS2