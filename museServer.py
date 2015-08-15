import argparse
import math
import time

from pythonosc import dispatcher
from pythonosc import osc_server

def initArrays():
  global alphaArray, betaArray, deltaArray, thetaArray, timesCalled, lastSubmit
  timesCalled = 0
  alphaArray = []
  betaArray = []
  thetaArray = []
  deltaArray = []
  lastSubmit = time.time()


def print_volume_handler(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))

def print_compute_handler(unused_addr, args, volume):
  print("Ok")
  try:
    print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass

def getAverage(*nums):
  total = 0
  for i in nums:
    total += i
  return total/(len(nums))

def arrayAverage(array):
  total = 0
  for i in array:
    total += i
  return total/(len(nums))

def clientDataHandler(*data):
  global alphaArray, betaArray, deltaArray, thetaArray, timesCalled
  mean = getAverage(data)
  if timesCalled % 4 == 0:
    alphaArray.append(mean)
  elif timesCalled % 4 == 1:
    betaArray.append(mean)
  elif timesCalled % 4 == 2:
    deltaArray.append(mean)
  else:
    thetaArray.append(mean)
  timesCalled += 1
  submitData()

def submitData():
  global lastSubmit, alphaArray, betaArray, deltaArray, thetaArray
  if time.time() - lastSubmit > 3:
    lastSubmit = time.time()
    avgArray = [arrayAverage(alphaArray), arrayAverage(betaArray), arrayAverage(deltaArray), arrayAverage(thetaArray)]
    mostActiveIndex = avgArray.find(max(avgArray))
    f = open('./file.txt', 'w')
    f.write(mostActiveIndex)
    f.close()
    print('Wrote ' + str(mostActiveIndex)) + ' to file.')
    alphaArray = []
    betaArray = []
    thetaArray = []
    deltaArray = []


if __name__ == "__main__":
  initArrays()
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="localhost", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/muse/elements/alpha_absolute", print)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()