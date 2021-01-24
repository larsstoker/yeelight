from yeelight import Bulb
from yeelight import *

# Yeelight transition
transition_alerting = [
    SleepTransition(duration=200),
    RGBTransition(255, 0, 0, duration=200, brightness=100),
    SleepTransition(duration=200),
    RGBTransition(255, 0, 0, duration=200, brightness=20),
    SleepTransition(duration=200),
]

# Yeelight flow
flow_alerting = Flow(
  action=Flow.actions.recover,
  count=0,
  transitions=transition_alerting,
)

# Yeelight IP address
light = "10.0.50.102"

bulb = Bulb(light)
bulb.start_flow(flow_alerting)