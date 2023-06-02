from flask import Flask, request
from flask_cors import CORS
import os
import pandas as pd
import networkx as nx
from networkx.algorithms.community.centrality import girvan_newman
from networkx.algorithms import community
from networkx import edge_betweenness_centrality as betweenness
import leidenalg
import igraph as ig
import itertools
import json

## Dataframe 직접 가공에 대한 warning 제거
pd.set_option('mode.chained_assignment', None)

ROOT = os.getcwd()
## Data loading을 위한 변수: Orthogonal Layout
ORTHOGONAL_BUS_1062 = ROOT + "/data/bus-1062.csv"
ORTHOGONAL_BUS_300 = ROOT + "/data/bus-300.csv"
ORTHOGONAL_BUS_118 = ROOT + "/data/bus-118.csv"
ORTHOGONAL_BUS_57 = ROOT + "/data/bus-57.csv"
ORTHOGONAL_BUS_30 = ROOT + "/data/bus-30.csv"
ORTHOGONAL_BUS_14 = ROOT + "/data/bus-14.csv"

ORTHOGONAL_BRANCH_1062 = ROOT + "/data/branch-1062.csv"
ORTHOGONAL_BRANCH_300 = ROOT + "/data/branch-300.csv"
ORTHOGONAL_BRANCH_118 = ROOT + "/data/branch-118.csv"
ORTHOGONAL_BRANCH_57 = ROOT + "/data/branch-57.csv"
ORTHOGONAL_BRANCH_30 = ROOT + "/data/branch-30.csv"
ORTHOGONAL_BRANCH_14 = ROOT + "/data/branch-14.csv"

## Data loading을 위한 변수: Patient flow
PATIENT_FLOW_PATH1_TYPE1 = ROOT + "/data/p1_type1.csv"
PATIENT_FLOW_PATH1_TYPE4 = ROOT + "/data/p1_type4.csv"
PATIENT_FLOW_PATH2_TYPE1 = ROOT + "/data/p2_type1.csv"
PATIENT_FLOW_PATH2_TYPE4 = ROOT + "/data/p2_type4.csv"
PATIENT_FLOW_PATH3_TYPE1 = ROOT + "/data/p3_type1.csv"
PATIENT_FLOW_PATH3_TYPE4 = ROOT + "/data/p3_type4.csv"
PATIENT_REGION1 = ROOT + "/data/p1_region.csv"
PATIENT_REGION2 = ROOT + "/data/p2_region.csv"
PATIENT_REGION3 = ROOT + "/data/p3_region.csv"

app = Flask(__name__)
CORS(app)

def most_central_edge(G):
  centrality = betweenness(G, weight="weight")
  return max(centrality, key=centrality.get)

@app.route('/girvan-newman/', methods=['GET'])
def runGirvanNewman():
  if request.method == 'GET':
    ### (ex) /girvan-newman/?data=1062&iter=8
    ### (ex) /girvan-newman/?data=300&iter=3
    dataNum = int(request.args.get('data', ''))
    iterNum = int(request.args.get('iter', ''))
    print('dataNum: ', dataNum)
    
    if dataNum == 1062:
      busData = pd.read_csv(ORTHOGONAL_BUS_1062, names=['id', 'type', 'pd', 'qd', 'bs', 'area', 'vmag', 'vang', 'pvtype'])
      branchData = pd.read_csv(ORTHOGONAL_BRANCH_1062, names=['from', 'to', 'r', 'x', 'b', 'tap'])
    elif dataNum == 300:
      busData = pd.read_csv(ORTHOGONAL_BUS_300, names=['id', 'area', 'degree'])
      branchData = pd.read_csv(ORTHOGONAL_BRANCH_300, names=['from', 'to'])
    elif dataNum == 118:
      busData = pd.read_csv(ORTHOGONAL_BUS_118, names=['id', 'area', 'degree'])
      branchData = pd.read_csv(ORTHOGONAL_BRANCH_118, names=['from', 'to'])
    elif dataNum == 57:
      busData = pd.read_csv(ORTHOGONAL_BUS_57, names=['id', 'area', 'degree'])
      branchData = pd.read_csv(ORTHOGONAL_BRANCH_57, names=['from', 'to'])
    elif dataNum == 30:
      busData = pd.read_csv(ORTHOGONAL_BUS_30, names=['id', 'area', 'degree'])
      branchData = pd.read_csv(ORTHOGONAL_BRANCH_30, names=['from', 'to'])
    elif dataNum == 14:
      busData = pd.read_csv(ORTHOGONAL_BUS_14, names=['id', 'area', 'degree'])
      branchData = pd.read_csv(ORTHOGONAL_BRANCH_14, names=['from', 'to'])
    else:
      return f'Data must in [1062, 300, 118, 57, 30, 14]'
    
    busData = busData.drop([0], axis=0)
    busData = busData.drop('area', axis=1)
    busData['cluster'] = -1
    busData = busData.astype({'id': 'int'})

    branchData = branchData.drop([0], axis=0)
    branchData = branchData.astype({'from': 'int'})
    branchData = branchData.astype({'to': 'int'})
    branch_from = branchData['from']
    branch_to = branchData['to']
    
    ## 방향성 멀티 그래프 생성 (= null graph: 0 node, 0 edge)
    G = nx.MultiDiGraph()

    ## Node 추가
    id_list = busData['id'].to_list()
    print('id_list', id_list)
    for i in id_list:
      G.add_node(i)
    
    ## Edge 추가
    for i in range(1, len(branchData.index)+1):
      G.add_edge(branch_from[i], branch_to[i])
    
    ## Debug: Node & Edge 개수
    print(f'Node Count: {G.number_of_nodes()}', sep=" ")
    print(f'Edge Count: {G.number_of_edges()}', sep=" ")
    
    comp = girvan_newman(G)
    for communities in itertools.islice(comp, iterNum):
      girvan_newman_result = tuple(sorted(c) for c in communities)
    
    for i, row in enumerate(girvan_newman_result):
      print("cluster", i)
      row = list(map(int, row))
      row.sort()
      print(row)
      for j in row:
        busData.loc[busData['id'] == j, 'cluster'] = i
    
    ## Debug: 각 Community의 노드 개수 및 결과 출력
    k = 1
    for i in girvan_newman_result:
      print(f"Community {k}: {len(i)}", sep=" ")
      k += 1
    
    ## JSON 객체 리턴
    bus_dict = busData.to_dict('records')
    branch_dict = branchData.to_dict('records')
    data = {
      'bus': bus_dict,
      'branch': branch_dict
    }
    
    json_result = json.dumps(data)
    return f'{json_result}'
  
  return 'error'

@app.route('/girvan-newman/pf/', methods=['GET'])
def runGirvanNewmanPF():
  if request.method == 'GET':
    ### (ex) /girvan-newman/pf/?p=1&iter=8
    ### (ex) /girvan-newman/pf/?p=2&iter=8
    ### (ex) /girvan-newman/pf/?p=3&iter=8
    path_type = request.args.get('p', '')
    if int(path_type) == 1:
      patient_data1 = pd.read_csv(PATIENT_FLOW_PATH1_TYPE1)
      patient_data4 = pd.read_csv(PATIENT_FLOW_PATH1_TYPE4)
      patient_region_data = pd.read_csv(PATIENT_REGION1)
    elif int(path_type) == 2:
      patient_data1 = pd.read_csv(PATIENT_FLOW_PATH2_TYPE1)
      patient_data4 = pd.read_csv(PATIENT_FLOW_PATH2_TYPE4)
      patient_region_data = pd.read_csv(PATIENT_REGION2)
    elif int(path_type) == 3:
      patient_data1 = pd.read_csv(PATIENT_FLOW_PATH3_TYPE1)
      patient_data4 = pd.read_csv(PATIENT_FLOW_PATH3_TYPE4)
      patient_region_data = pd.read_csv(PATIENT_REGION3)
    else:
      return '잘못된 parameter 입니다. p: 1~3'
    
    iterNum = int(request.args.get('iter', ''))
    
    ## type4 dataframe column명 수정
    patient_data4.columns = ['h1', 'count', 'u1']
    patient_data4['h2_a'] = patient_data4['h1']
    
    ## type1 & type4: concat (세로 방향)
    patient_data = pd.concat([patient_data1, patient_data4], axis=0, ignore_index=True)
    
    ## 불필요 u1 column 제거 & cluster column 추가(-1 초기화)
    patient_data = patient_data.drop('u1', axis=1)
    patient_data["cluster"] = -1

    ## column 명 변경
    patient_data.columns = ['from', 'to', 'weight', 'cluster']
    patient_data = patient_data[['from', 'to', 'weight', 'cluster']]
    patient_data = patient_data.sort_values(['from', 'to'])
    
    # 멀티 그래프 객체 생성
    mg = nx.MultiDiGraph()
    
    # node 추가
    l_region = patient_region_data['id'].to_list()
    for i in l_region:
      mg.add_node(i)
    
    # edge 추가
    for i in range(len(patient_data.index)):
      mg.add_weighted_edges_from([(patient_data.iloc[i]['from'], patient_data.iloc[i]['to'], patient_data.iloc[i]['weight'])])
    
    comp = girvan_newman(mg)
    for communities in itertools.islice(comp, iterNum):
      girvan_newman_result = tuple(sorted(c) for c in communities)
    
    patient_result = []
    for i, row in enumerate(girvan_newman_result):
      print('cluster', i)
      print(list(row))
      patient_result.append({"cluster": i, "nodes": list(row)})
      
    patient_result = {"result": patient_result}
    json_result = json.dumps(patient_result)
    return f'{json_result}'
  
  return 'error'

@app.route('/louvain/', methods=['GET'])
def runLouvain():
  if request.method == 'GET':    
    # (ex) /louvain/?data=300&resolution=0.1&threshold=0.0000001&seed=0
    dataNum = int(request.args.get('data', ''))
    resolution = float(request.args.get('resolution', None))
    threshold = float(request.args.get('threshold', None))
    seed = int(request.args.get('seed', None))
    
    if dataNum == 1062:
      busData = pd.read_csv(ORTHOGONAL_BUS_1062, names=['id', 'type', 'pd', 'qd', 'bs', 'area', 'vmag', 'vang', 'pvtype'])
      branchData = pd.read_csv(ORTHOGONAL_BRANCH_1062, names=['from', 'to', 'r', 'x', 'b', 'tap'])
    elif dataNum == 300:
      busData = pd.read_csv(ORTHOGONAL_BUS_300, names=['id', 'area', 'degree'])
      branchData = pd.read_csv(ORTHOGONAL_BRANCH_300, names=['from', 'to'])
    elif dataNum == 118:
      busData = pd.read_csv(ORTHOGONAL_BUS_118, names=['id', 'area', 'degree'])
      branchData = pd.read_csv(ORTHOGONAL_BRANCH_118, names=['from', 'to'])
    elif dataNum == 57:
      busData = pd.read_csv(ORTHOGONAL_BUS_57, names=['id', 'area', 'degree'])
      branchData = pd.read_csv(ORTHOGONAL_BRANCH_57, names=['from', 'to'])
    elif dataNum == 30:
      busData = pd.read_csv(ORTHOGONAL_BUS_30, names=['id', 'area', 'degree'])
      branchData = pd.read_csv(ORTHOGONAL_BRANCH_30, names=['from', 'to'])
    elif dataNum == 14:
      busData = pd.read_csv(ORTHOGONAL_BUS_14, names=['id', 'area', 'degree'])
      branchData = pd.read_csv(ORTHOGONAL_BRANCH_14, names=['from', 'to'])
    else:
      return f'Data must in [1062, 300, 118, 57, 30, 14]'
    
    branch_from = branchData['from']
    branch_to = branchData['to']

    ## 방향성 멀티 그래프 생성 (= null graph: 0 node, 0 edge)
    G = nx.MultiDiGraph()

    ## Node 추가
    id_list = busData['id'].to_list()
    id_list.remove('id')
    print('id_list', id_list)
    for i in id_list:
      G.add_node(i)    
    
    ## Edge 추가
    for i in range(1, len(branchData.index)):
      G.add_edge(branch_from[i], branch_to[i])
      
      
    # ## Node, Edge 추가 (아무 연결도 없는 Node는 없다고 가정 -> Branch data 기준으로 add edge)
    # for e in range(1, len(branchData)):
    #   G.add_edge(branch_from[e], branch_to[e], edge=e)
      
    ## Cluster 추가 & Dataframe으로 구성
    busData = busData.drop([0], axis=0)
    busData = busData.drop('area', axis=1)
    busData['cluster'] = -1
    branchData = branchData.drop([0], axis=0)
    busData = busData.astype({'id': 'int'})
    
    louvain_result = community.louvain_communities(G, resolution=resolution, threshold=threshold, seed=seed)
    for i, row in enumerate(louvain_result):
      print("cluster", i, end=" ")
      row = list(map(int, row))
      row.sort()
      print(row)
      # busData['cluster'][row] = i
      for j in row:
        busData.loc[busData['id'] == j, 'cluster'] = i

    
    ## JSON 객체 리턴
    bus_dict = busData.to_dict('records')
    branch_dict = branchData.to_dict('records')
    data = {
      'bus': bus_dict,
      'branch': branch_dict
    }
    
    json_result = json.dumps(data)
    # print(louvain_result)
    # print(len(louvain_result))
    
    return f'{json_result}'
    
  return 'error'

@app.route('/louvain/pf/', methods=['GET'])
def runLouvainPF():
  if request.method == 'GET':    
    ## url param: 
    ### /louvain/pf/?p=1&resolution=0.1&threshold=0.0000001&seed=0
    ### /louvain/pf/?p=2&resolution=0.1&threshold=0.0000001&seed=0
    ### /louvain/pf/?p=3&resolution=0.1&threshold=0.0000001&seed=0
    path_type = request.args.get('p', '')
    if int(path_type) == 1:
      patient_data1 = pd.read_csv(PATIENT_FLOW_PATH1_TYPE1)
      patient_data4 = pd.read_csv(PATIENT_FLOW_PATH1_TYPE4)
      patient_region_data = pd.read_csv(PATIENT_REGION1)
    elif int(path_type) == 2:
      patient_data1 = pd.read_csv(PATIENT_FLOW_PATH2_TYPE1)
      patient_data4 = pd.read_csv(PATIENT_FLOW_PATH2_TYPE4)
      patient_region_data = pd.read_csv(PATIENT_REGION2)
    elif int(path_type) == 3:
      patient_data1 = pd.read_csv(PATIENT_FLOW_PATH3_TYPE1)
      patient_data4 = pd.read_csv(PATIENT_FLOW_PATH3_TYPE4)
      patient_region_data = pd.read_csv(PATIENT_REGION3)
    else:
      return '잘못된 parameter 입니다. p: 1~3'
    
    resolution = float(request.args.get('resolution', None))
    threshold = float(request.args.get('threshold', None))
    seed = int(request.args.get('seed', None))
    
    ## type4 dataframe column명 수정
    patient_data4.columns = ['h1', 'count', 'u1']
    patient_data4['h2_a'] = patient_data4['h1']
    
    ## type1 & type4: concat (세로 방향)
    patient_data = pd.concat([patient_data1, patient_data4], axis=0, ignore_index=True)
    
    ## 불필요 u1 column 제거 & cluster column 추가(-1 초기화)
    patient_data = patient_data.drop('u1', axis=1)
    patient_data["cluster"] = -1

    ## column 명 변경
    patient_data.columns = ['from', 'to', 'weight', 'cluster']
    patient_data = patient_data[['from', 'to', 'weight', 'cluster']]
    patient_data = patient_data.sort_values(['from', 'to'])

    # 멀티 그래프 객체 생성
    mg = nx.MultiDiGraph()
    
    # node 추가
    l_region = patient_region_data['id'].to_list()
    for i in l_region:
      mg.add_node(i)
    
    # edge 추가
    for i in range(len(patient_data.index)):
      mg.add_weighted_edges_from([(patient_data.iloc[i]['from'], patient_data.iloc[i]['to'], patient_data.iloc[i]['weight'])])
    
    # Louvain 알고리즘 수행
    louvain_result = community.louvain_communities(mg, resolution=resolution, threshold=threshold, seed=seed)

    patient_result = []
    for i, row in enumerate(louvain_result):
      print('cluster', i)
      print(list(row))
      patient_result.append({'cluster': i, 'nodes': list(row)})
      
    patient_result = {'result': patient_result}
    print(patient_result)
    json_result = json.dumps(patient_result)
    return f'{json_result}'
  return 'error'


# function to obtain the communities calculated by leiden algorithm
def get_leiden_communities(graph):
  if isinstance(graph, nx.MultiDiGraph):
      graph = ig.Graph.from_networkx(graph)
      print("야이 ㄱ")
  return list(leidenalg.find_partition(graph, partition_type=leidenalg.ModularityVertexPartition))
  
@app.route('/leiden/', methods=['GET'])
def runLeiden():
  ### (ex) /leiden/?data=1062
  ### (ex) /leiden/?data=300
  dataNum = int(request.args.get('data', ''))
  print('dataNum: ', dataNum)
  
  if dataNum == 1062:
    busData = pd.read_csv(ORTHOGONAL_BUS_1062, names=['id', 'type', 'pd', 'qd', 'bs', 'area', 'vmag', 'vang', 'pvtype'])
    branchData = pd.read_csv(ORTHOGONAL_BRANCH_1062, names=['from', 'to', 'r', 'x', 'b', 'tap'])
  elif dataNum == 300:
    busData = pd.read_csv(ORTHOGONAL_BUS_300, names=['id', 'area', 'degree'])
    branchData = pd.read_csv(ORTHOGONAL_BRANCH_300, names=['from', 'to'])
  elif dataNum == 118:
    busData = pd.read_csv(ORTHOGONAL_BUS_118, names=['id', 'area', 'degree'])
    branchData = pd.read_csv(ORTHOGONAL_BRANCH_118, names=['from', 'to'])
  elif dataNum == 57:
    busData = pd.read_csv(ORTHOGONAL_BUS_57, names=['id', 'area', 'degree'])
    branchData = pd.read_csv(ORTHOGONAL_BRANCH_57, names=['from', 'to'])
  elif dataNum == 30:
    busData = pd.read_csv(ORTHOGONAL_BUS_30, names=['id', 'area', 'degree'])
    branchData = pd.read_csv(ORTHOGONAL_BRANCH_30, names=['from', 'to'])
  elif dataNum == 14:
    busData = pd.read_csv(ORTHOGONAL_BUS_14, names=['id', 'area', 'degree'])
    branchData = pd.read_csv(ORTHOGONAL_BRANCH_14, names=['from', 'to'])
  else:
    return f'Data must in [1062, 300, 118, 57, 30, 14]'
  
  busData = busData.drop([0], axis=0)
  busData = busData.drop('area', axis=1)
  busData['cluster'] = -1
  busData = busData.astype({'id': 'int'})
  print('busData', busData, sep='\n')
  
  branchData = branchData.drop([0], axis=0)
  branchData = branchData.astype({'from': 'int'})
  branchData = branchData.astype({'to': 'int'})
  branch_from = branchData['from']
  branch_to = branchData['to']
  # print('branch_from', branch_from, sep='\n')
  # print('branch_to', branch_to, sep='\n')
  
  
  # 멀티 그래프 객체 생성
  G = nx.MultiDiGraph()
  
  ## Node 추가
  id_list = busData['id'].to_list()
  print('id_list', id_list, sep='\n')
  for i in id_list:
    G.add_node(i)
  print('G.nodes', G.nodes, sep='\n')
  
  ## Edge 추가
  for i in range(1, len(branchData.index)+1):
    G.add_edge(branch_from[i], branch_to[i])
  print('G.edges', G.edges.data(), sep='\n')
    
  ## Debug: Node & Edge 개수
  print(f'Node Count: {G.number_of_nodes()}', sep=" ")
  print(f'Edge Count: {G.number_of_edges()}', sep=" ")


  leiden_communities = get_leiden_communities(G)
  print(leiden_communities)
  for i, row in enumerate (leiden_communities):
    print("cluster", i)
    row = list(map(int, row))
    row.sort()
    print(row)
    for j in row:
      busData.loc[busData['id'] == j+1, 'cluster'] = i
  
  busData.to_csv('C:/Users/user/Desktop/ClusteringAlgorithms/data/test.csv')

  print('after:', busData, sep='\n')
  bus_dict = busData.to_dict('records')
  branch_dict = branchData.to_dict('records')
  data = {
    'bus': bus_dict,
    'branch': branch_dict
  }
  json_result = json.dumps(data)
  return f'{json_result}'

@app.route('/leiden/pf/', methods=['GET'])
def runLeidenPF():
  ## url param: 
  ### /leiden/pf/?p=1
  ### /leiden/pf/?p=2 
  ### /leiden/pf/?p=3
  path_type = request.args.get('p', '')
  if int(path_type) == 1:
    patient_data1 = pd.read_csv(PATIENT_FLOW_PATH1_TYPE1)
    patient_data4 = pd.read_csv(PATIENT_FLOW_PATH1_TYPE4)
    patient_region_data = pd.read_csv(PATIENT_REGION1)
  elif int(path_type) == 2:
    patient_data1 = pd.read_csv(PATIENT_FLOW_PATH2_TYPE1)
    patient_data4 = pd.read_csv(PATIENT_FLOW_PATH2_TYPE4)
    patient_region_data = pd.read_csv(PATIENT_REGION2)
  elif int(path_type) == 3:
    patient_data1 = pd.read_csv(PATIENT_FLOW_PATH3_TYPE1)
    patient_data4 = pd.read_csv(PATIENT_FLOW_PATH3_TYPE4)
    patient_region_data = pd.read_csv(PATIENT_REGION3)
  else:
    return '잘못된 parameter 입니다. p: 1~3'
  
  ## type4 dataframe column명 수정
  patient_data4.columns = ['h1', 'count', 'u1']
  patient_data4['h2_a'] = patient_data4['h1']
  
  ## type1 & type4: concat (세로 방향)
  patient_data = pd.concat([patient_data1, patient_data4], axis=0, ignore_index=True)
  
  ## 불필요 u1 column 제거 & cluster column 추가(-1 초기화)
  patient_data = patient_data.drop('u1', axis=1)
  patient_data["cluster"] = -1
  
  ## column 명 변경
  patient_data.columns = ['from', 'to', 'weight', 'cluster']
  patient_data = patient_data[['from', 'to', 'weight', 'cluster']]
  patient_data = patient_data.sort_values(['from', 'to'])
  
  # 멀티 그래프 객체 생성
  mg = nx.MultiDiGraph()
  
  # node 추가
  l_region = patient_region_data['id'].to_list()
  for i in l_region:
    mg.add_node(i)
  
  # edge 추가
  for i in range(len(patient_data.index)):
    mg.add_weighted_edges_from([(patient_data.iloc[i]['from'], patient_data.iloc[i]['to'], patient_data.iloc[i]['weight'])])
  
  leiden_communities = get_leiden_communities(mg)
  
  patient_result = []
  for i, row in enumerate (leiden_communities):
    print('cluster', i)
    print(row)
    patient_result.append({'cluster': i, 'nodes': row})
    
  patient_result = {'result': patient_result}
  json_result = json.dumps(patient_result)
  return f'{json_result}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)