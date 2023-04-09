from flask import Flask, request
from flask_cors import CORS
import os
import pandas as pd
import networkx as nx
from networkx.algorithms import community
import leidenalg
import igraph as ig
import itertools

## Dataframe 직접 가공에 대한 warning 제거
pd.set_option('mode.chained_assignment', None)

## Data loading을 위한 변수
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

@app.route('/girvan-newman/', methods=['GET'])
def runGirvanNewman():
  if request.method == 'GET':
    # 반복 횟수를 요청 parameter로 받음
    iterNum = request.args.get('iter', '')

    busData = pd.read_csv(BUS_PATH, names=['id', 'type', 'pd', 'qd', 'bs', 'area', 'vmag', 'vang', 'pvtype'])
    branchData = pd.read_csv(BRANCH_PATH, names=['from', 'to', 'r', 'x', 'b', 'tap'])
    
    branch_from = branchData['from']
    branch_to = branchData['to']

    ## 방향성 멀티 그래프 생성 (= null graph: 0 node, 0 edge)
    G = nx.MultiDiGraph()
    
    ## Node, Edge 추가 (아무 연결도 없는 Node는 없다고 가정 -> Branch data 기준으로 add edge)
    for e in range(1, len(branchData)):
      G.add_edge(branch_from[e], branch_to[e], edge=e)
    
    ## Debug: Node & Edge 개수
    print(f'Node Count: {G.number_of_nodes()}', sep=" ")
    print(f'Edge Count: {G.number_of_edges()}', sep=" ")
    
    ## Girvan-newman 알고리즘 적용
    comp = community.centrality.girvan_newman(G)
    for communities in itertools.islice(comp, int(iterNum)):
      girvan_newman_result = tuple(sorted(c) for c in communities)

    ## 각 Community의 노드 개수 및 결과 출력
    k = 1
    for i in girvan_newman_result:
      print(f"Community {k}: {len(i)}", sep=" ")
      k += 1
    print(f"Community Count: {len(girvan_newman_result)}", sep=" ")
    
    ## Cluster 추가 & Dataframe으로 구성
    busData = busData.drop([0], axis=0)
    busData = busData.drop('area', axis=1)
    busData['cluster'] = -1
    branchData = branchData.drop([0], axis=0)
    
    for i, row in enumerate(girvan_newman_result):
      print("cluster", i, end=" ")
      row = list(map(int, row))
      row.sort()
      print(row)
      busData['cluster'][row] = i
    
    ## JSON 객체로 변환
    bus_dict = busData.to_dict('records')
    branch_dict = branchData.to_dict('records')
    data = {
      'bus': bus_dict,
      'branch': branch_dict
    }

    ## JSON 객체 리턴
    return f'{data}'
  
  return 'error'

@app.route('/louvain/', methods=['GET'])
def runLouvain():
  if request.method == 'GET':    
    # 반복 횟수를 요청 parameter로 받음
    resolution = request.args.get('resolution', None)
    resolution = float(resolution)
    threshold = request.args.get('threshold', None)
    threshold = float(threshold)
    seed = request.args.get('seed', None)
    seed = int(seed)
    print(float(resolution))
    print(float(threshold))

    busData = pd.read_csv(BUS_PATH, names=['id', 'type', 'pd', 'qd', 'bs', 'area', 'vmag', 'vang', 'pvtype'])
    branchData = pd.read_csv(BRANCH_PATH, names=['from', 'to', 'r', 'x', 'b', 'tap'])
    
    branch_from = branchData['from']
    branch_to = branchData['to']

    ## 방향성 멀티 그래프 생성 (= null graph: 0 node, 0 edge)
    G = nx.MultiDiGraph()
    
    ## Node, Edge 추가 (아무 연결도 없는 Node는 없다고 가정 -> Branch data 기준으로 add edge)
    for e in range(1, len(branchData)):
      G.add_edge(branch_from[e], branch_to[e], edge=e)
    
    res = community.louvain_communities(G, resolution=resolution, threshold=threshold, seed=seed)
    # print(res)
    print(len(res))
    
    return f''
    
  return 'error'

# function to obtain the communities calculated by leiden algorithm
def get_leiden_communities(graph, random_state=0):
    if isinstance(graph, (nx.Graph, nx.DiGraph)):
        graph = ig.Graph.from_networkx(graph)
    return list(leidenalg.find_partition(graph, partition_type=leidenalg.ModularityVertexPartition, seed=random_state))
  
@app.route('/leidon/', methods=['GET'])
def runLeidon():
    branch = pd.read_csv(BRANCH_PATH, encoding = 'euc-kr')
    bus = pd.read_csv(BUS_PATH, encoding = 'euc-kr')
    bus = bus.drop('area', axis=1)
    bus['cluster'] = -1
  
    # 멀티 그래프 객체 생성
    mg = nx.MultiGraph()
    
    # node 추가
    for i in range(len(bus['id'])):
      mg.add_node(bus['id'][i])

    # edge 추가
    for i in range(len(branch['from'])):
      mg.add_edges_from([(branch['from'][i], branch['to'][i])])
    
    leiden_communities = get_leiden_communities(mg)
    for i, row in enumerate (leiden_communities):
      print("cluster", i)
      print(row)
      bus['cluster'][row] = i


    bus_dict = bus.to_dict('records')
    branch_dict = branch.to_dict('records')
    data = {
      'bus': bus_dict,
      'branch': branch_dict
    }
    return f'{data}'

if __name__ == '__main__':
    app.run(debug=True)