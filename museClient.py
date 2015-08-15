import argparse
import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
<<<<<<< HEAD
  parser.add_argument("--port", type=int, default=8080,
=======
  parser.add_argument("--port", type=int, default=5006,
>>>>>>> origin/master
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.UDPClient(args.ip, args.port)

  for x in range(10):
    msg = osc_message_builder.OscMessageBuilder(address = "/filter")
    msg.add_arg(random.random())
    msg = msg.build()
    client.send(msg)
    time.sleep(1)