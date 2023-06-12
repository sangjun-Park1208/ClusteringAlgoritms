import matplotlib.pyplot as plt
import numpy as np
import json

data_path = './orthogonal_measures.json'
with open(data_path, 'r') as file:
  data = json.load(file)

colors_6 = ['royalblue', 'limegreen', 'dodgerblue', 'tomato', 'gold', 'purple']

# 그래프 그려주는 함수
def plot_group_bar_chart(xTitle, yTitle, chartName, groupNames, labelNames, data, colors):
    # x 좌표 설정
    x = np.arange(len(groupNames))

    # 그룹 막대 차트 생성
    fig, ax = plt.subplots()

    # 막대 차트 그리기
    bar_width = 0.1
    opacity = 0.8
    space = 0  # 그룹 사이의 간격

    for i, group_data in enumerate(data):
      offset = bar_width * space
      print(f'{i}: ', group_data, sep=' ')
      ax.bar(x + offset, group_data, bar_width, alpha=opacity, label=labelNames[i], color=colors[i])
      space += 1.1
    
    # 로그 스케일로 y축 변경
    ax.set_yscale('log')

    # 축, 레이블, 범례, 제목 설정
    ax.set_xlabel(xTitle)
    ax.set_ylabel(yTitle)
    ax.set_title(chartName)
    ax.set_xticks(x + bar_width * 2.5 * (len(groupNames) - 1) / 2)
    ax.set_xticklabels(groupNames)
    ax.legend()

    plt.tight_layout()
    plt.show()

def mapping(list, key):
  ret = []
  for item in list:
    ret.append(item[key])
  return ret

# (3) 
## Xticks: algorithm
## Y: Length, Crossing, Bending
## Group: Vertex 개수
## 인자: Port번호, Layout종류
def draw_port_layout(portNum, layout, data):
  groupNames = ["louvain", "leiden", "girvan-newman"]
  labelNames = ["14", "30", "57", "118", "300", "1062"]
  
  # 데이터 분리
  # louvain
  ## louvain_length
  ### zigzag
  louvain_length_4port_zigzag = mapping(data['louvain4'], "zig-zag")
  louvain_length_8port_zigzag = mapping(data['louvain8'], "zig-zag")
  louvain_length_12port_zigzag = mapping(data['louvain12'], "zig-zag")
  ### ascending
  louvain_length_4port_ascending = mapping(data['louvain4'], "ascending")
  louvain_length_8port_ascending = mapping(data['louvain8'], "ascending")
  louvain_length_12port_ascending = mapping(data['louvain12'], "ascending")
  ### local_min
  louvain_length_4port_localmin = mapping(data['louvain4'], "local_min")
  louvain_length_8port_localmin = mapping(data['louvain8'], "local_min")
  louvain_length_12port_localmin = mapping(data['louvain12'], "local_min")
  ### global_min
  louvain_length_4port_globalmin = mapping(data['louvain4'], "global_min")
  louvain_length_8port_globalmin = mapping(data['louvain8'], "global_min")
  louvain_length_12port_globalmin = mapping(data['louvain12'], "global_min")
  
  ## louvain_crossing
  louvain_crossing_4port_zigzag = mapping(data['louvain4'], "zig-zag2")
  louvain_crossing_8port_zigzag = mapping(data['louvain8'], "zig-zag2")
  louvain_crossing_12port_zigzag = mapping(data['louvain12'], "zig-zag2")
  ### ascending
  louvain_crossing_4port_ascending = mapping(data['louvain4'], "ascending2")
  louvain_crossing_8port_ascending = mapping(data['louvain8'], "ascending2")
  louvain_crossing_12port_ascending = mapping(data['louvain12'], "ascending2")
  ### local_min
  louvain_crossing_4port_localmin = mapping(data['louvain4'], "local_min2")
  louvain_crossing_8port_localmin = mapping(data['louvain8'], "local_min2")
  louvain_crossing_12port_localmin = mapping(data['louvain12'], "local_min2")
  ### global_min
  louvain_crossing_4port_globalmin = mapping(data['louvain4'], "global_min2")
  louvain_crossing_8port_globalmin = mapping(data['louvain8'], "global_min2")
  louvain_crossing_12port_globalmin = mapping(data['louvain12'], "global_min2")
  
  ## louvain_bending
  louvain_bending_4port_zigzag = mapping(data['louvain4'], "zig-zag3")
  louvain_bending_8port_zigzag = mapping(data['louvain8'], "zig-zag3")
  louvain_bending_12port_zigzag = mapping(data['louvain12'], "zig-zag3")
  ### ascending
  louvain_bending_4port_ascending = mapping(data['louvain4'], "ascending3")
  louvain_bending_8port_ascending = mapping(data['louvain8'], "ascending3")
  louvain_bending_12port_ascending = mapping(data['louvain12'], "ascending3")
  ### local_min
  louvain_bending_4port_localmin = mapping(data['louvain4'], "local_min3")
  louvain_bending_8port_localmin = mapping(data['louvain8'], "local_min3")
  louvain_bending_12port_localmin = mapping(data['louvain12'], "local_min3")
  ### global_min
  louvain_bending_4port_globalmin = mapping(data['louvain4'], "global_min3")
  louvain_bending_8port_globalmin = mapping(data['louvain8'], "global_min3")
  louvain_bending_12port_globalmin = mapping(data['louvain12'], "global_min3")
  
  
  # leiden
  ## leiden_length
  ### zigzag
  leiden_length_4port_zigzag = mapping(data['leiden4'], "zig-zag")
  leiden_length_8port_zigzag = mapping(data['leiden8'], "zig-zag")
  leiden_length_12port_zigzag = mapping(data['leiden12'], "zig-zag")
  ### ascending
  leiden_length_4port_ascending = mapping(data['leiden4'], "ascending")
  leiden_length_8port_ascending = mapping(data['leiden8'], "ascending")
  leiden_length_12port_ascending = mapping(data['leiden12'], "ascending")
  ### local_min
  leiden_length_4port_localmin = mapping(data['leiden4'], "local_min")
  leiden_length_8port_localmin = mapping(data['leiden8'], "local_min")
  leiden_length_12port_localmin = mapping(data['leiden12'], "local_min")
  ### global_min
  leiden_length_4port_globalmin = mapping(data['leiden4'], "global_min")
  leiden_length_8port_globalmin = mapping(data['leiden8'], "global_min")
  leiden_length_12port_globalmin = mapping(data['leiden12'], "global_min")
  
  ## leiden_crossing
  leiden_crossing_4port_zigzag = mapping(data['leiden4'], "zig-zag2")
  leiden_crossing_8port_zigzag = mapping(data['leiden8'], "zig-zag2")
  leiden_crossing_12port_zigzag = mapping(data['leiden12'], "zig-zag2")
  ### ascending
  leiden_crossing_4port_ascending = mapping(data['leiden4'], "ascending2")
  leiden_crossing_8port_ascending = mapping(data['leiden8'], "ascending2")
  leiden_crossing_12port_ascending = mapping(data['leiden12'], "ascending2")
  ### local_min
  leiden_crossing_4port_localmin = mapping(data['leiden4'], "local_min2")
  leiden_crossing_8port_localmin = mapping(data['leiden8'], "local_min2")
  leiden_crossing_12port_localmin = mapping(data['leiden12'], "local_min2")
  ### global_min
  leiden_crossing_4port_globalmin = mapping(data['leiden4'], "global_min2")
  leiden_crossing_8port_globalmin = mapping(data['leiden8'], "global_min2")
  leiden_crossing_12port_globalmin = mapping(data['leiden12'], "global_min2")
  
  ## leiden_bending
  leiden_bending_4port_zigzag = mapping(data['leiden4'], "zig-zag3")
  leiden_bending_8port_zigzag = mapping(data['leiden8'], "zig-zag3")
  leiden_bending_12port_zigzag = mapping(data['leiden12'], "zig-zag3")
  ### ascending
  leiden_bending_4port_ascending = mapping(data['leiden4'], "ascending3")
  leiden_bending_8port_ascending = mapping(data['leiden8'], "ascending3")
  leiden_bending_12port_ascending = mapping(data['leiden12'], "ascending3")
  ### local_min
  leiden_bending_4port_localmin = mapping(data['leiden4'], "local_min3")
  leiden_bending_8port_localmin = mapping(data['leiden8'], "local_min3")
  leiden_bending_12port_localmin = mapping(data['leiden12'], "local_min3")
  ### global_min
  leiden_bending_4port_globalmin = mapping(data['leiden4'], "global_min3")
  leiden_bending_8port_globalmin = mapping(data['leiden8'], "global_min3")
  leiden_bending_12port_globalmin = mapping(data['leiden12'], "global_min3")
  
  
  # girvan-newman
  ## girvan_length
  ### zigzag
  girvan_length_4port_zigzag = mapping(data['girvan4'], "zig-zag")
  girvan_length_8port_zigzag = mapping(data['girvan8'], "zig-zag")
  girvan_length_12port_zigzag = mapping(data['girvan12'], "zig-zag")
  ### ascending
  girvan_length_4port_ascending = mapping(data['girvan4'], "ascending")
  girvan_length_8port_ascending = mapping(data['girvan8'], "ascending")
  girvan_length_12port_ascending = mapping(data['girvan12'], "ascending")
  ### local_min
  girvan_length_4port_localmin = mapping(data['girvan4'], "local_min")
  girvan_length_8port_localmin = mapping(data['girvan8'], "local_min")
  girvan_length_12port_localmin = mapping(data['girvan12'], "local_min")
  ### global_min
  girvan_length_4port_globalmin = mapping(data['girvan4'], "global_min")
  girvan_length_8port_globalmin = mapping(data['girvan8'], "global_min")
  girvan_length_12port_globalmin = mapping(data['girvan12'], "global_min")
  
  ## girvan_crossing
  girvan_crossing_4port_zigzag = mapping(data['girvan4'], "zig-zag2")
  girvan_crossing_8port_zigzag = mapping(data['girvan8'], "zig-zag2")
  girvan_crossing_12port_zigzag = mapping(data['girvan12'], "zig-zag2")
  ### ascending
  girvan_crossing_4port_ascending = mapping(data['girvan4'], "ascending2")
  girvan_crossing_8port_ascending = mapping(data['girvan8'], "ascending2")
  girvan_crossing_12port_ascending = mapping(data['girvan12'], "ascending2")
  ### local_min
  girvan_crossing_4port_localmin = mapping(data['girvan4'], "local_min2")
  girvan_crossing_8port_localmin = mapping(data['girvan8'], "local_min2")
  girvan_crossing_12port_localmin = mapping(data['girvan12'], "local_min2")
  ### global_min
  girvan_crossing_4port_globalmin = mapping(data['girvan4'], "global_min2")
  girvan_crossing_8port_globalmin = mapping(data['girvan8'], "global_min2")
  girvan_crossing_12port_globalmin = mapping(data['girvan12'], "global_min2")
  
  ## girvan_bending
  girvan_bending_4port_zigzag = mapping(data['girvan4'], "zig-zag3")
  girvan_bending_8port_zigzag = mapping(data['girvan8'], "zig-zag3")
  girvan_bending_12port_zigzag = mapping(data['girvan12'], "zig-zag3")
  ### ascending
  girvan_bending_4port_ascending = mapping(data['girvan4'], "ascending3")
  girvan_bending_8port_ascending = mapping(data['girvan8'], "ascending3")
  girvan_bending_12port_ascending = mapping(data['girvan12'], "ascending3")
  ### local_min
  girvan_bending_4port_localmin = mapping(data['girvan4'], "local_min3")
  girvan_bending_8port_localmin = mapping(data['girvan8'], "local_min3")
  girvan_bending_12port_localmin = mapping(data['girvan12'], "local_min3")
  ### global_min
  girvan_bending_4port_globalmin = mapping(data['girvan4'], "global_min3")
  girvan_bending_8port_globalmin = mapping(data['girvan8'], "global_min3")
  girvan_bending_12port_globalmin = mapping(data['girvan12'], "global_min3")
  
  # length
  length_4port_zigzag = []
  length_8port_zigzag = []
  length_12port_zigzag = []
  length_4port_zigzag.extend([louvain_length_4port_zigzag, leiden_length_4port_zigzag, girvan_length_4port_zigzag])
  length_8port_zigzag.extend([louvain_length_8port_zigzag, leiden_length_8port_zigzag, girvan_length_8port_zigzag])
  length_12port_zigzag.extend([louvain_length_12port_zigzag, leiden_length_12port_zigzag, girvan_length_12port_zigzag])
  
  length_4port_ascending = []
  length_8port_ascending = []
  length_12port_ascending = []
  length_4port_ascending.extend([louvain_length_4port_ascending, leiden_length_4port_ascending, girvan_length_4port_ascending])
  length_8port_ascending.extend([louvain_length_8port_ascending, leiden_length_8port_ascending, girvan_length_8port_ascending])
  length_12port_ascending.extend([louvain_length_12port_ascending, leiden_length_12port_ascending, girvan_length_12port_ascending])

  length_4port_localmin = []
  length_8port_localmin = []
  length_12port_localmin = []
  length_4port_localmin.extend([louvain_length_4port_localmin, leiden_length_4port_localmin, girvan_length_4port_localmin])
  length_8port_localmin.extend([louvain_length_8port_localmin, leiden_length_8port_localmin, girvan_length_8port_localmin])
  length_12port_localmin.extend([louvain_length_12port_localmin, leiden_length_12port_localmin, girvan_length_12port_localmin])
  
  length_4port_globalmin = []
  length_8port_globalmin = []
  length_12port_globalmin = []
  length_4port_globalmin.extend([louvain_length_4port_globalmin, leiden_length_4port_globalmin, girvan_length_4port_globalmin])
  length_8port_globalmin.extend([louvain_length_8port_globalmin, leiden_length_8port_globalmin, girvan_length_8port_globalmin])
  length_12port_globalmin.extend([louvain_length_12port_globalmin, leiden_length_12port_globalmin, girvan_length_12port_globalmin])
  
  # crossing
  crossing_4port_zigzag = []
  crossing_8port_zigzag = []
  crossing_12port_zigzag = []
  crossing_4port_zigzag.extend([louvain_crossing_4port_zigzag, leiden_crossing_4port_zigzag, girvan_crossing_4port_zigzag])
  crossing_8port_zigzag.extend([louvain_crossing_8port_zigzag, leiden_crossing_8port_zigzag, girvan_crossing_8port_zigzag])
  crossing_12port_zigzag.extend([louvain_crossing_12port_zigzag, leiden_crossing_12port_zigzag, girvan_crossing_12port_zigzag])
  
  crossing_4port_ascending = []
  crossing_8port_ascending = []
  crossing_12port_ascending = []
  crossing_4port_ascending.extend([louvain_crossing_4port_ascending, leiden_crossing_4port_ascending, girvan_crossing_4port_ascending])
  crossing_8port_ascending.extend([louvain_crossing_8port_ascending, leiden_crossing_8port_ascending, girvan_crossing_8port_ascending])
  crossing_12port_ascending.extend([louvain_crossing_12port_ascending, leiden_crossing_12port_ascending, girvan_crossing_12port_ascending])

  crossing_4port_localmin = []
  crossing_8port_localmin = []
  crossing_12port_localmin = []
  crossing_4port_localmin.extend([louvain_crossing_4port_localmin, leiden_crossing_4port_localmin, girvan_crossing_4port_localmin])
  crossing_8port_localmin.extend([louvain_crossing_8port_localmin, leiden_crossing_8port_localmin, girvan_crossing_8port_localmin])
  crossing_12port_localmin.extend([louvain_crossing_12port_localmin, leiden_crossing_12port_localmin, girvan_crossing_12port_localmin])
  
  crossing_4port_globalmin = []
  crossing_8port_globalmin = []
  crossing_12port_globalmin = []
  crossing_4port_globalmin.extend([louvain_crossing_4port_globalmin, leiden_crossing_4port_globalmin, girvan_crossing_4port_globalmin])
  crossing_8port_globalmin.extend([louvain_crossing_8port_globalmin, leiden_crossing_8port_globalmin, girvan_crossing_8port_globalmin])
  crossing_12port_globalmin.extend([louvain_crossing_12port_globalmin, leiden_crossing_12port_globalmin, girvan_crossing_12port_globalmin])
   
  # bending
  bending_4port_zigzag = []
  bending_8port_zigzag = []
  bending_12port_zigzag = []
  bending_4port_zigzag.extend([louvain_bending_4port_zigzag, leiden_bending_4port_zigzag, girvan_bending_4port_zigzag])
  bending_8port_zigzag.extend([louvain_bending_8port_zigzag, leiden_bending_8port_zigzag, girvan_bending_8port_zigzag])
  bending_12port_zigzag.extend([louvain_bending_12port_zigzag, leiden_bending_12port_zigzag, girvan_bending_12port_zigzag])
  
  bending_4port_ascending = []
  bending_8port_ascending = []
  bending_12port_ascending = []
  bending_4port_ascending.extend([louvain_bending_4port_ascending, leiden_bending_4port_ascending, girvan_bending_4port_ascending])
  bending_8port_ascending.extend([louvain_bending_8port_ascending, leiden_bending_8port_ascending, girvan_bending_8port_ascending])
  bending_12port_ascending.extend([louvain_bending_12port_ascending, leiden_bending_12port_ascending, girvan_bending_12port_ascending])

  bending_4port_localmin = []
  bending_8port_localmin = []
  bending_12port_localmin = []
  bending_4port_localmin.extend([louvain_bending_4port_localmin, leiden_bending_4port_localmin, girvan_bending_4port_localmin])
  bending_8port_localmin.extend([louvain_bending_8port_localmin, leiden_bending_8port_localmin, girvan_bending_8port_localmin])
  bending_12port_localmin.extend([louvain_bending_12port_localmin, leiden_bending_12port_localmin, girvan_bending_12port_localmin])
  
  bending_4port_globalmin = []
  bending_8port_globalmin = []
  bending_12port_globalmin = []
  bending_4port_globalmin.extend([louvain_bending_4port_globalmin, leiden_bending_4port_globalmin, girvan_bending_4port_globalmin])
  bending_8port_globalmin.extend([louvain_bending_8port_globalmin, leiden_bending_8port_globalmin, girvan_bending_8port_globalmin])
  bending_12port_globalmin.extend([louvain_bending_12port_globalmin, leiden_bending_12port_globalmin, girvan_bending_12port_globalmin])

  # 그래프 그리기
  plot_group_bar_chart('Algorithm', 'Length', 'length_4port_zigzag', groupNames, labelNames, np.transpose(length_4port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', 'length_8port_zigzag', groupNames, labelNames, np.transpose(length_8port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', 'length_12port_zigzag', groupNames, labelNames, np.transpose(length_12port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', 'length_4port_ascending', groupNames, labelNames, np.transpose(length_4port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', 'length_8port_ascending', groupNames, labelNames, np.transpose(length_8port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', 'length_12port_ascending', groupNames, labelNames, np.transpose(length_12port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', 'length_4port_localmin', groupNames, labelNames, np.transpose(length_4port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', 'length_8port_localmin', groupNames, labelNames, np.transpose(length_8port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', 'length_12port_localmin', groupNames, labelNames, np.transpose(length_12port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', 'length_4port_globalmin', groupNames, labelNames, np.transpose(length_4port_globalmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', 'length_8port_globalmin', groupNames, labelNames, np.transpose(length_8port_globalmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', 'length_12port_globalmin', groupNames, labelNames, np.transpose(length_12port_globalmin), colors_6)
  
  plot_group_bar_chart('Algorithm', 'Crossing', 'crossing_4port_zigzag', groupNames, labelNames, np.transpose(crossing_4port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', 'crossing_8port_zigzag', groupNames, labelNames, np.transpose(crossing_8port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', 'crossing_12port_zigzag', groupNames, labelNames, np.transpose(crossing_12port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', 'crossing_4port_ascending', groupNames, labelNames, np.transpose(crossing_4port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', 'crossing_8port_ascending', groupNames, labelNames, np.transpose(crossing_8port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', 'crossing_12port_ascending', groupNames, labelNames, np.transpose(crossing_12port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', 'crossing_4port_localmin', groupNames, labelNames, np.transpose(crossing_4port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', 'crossing_8port_localmin', groupNames, labelNames, np.transpose(crossing_8port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', 'crossing_12port_localmin', groupNames, labelNames, np.transpose(crossing_12port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', 'crossing_4port_globalmin', groupNames, labelNames, np.transpose(crossing_4port_globalmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', 'crossing_8port_globalmin', groupNames, labelNames, np.transpose(crossing_8port_globalmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', 'crossing_12port_globalmin', groupNames, labelNames, np.transpose(crossing_12port_globalmin), colors_6)
  
  plot_group_bar_chart('Algorithm', 'Bending', 'bending_4port_zigzag', groupNames, labelNames, np.transpose(bending_4port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', 'bending_8port_zigzag', groupNames, labelNames, np.transpose(bending_8port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', 'bending_12port_zigzag', groupNames, labelNames, np.transpose(bending_12port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', 'bending_4port_ascending', groupNames, labelNames, np.transpose(bending_4port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', 'bending_8port_ascending', groupNames, labelNames, np.transpose(bending_8port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', 'bending_12port_ascending', groupNames, labelNames, np.transpose(bending_12port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', 'bending_4port_localmin', groupNames, labelNames, np.transpose(bending_4port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', 'bending_8port_localmin', groupNames, labelNames, np.transpose(bending_8port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', 'bending_12port_localmin', groupNames, labelNames, np.transpose(bending_12port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', 'bending_4port_globalmin', groupNames, labelNames, np.transpose(bending_4port_globalmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', 'bending_8port_globalmin', groupNames, labelNames, np.transpose(bending_8port_globalmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', 'bending_12port_globalmin', groupNames, labelNames, np.transpose(bending_12port_globalmin), colors_6)

draw_port_layout("", "", data)

# (4) 
## Xticks: PortNum
## Y: Length, Crossing, Bending
## Group: Vertex 개수
## 인자: Algorithm, Layout종류

def draw_algorithm_layout(algorithm, layout, data):
  groupNames = ["4port", "8port", "12port"]
  labelNames = ["14", "30", "57", "118", "300", "1062"]

  # 데이터 분리
  # port4
  ## length
  ### zigzag
  port4_length_louvain_zigzag = mapping(data['louvain4'], 'zig-zag')
  port4_length_leiden_zigzag = mapping(data['leiden4'], 'zig-zag')
  port4_length_girvan_zigzag = mapping(data['girvan4'], 'zig-zag')
  ### ascending
  port4_length_louvain_ascending = mapping(data['louvain4'], 'ascending')
  port4_length_leiden_ascending = mapping(data['leiden4'], 'ascending')
  port4_length_girvan_ascending = mapping(data['girvan4'], 'ascending')
  ### localmin
  port4_length_louvain_localmin = mapping(data['louvain4'], 'local_min')
  port4_length_leiden_localmin = mapping(data['leiden4'], 'local_min')
  port4_length_girvan_localmin = mapping(data['girvan4'], 'local_min')
  ### globalmin
  port4_length_louvain_globalmin = mapping(data['louvain4'], 'global_min')
  port4_length_leiden_globalmin = mapping(data['leiden4'], 'global_min')
  port4_length_girvan_globalmin = mapping(data['girvan4'], 'global_min')

  ## crossing
  ### zigzag
  port4_crossing_louvain_zigzag = mapping(data['louvain4'], 'zig-zag2')
  port4_crossing_leiden_zigzag = mapping(data['leiden4'], 'zig-zag2')
  port4_crossing_girvan_zigzag = mapping(data['girvan4'], 'zig-zag2')
  ### ascending
  port4_crossing_louvain_ascending = mapping(data['louvain4'], 'ascending2')
  port4_crossing_leiden_ascending = mapping(data['leiden4'], 'ascending2')
  port4_crossing_girvan_ascending = mapping(data['girvan4'], 'ascending2')
  ### localmin
  port4_crossing_louvain_localmin = mapping(data['louvain4'], 'local_min2')
  port4_crossing_leiden_localmin = mapping(data['leiden4'], 'local_min2')
  port4_crossing_girvan_localmin = mapping(data['girvan4'], 'local_min2')
  ### globalmin
  port4_crossing_louvain_globalmin = mapping(data['louvain4'], 'global_min2')
  port4_crossing_leiden_globalmin = mapping(data['leiden4'], 'global_min2')
  port4_crossing_girvan_globalmin = mapping(data['girvan4'], 'global_min2')
  
  ## bending
  ### zigzag
  port4_bending_louvain_zigzag = mapping(data['louvain4'], 'zig-zag3')
  port4_bending_leiden_zigzag = mapping(data['leiden4'], 'zig-zag3')
  port4_bending_girvan_zigzag = mapping(data['girvan4'], 'zig-zag3')
  ### ascending
  port4_bending_louvain_ascending = mapping(data['louvain4'], 'ascending3')
  port4_bending_leiden_ascending = mapping(data['leiden4'], 'ascending3')
  port4_bending_girvan_ascending = mapping(data['girvan4'], 'ascending3')
  ### localmin
  port4_bending_louvain_localmin = mapping(data['louvain4'], 'local_min3')
  port4_bending_leiden_localmin = mapping(data['leiden4'], 'local_min3')
  port4_bending_girvan_localmin = mapping(data['girvan4'], 'local_min3')
  ### globalmin
  port4_bending_louvain_globalmin = mapping(data['louvain4'], 'global_min3')
  port4_bending_leiden_globalmin = mapping(data['leiden4'], 'global_min3')
  port4_bending_girvan_globalmin = mapping(data['girvan4'], 'global_min3')
  
  # port8
  ## length
  ### zigzag
  port8_length_louvain_zigzag = mapping(data['louvain8'], 'zig-zag')
  port8_length_leiden_zigzag = mapping(data['leiden8'], 'zig-zag')
  port8_length_girvan_zigzag = mapping(data['girvan8'], 'zig-zag')
  ### ascending
  port8_length_louvain_ascending = mapping(data['louvain8'], 'ascending')
  port8_length_leiden_ascending = mapping(data['leiden8'], 'ascending')
  port8_length_girvan_ascending = mapping(data['girvan8'], 'ascending')
  ### localmin
  port8_length_louvain_localmin = mapping(data['louvain8'], 'local_min')
  port8_length_leiden_localmin = mapping(data['leiden8'], 'local_min')
  port8_length_girvan_localmin = mapping(data['girvan8'], 'local_min')
  ### globalmin
  port8_length_louvain_globalmin = mapping(data['louvain8'], 'global_min')
  port8_length_leiden_globalmin = mapping(data['leiden8'], 'global_min')
  port8_length_girvan_globalmin = mapping(data['girvan8'], 'global_min')

  ## crossing
  ### zigzag
  port8_crossing_louvain_zigzag = mapping(data['louvain8'], 'zig-zag2')
  port8_crossing_leiden_zigzag = mapping(data['leiden8'], 'zig-zag2')
  port8_crossing_girvan_zigzag = mapping(data['girvan8'], 'zig-zag2')
  ### ascending
  port8_crossing_louvain_ascending = mapping(data['louvain8'], 'ascending2')
  port8_crossing_leiden_ascending = mapping(data['leiden8'], 'ascending2')
  port8_crossing_girvan_ascending = mapping(data['girvan8'], 'ascending2')
  ### localmin
  port8_crossing_louvain_localmin = mapping(data['louvain8'], 'local_min2')
  port8_crossing_leiden_localmin = mapping(data['leiden8'], 'local_min2')
  port8_crossing_girvan_localmin = mapping(data['girvan8'], 'local_min2')
  ### globalmin
  port8_crossing_louvain_globalmin = mapping(data['louvain8'], 'global_min2')
  port8_crossing_leiden_globalmin = mapping(data['leiden8'], 'global_min2')
  port8_crossing_girvan_globalmin = mapping(data['girvan8'], 'global_min2')
  
  ## bending
  ### zigzag
  port8_bending_louvain_zigzag = mapping(data['louvain8'], 'zig-zag3')
  port8_bending_leiden_zigzag = mapping(data['leiden8'], 'zig-zag3')
  port8_bending_girvan_zigzag = mapping(data['girvan8'], 'zig-zag3')
  ### ascending
  port8_bending_louvain_ascending = mapping(data['louvain8'], 'ascending3')
  port8_bending_leiden_ascending = mapping(data['leiden8'], 'ascending3')
  port8_bending_girvan_ascending = mapping(data['girvan8'], 'ascending3')
  ### localmin
  port8_bending_louvain_localmin = mapping(data['louvain8'], 'local_min3')
  port8_bending_leiden_localmin = mapping(data['leiden8'], 'local_min3')
  port8_bending_girvan_localmin = mapping(data['girvan8'], 'local_min3')
  ### globalmin
  port8_bending_louvain_globalmin = mapping(data['louvain8'], 'global_min3')
  port8_bending_leiden_globalmin = mapping(data['leiden8'], 'global_min3')
  port8_bending_girvan_globalmin = mapping(data['girvan8'], 'global_min3')
  
  # port12
  ## length
  ### zigzag
  port12_length_louvain_zigzag = mapping(data['louvain12'], 'zig-zag')
  port12_length_leiden_zigzag = mapping(data['leiden12'], 'zig-zag')
  port12_length_girvan_zigzag = mapping(data['girvan12'], 'zig-zag')
  ### ascending
  port12_length_louvain_ascending = mapping(data['louvain12'], 'ascending')
  port12_length_leiden_ascending = mapping(data['leiden12'], 'ascending')
  port12_length_girvan_ascending = mapping(data['girvan12'], 'ascending')
  ### localmin
  port12_length_louvain_localmin = mapping(data['louvain12'], 'local_min')
  port12_length_leiden_localmin = mapping(data['leiden12'], 'local_min')
  port12_length_girvan_localmin = mapping(data['girvan12'], 'local_min')
  ### globalmin
  port12_length_louvain_globalmin = mapping(data['louvain12'], 'global_min')
  port12_length_leiden_globalmin = mapping(data['leiden12'], 'global_min')
  port12_length_girvan_globalmin = mapping(data['girvan12'], 'global_min')

  ## crossing
  ### zigzag
  port12_crossing_louvain_zigzag = mapping(data['louvain12'], 'zig-zag2')
  port12_crossing_leiden_zigzag = mapping(data['leiden12'], 'zig-zag2')
  port12_crossing_girvan_zigzag = mapping(data['girvan12'], 'zig-zag2')
  ### ascending
  port12_crossing_louvain_ascending = mapping(data['louvain12'], 'ascending2')
  port12_crossing_leiden_ascending = mapping(data['leiden12'], 'ascending2')
  port12_crossing_girvan_ascending = mapping(data['girvan12'], 'ascending2')
  ### localmin
  port12_crossing_louvain_localmin = mapping(data['louvain12'], 'local_min2')
  port12_crossing_leiden_localmin = mapping(data['leiden12'], 'local_min2')
  port12_crossing_girvan_localmin = mapping(data['girvan12'], 'local_min2')
  ### globalmin
  port12_crossing_louvain_globalmin = mapping(data['louvain12'], 'global_min2')
  port12_crossing_leiden_globalmin = mapping(data['leiden12'], 'global_min2')
  port12_crossing_girvan_globalmin = mapping(data['girvan12'], 'global_min2')
  
  ## bending
  ### zigzag
  port12_bending_louvain_zigzag = mapping(data['louvain12'], 'zig-zag3')
  port12_bending_leiden_zigzag = mapping(data['leiden12'], 'zig-zag3')
  port12_bending_girvan_zigzag = mapping(data['girvan12'], 'zig-zag3')
  ### ascending
  port12_bending_louvain_ascending = mapping(data['louvain12'], 'ascending3')
  port12_bending_leiden_ascending = mapping(data['leiden12'], 'ascending3')
  port12_bending_girvan_ascending = mapping(data['girvan12'], 'ascending3')
  ### localmin
  port12_bending_louvain_localmin = mapping(data['louvain12'], 'local_min3')
  port12_bending_leiden_localmin = mapping(data['leiden12'], 'local_min3')
  port12_bending_girvan_localmin = mapping(data['girvan12'], 'local_min3')
  ### globalmin
  port12_bending_louvain_globalmin = mapping(data['louvain12'], 'global_min3')
  port12_bending_leiden_globalmin = mapping(data['leiden12'], 'global_min3')
  port12_bending_girvan_globalmin = mapping(data['girvan12'], 'global_min3')
  
  length_louvain_zigzag = []
  length_louvain_ascending = []
  length_louvain_localmin = []
  length_louvain_globalmin = []
  length_louvain_zigzag.extend([port4_length_louvain_zigzag, port8_length_louvain_zigzag, port12_length_louvain_zigzag])
  length_louvain_ascending.extend([port4_length_louvain_ascending, port8_length_louvain_ascending, port12_length_louvain_ascending])
  length_louvain_localmin.extend([port4_length_louvain_localmin, port8_length_louvain_localmin, port12_length_louvain_localmin])
  length_louvain_globalmin.extend([port4_length_louvain_globalmin, port8_length_louvain_globalmin, port12_length_louvain_globalmin])
  
  length_leiden_zigzag = []
  length_leiden_ascending = []
  length_leiden_localmin = []
  length_leiden_globalmin = []
  length_leiden_zigzag.extend([port4_length_leiden_zigzag, port8_length_leiden_zigzag, port12_length_leiden_zigzag])
  length_leiden_ascending.extend([port4_length_leiden_ascending, port8_length_leiden_ascending, port12_length_leiden_ascending])
  length_leiden_localmin.extend([port4_length_leiden_localmin, port8_length_leiden_localmin, port12_length_leiden_localmin])
  length_leiden_globalmin.extend([port4_length_leiden_globalmin, port8_length_leiden_globalmin, port12_length_leiden_globalmin])
  
  length_girvan_zigzag = []
  length_girvan_ascending = []
  length_girvan_localmin = []
  length_girvan_globalmin = []
  length_girvan_zigzag.extend([port4_length_girvan_zigzag, port8_length_girvan_zigzag, port12_length_girvan_zigzag])
  length_girvan_ascending.extend([port4_length_girvan_ascending, port8_length_girvan_ascending, port12_length_girvan_ascending])
  length_girvan_localmin.extend([port4_length_girvan_localmin, port8_length_girvan_localmin, port12_length_girvan_localmin])
  length_girvan_globalmin.extend([port4_length_girvan_globalmin, port8_length_girvan_globalmin, port12_length_girvan_globalmin])

  crossing_louvain_zigzag = []
  crossing_louvain_ascending = []
  crossing_louvain_localmin = []
  crossing_louvain_globalmin = []
  crossing_louvain_zigzag.extend([port4_crossing_louvain_zigzag, port8_crossing_louvain_zigzag, port12_crossing_louvain_zigzag])
  crossing_louvain_ascending.extend([port4_crossing_louvain_ascending, port8_crossing_louvain_ascending, port12_crossing_louvain_ascending])
  crossing_louvain_localmin.extend([port4_crossing_louvain_localmin, port8_crossing_louvain_localmin, port12_crossing_louvain_localmin])
  crossing_louvain_globalmin.extend([port4_crossing_louvain_globalmin, port8_crossing_louvain_globalmin, port12_crossing_louvain_globalmin])
  
  crossing_leiden_zigzag = []
  crossing_leiden_ascending = []
  crossing_leiden_localmin = []
  crossing_leiden_globalmin = []
  crossing_leiden_zigzag.extend([port4_crossing_leiden_zigzag, port8_crossing_leiden_zigzag, port12_crossing_leiden_zigzag])
  crossing_leiden_ascending.extend([port4_crossing_leiden_ascending, port8_crossing_leiden_ascending, port12_crossing_leiden_ascending])
  crossing_leiden_localmin.extend([port4_crossing_leiden_localmin, port8_crossing_leiden_localmin, port12_crossing_leiden_localmin])
  crossing_leiden_globalmin.extend([port4_crossing_leiden_globalmin, port8_crossing_leiden_globalmin, port12_crossing_leiden_globalmin])
  
  crossing_girvan_zigzag = []
  crossing_girvan_ascending = []
  crossing_girvan_localmin = []
  crossing_girvan_globalmin = []
  crossing_girvan_zigzag.extend([port4_crossing_girvan_zigzag, port8_crossing_girvan_zigzag, port12_crossing_girvan_zigzag])
  crossing_girvan_ascending.extend([port4_crossing_girvan_ascending, port8_crossing_girvan_ascending, port12_crossing_girvan_ascending])
  crossing_girvan_localmin.extend([port4_crossing_girvan_localmin, port8_crossing_girvan_localmin, port12_crossing_girvan_localmin])
  crossing_girvan_globalmin.extend([port4_crossing_girvan_globalmin, port8_crossing_girvan_globalmin, port12_crossing_girvan_globalmin])

  bending_louvain_zigzag = []
  bending_louvain_ascending = []
  bending_louvain_localmin = []
  bending_louvain_globalmin = []
  bending_louvain_zigzag.extend([port4_bending_louvain_zigzag, port8_bending_louvain_zigzag, port12_bending_louvain_zigzag])
  bending_louvain_ascending.extend([port4_bending_louvain_ascending, port8_bending_louvain_ascending, port12_bending_louvain_ascending])
  bending_louvain_localmin.extend([port4_bending_louvain_localmin, port8_bending_louvain_localmin, port12_bending_louvain_localmin])
  bending_louvain_globalmin.extend([port4_bending_louvain_globalmin, port8_bending_louvain_globalmin, port12_bending_louvain_globalmin])
  
  bending_leiden_zigzag = []
  bending_leiden_ascending = []
  bending_leiden_localmin = []
  bending_leiden_globalmin = []
  bending_leiden_zigzag.extend([port4_bending_leiden_zigzag, port8_bending_leiden_zigzag, port12_bending_leiden_zigzag])
  bending_leiden_ascending.extend([port4_bending_leiden_ascending, port8_bending_leiden_ascending, port12_bending_leiden_ascending])
  bending_leiden_localmin.extend([port4_bending_leiden_localmin, port8_bending_leiden_localmin, port12_bending_leiden_localmin])
  bending_leiden_globalmin.extend([port4_bending_leiden_globalmin, port8_bending_leiden_globalmin, port12_bending_leiden_globalmin])
  
  bending_girvan_zigzag = []
  bending_girvan_ascending = []
  bending_girvan_localmin = []
  bending_girvan_globalmin = []
  bending_girvan_zigzag.extend([port4_bending_girvan_zigzag, port8_bending_girvan_zigzag, port12_bending_girvan_zigzag])
  bending_girvan_ascending.extend([port4_bending_girvan_ascending, port8_bending_girvan_ascending, port12_bending_girvan_ascending])
  bending_girvan_localmin.extend([port4_bending_girvan_localmin, port8_bending_girvan_localmin, port12_bending_girvan_localmin])
  bending_girvan_globalmin.extend([port4_bending_girvan_globalmin, port8_bending_girvan_globalmin, port12_bending_girvan_globalmin])
  
  # 그래프 그리기
  ## louvain
  plot_group_bar_chart("PortNum", "length", "length_louvain_zigzag", groupNames, labelNames, np.transpose(length_louvain_zigzag), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "crossing_louvain_zigzag", groupNames, labelNames, np.transpose(crossing_louvain_zigzag), colors_6)
  plot_group_bar_chart("PortNum", "bending", "bending_louvain_zigzag", groupNames, labelNames, np.transpose(bending_louvain_zigzag), colors_6)
  
  plot_group_bar_chart("PortNum", "length", "length_louvain_ascending", groupNames, labelNames, np.transpose(length_louvain_ascending), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "crossing_louvain_ascending", groupNames, labelNames, np.transpose(crossing_louvain_ascending), colors_6)
  plot_group_bar_chart("PortNum", "bending", "bending_louvain_ascending", groupNames, labelNames, np.transpose(bending_louvain_ascending), colors_6)
  
  plot_group_bar_chart("PortNum", "length", "length_louvain_localmin", groupNames, labelNames, np.transpose(length_louvain_localmin), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "crossing_louvain_localmin", groupNames, labelNames, np.transpose(crossing_louvain_localmin), colors_6)
  plot_group_bar_chart("PortNum", "bending", "bending_louvain_localmin", groupNames, labelNames, np.transpose(bending_louvain_localmin), colors_6)

  plot_group_bar_chart("PortNum", "length", "length_louvain_globalmin", groupNames, labelNames, np.transpose(length_louvain_globalmin), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "crossing_louvain_globalmin", groupNames, labelNames, np.transpose(crossing_louvain_globalmin), colors_6)
  plot_group_bar_chart("PortNum", "bending", "bending_louvain_globalmin", groupNames, labelNames, np.transpose(bending_louvain_globalmin), colors_6)
  
  ## leiden
  plot_group_bar_chart("PortNum", "length", "length_leiden_zigzag", groupNames, labelNames, np.transpose(length_leiden_zigzag), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "crossing_leiden_zigzag", groupNames, labelNames, np.transpose(crossing_leiden_zigzag), colors_6)
  plot_group_bar_chart("PortNum", "bending", "bending_leiden_zigzag", groupNames, labelNames, np.transpose(bending_leiden_zigzag), colors_6)
  
  plot_group_bar_chart("PortNum", "length", "length_leiden_ascending", groupNames, labelNames, np.transpose(length_leiden_ascending), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "crossing_leiden_ascending", groupNames, labelNames, np.transpose(crossing_leiden_ascending), colors_6)
  plot_group_bar_chart("PortNum", "bending", "bending_leiden_ascending", groupNames, labelNames, np.transpose(bending_leiden_ascending), colors_6)
  
  plot_group_bar_chart("PortNum", "length", "length_leiden_localmin", groupNames, labelNames, np.transpose(length_leiden_localmin), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "crossing_leiden_localmin", groupNames, labelNames, np.transpose(crossing_leiden_localmin), colors_6)
  plot_group_bar_chart("PortNum", "bending", "bending_leiden_localmin", groupNames, labelNames, np.transpose(bending_leiden_localmin), colors_6)

  plot_group_bar_chart("PortNum", "length", "length_leiden_globalmin", groupNames, labelNames, np.transpose(length_leiden_globalmin), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "crossing_leiden_globalmin", groupNames, labelNames, np.transpose(crossing_leiden_globalmin), colors_6)
  plot_group_bar_chart("PortNum", "bending", "bending_leiden_globalmin", groupNames, labelNames, np.transpose(bending_leiden_globalmin), colors_6)
  
  ## girvan-newman
  plot_group_bar_chart("PortNum", "length", "length_girvan_zigzag", groupNames, labelNames, np.transpose(length_girvan_zigzag), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "crossing_girvan_zigzag", groupNames, labelNames, np.transpose(crossing_girvan_zigzag), colors_6)
  plot_group_bar_chart("PortNum", "bending", "bending_girvan_zigzag", groupNames, labelNames, np.transpose(bending_girvan_zigzag), colors_6)
  
  plot_group_bar_chart("PortNum", "length", "length_girvan_ascending", groupNames, labelNames, np.transpose(length_girvan_ascending), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "crossing_girvan_ascending", groupNames, labelNames, np.transpose(crossing_girvan_ascending), colors_6)
  plot_group_bar_chart("PortNum", "bending", "bending_girvan_ascending", groupNames, labelNames, np.transpose(bending_girvan_ascending), colors_6)
  
  plot_group_bar_chart("PortNum", "length", "length_girvan_localmin", groupNames, labelNames, np.transpose(length_girvan_localmin), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "crossing_girvan_localmin", groupNames, labelNames, np.transpose(crossing_girvan_localmin), colors_6)
  plot_group_bar_chart("PortNum", "bending", "bending_girvan_localmin", groupNames, labelNames, np.transpose(bending_girvan_localmin), colors_6)

  plot_group_bar_chart("PortNum", "length", "length_girvan_globalmin", groupNames, labelNames, np.transpose(length_girvan_globalmin), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "crossing_girvan_globalmin", groupNames, labelNames, np.transpose(crossing_girvan_globalmin), colors_6)
  plot_group_bar_chart("PortNum", "bending", "bending_girvan_globalmin", groupNames, labelNames, np.transpose(bending_girvan_globalmin), colors_6)
  

# draw_algorithm_layout("", "", data)