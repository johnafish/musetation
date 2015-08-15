import argparse
import math
import time

from pythonosc import dispatcher
from pythonosc import osc_server

def initArrays():
  global alphaArray, betaArray, deltaArray, thetaArray
  global timesCalled, lastSubmit, serverRunning
  timesCalled = 0
  alphaArray = []
  betaArray = []
  thetaArray = []
  deltaArray = []
  lastSubmit = time.time()
  serverRunning = False

def print_volume_handler(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))

def print_compute_handler(unused_addr, args, volume):
  print("Ok")
  try:
    print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass

def getAverage(*nums):
  total = 0
  nums = list(nums)
  for i in range(len(nums[0])):
    if i>0:
      total += float(nums[0][i])
  total = total/4
  return total

def arrayAverage(array):
  total = 0
  for i in array:
    total += i
  return total/(len(array))

def alphaData(*data):
  global alphaArray
  alphaArray.append(getAverage(data))
  submitData()

def betaData(*data):
  global betaArray
  betaArray.append(getAverage(data))
  submitData()

def deltaData(*data):
  global deltaArray
  deltaArray.append(getAverage(data))
  submitData()

def thetaData(*data):
  global thetaArray
  thetaArray.append(getAverage(data))
  submitData()

def submitData():
  global lastSubmit, alphaArray, betaArray, deltaArray, thetaArray
  if time.time() - lastSubmit > 3:
    lastSubmit = time.time()
    avgArray = [arrayAverage(alphaArray), arrayAverage(betaArray), arrayAverage(deltaArray), arrayAverage(thetaArray)]
    print(avgArray)
    mostActiveIndex = avgArray.index(max(avgArray))
    f = open('./file.txt', 'a')
    f.write(str(mostActiveIndex)+",")
    f.close()
    # print('Wrote ' + str(mostActiveIndex)) + ' to file.')
    alphaArray = []
    betaArray = []
    thetaArray = []
    deltaArray = []


def runMuseServer():
  global dispatcher, Dispatcher, serverRunning
  if not serverRunning:
    print('called')
    serverRunning = True
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
        default="localhost", help="The ip to listen on")
    parser.add_argument("--port",
        type=int, default=5005, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/muse/elements/alpha_absolute", alphaData)
    dispatcher.map("/muse/elements/beta_absolute", betaData)
    dispatcher.map("/muse/elements/delta_absolute", deltaData)
    dispatcher.map("/muse/elements/theta_absolute", thetaData)

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()