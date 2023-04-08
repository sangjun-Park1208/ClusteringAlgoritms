from flask import Flask
from flask_cors import CORS
import networkx as nx
from networkx.algorithms import community
from networkx.utils import pairwise
import numpy as np
import itertools
import os
import numpy as np
import pandas as pd
import csv
import json

ROOT = os.getcwd()
DATA = "/data"
BUS = "/bus-1062"
BRANCH = "/branch-1062"
CSV = ".csv"
JSON = ".json"

BUS_PATH = ROOT + DATA + BUS + CSV
BRANCH_PATH = ROOT + DATA + BRANCH + CSV

app = Flask(__name__)
CORS(app)

def loadBusData(path):
  global busData, bus_rowCnt
  busData = pd.read_csv(path, names=['id', 'type', 'pd', 'qd', 'bs', 'area', 'vmag', 'vang', 'pvtype'])
  bus_rowCnt = len(busData.index)
  # print('busData\n', busData)
  return

def loadBranchData(path):
  global branchData, branch_rowCnt
  branchData = pd.read_csv(path, names=['from', 'to', 'r', 'x', 'b', 'tap'])
  branch_rowCnt = len(branchData.index)
  # print('branch_rowCnt', branch_rowCnt)
  return 

@app.route('/louvain/')
def runGirvanNewman():
  loadBusData(BUS_PATH)
  loadBranchData(BRANCH_PATH)
  
  bus_id = busData['id']
  bus_type = busData['type']
  bus_pd = busData['pd']
  bus_qd = busData['qd']
  bus_bs = busData['bs']
  bus_area = busData['area']
  bus_vmag = busData['vmag']
  bus_vang = busData['vang']
  bus_pvtype = busData['pvtype']
  
  branch_from = branchData['from']
  branch_to = branchData['to']
  branch_r = branchData['r']
  branch_x = branchData['x']
  branch_b = branchData['b']
  branch_tap = branchData['tap']
  
  print(bus_id)
  
  return f'{bus_id.to_json()}'

if __name__ == '__main__':
    app.run(debug=True)