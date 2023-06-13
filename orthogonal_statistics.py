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
    
    ax.set_yscale('log')

    for i, group_data in enumerate(data):
      print(f'{i}: ', group_data, sep=' ')
      offset = bar_width * space
      ax.bar(x + offset, group_data, bar_width, alpha=opacity, label=labelNames[i], color=colors[i])
      space += 1.1

    # 축, 레이블, 범례, 제목 설정
    ax.set_xlabel(xTitle)
    ax.set_ylabel(yTitle)
    ax.set_title(chartName)
    ax.set_xticks(x + bar_width * 0.6 * (len(groupNames) - 1) / 2)
    ax.set_xticklabels(groupNames)
    ax.legend()

    plt.tight_layout()
    plt.show()

def mapping(list, key):
  ret = []
  for item in list:
    ret.append(item[key])
  return ret

# (0)
## Xticks: Vertex
## Y: Length, Crossing, Bending
## Group: Layout
## 인자: Algorithm, Port
def draw_algorithm_port(algorithm, port, data):
  groupNames = ["14", "30", "57", "118", "300", "1062"]
  labelNames = ["ascending", "zigzag", "local min", "global min"]

  # 데이터 분리
  # louvain
  ## 4port
  ### length
  louvain_4port_zigzag_length = mapping(data['louvain4'], "zig-zag")
  louvain_4port_ascending_length = mapping(data['louvain4'], "ascending")
  louvain_4port_localmin_length = mapping(data['louvain4'], "local_min")
  louvain_4port_globalmin_length = mapping(data['louvain4'], "global_min")   
  ### crossing
  louvain_4port_zigzag_crossing = mapping(data['louvain4'], "zig-zag2")
  louvain_4port_ascending_crossing = mapping(data['louvain4'], "ascending2")
  louvain_4port_localmin_crossing = mapping(data['louvain4'], "local_min2")  
  louvain_4port_globalmin_crossing = mapping(data['louvain4'], "global_min2")
  ### bending
  louvain_4port_zigzag_bending = mapping(data['louvain4'], "zig-zag3")
  louvain_4port_ascending_bending = mapping(data['louvain4'], "ascending3")
  louvain_4port_localmin_bending = mapping(data['louvain4'], "local_min3")  
  louvain_4port_globalmin_bending = mapping(data['louvain4'], "global_min3")
  
  ## 8port
  ### length
  louvain_8port_zigzag_length = mapping(data['louvain8'], "zig-zag")
  louvain_8port_ascending_length = mapping(data['louvain8'], "ascending")
  louvain_8port_localmin_length = mapping(data['louvain8'], "local_min")
  louvain_8port_globalmin_length = mapping(data['louvain8'], "global_min")   
  ### crossing
  louvain_8port_zigzag_crossing = mapping(data['louvain8'], "zig-zag2")
  louvain_8port_ascending_crossing = mapping(data['louvain8'], "ascending2")
  louvain_8port_localmin_crossing = mapping(data['louvain8'], "local_min2")  
  louvain_8port_globalmin_crossing = mapping(data['louvain8'], "global_min2")
  ### bending
  louvain_8port_zigzag_bending = mapping(data['louvain8'], "zig-zag3")
  louvain_8port_ascending_bending = mapping(data['louvain8'], "ascending3")
  louvain_8port_localmin_bending = mapping(data['louvain8'], "local_min3")  
  louvain_8port_globalmin_bending = mapping(data['louvain8'], "global_min3") 
  
  ## 12port
  ### length
  louvain_12port_zigzag_length = mapping(data['louvain12'], "zig-zag")
  louvain_12port_ascending_length = mapping(data['louvain12'], "ascending")
  louvain_12port_localmin_length = mapping(data['louvain12'], "local_min")
  louvain_12port_globalmin_length = mapping(data['louvain12'], "global_min")   
  ### crossing
  louvain_12port_zigzag_crossing = mapping(data['louvain12'], "zig-zag2")
  louvain_12port_ascending_crossing = mapping(data['louvain12'], "ascending2")
  louvain_12port_localmin_crossing = mapping(data['louvain12'], "local_min2")  
  louvain_12port_globalmin_crossing = mapping(data['louvain12'], "global_min2")
  ### bending
  louvain_12port_zigzag_bending = mapping(data['louvain12'], "zig-zag3")
  louvain_12port_ascending_bending = mapping(data['louvain12'], "ascending3")
  louvain_12port_localmin_bending = mapping(data['louvain12'], "local_min3")  
  louvain_12port_globalmin_bending = mapping(data['louvain12'], "global_min3") 
  
  # leiden
  ## 4port
  ### length
  leiden_4port_zigzag_length = mapping(data['leiden4'], "zig-zag")
  leiden_4port_ascending_length = mapping(data['leiden4'], "ascending")
  leiden_4port_localmin_length = mapping(data['leiden4'], "local_min")
  leiden_4port_globalmin_length = mapping(data['leiden4'], "global_min")   
  ### crossing
  leiden_4port_zigzag_crossing = mapping(data['leiden4'], "zig-zag2")
  leiden_4port_ascending_crossing = mapping(data['leiden4'], "ascending2")
  leiden_4port_localmin_crossing = mapping(data['leiden4'], "local_min2")  
  leiden_4port_globalmin_crossing = mapping(data['leiden4'], "global_min2")
  ### bending
  leiden_4port_zigzag_bending = mapping(data['leiden4'], "zig-zag3")
  leiden_4port_ascending_bending = mapping(data['leiden4'], "ascending3")
  leiden_4port_localmin_bending = mapping(data['leiden4'], "local_min3")  
  leiden_4port_globalmin_bending = mapping(data['leiden4'], "global_min3")
  
  ## 8port
  ### length
  leiden_8port_zigzag_length = mapping(data['leiden8'], "zig-zag")
  leiden_8port_ascending_length = mapping(data['leiden8'], "ascending")
  leiden_8port_localmin_length = mapping(data['leiden8'], "local_min")
  leiden_8port_globalmin_length = mapping(data['leiden8'], "global_min")   
  ### crossing
  leiden_8port_zigzag_crossing = mapping(data['leiden8'], "zig-zag2")
  leiden_8port_ascending_crossing = mapping(data['leiden8'], "ascending2")
  leiden_8port_localmin_crossing = mapping(data['leiden8'], "local_min2")  
  leiden_8port_globalmin_crossing = mapping(data['leiden8'], "global_min2")
  ### bending
  leiden_8port_zigzag_bending = mapping(data['leiden8'], "zig-zag3")
  leiden_8port_ascending_bending = mapping(data['leiden8'], "ascending3")
  leiden_8port_localmin_bending = mapping(data['leiden8'], "local_min3")  
  leiden_8port_globalmin_bending = mapping(data['leiden8'], "global_min3") 
  
  ## 12port
  ### length
  leiden_12port_zigzag_length = mapping(data['leiden12'], "zig-zag")
  leiden_12port_ascending_length = mapping(data['leiden12'], "ascending")
  leiden_12port_localmin_length = mapping(data['leiden12'], "local_min")
  leiden_12port_globalmin_length = mapping(data['leiden12'], "global_min")   
  ### crossing
  leiden_12port_zigzag_crossing = mapping(data['leiden12'], "zig-zag2")
  leiden_12port_ascending_crossing = mapping(data['leiden12'], "ascending2")
  leiden_12port_localmin_crossing = mapping(data['leiden12'], "local_min2")  
  leiden_12port_globalmin_crossing = mapping(data['leiden12'], "global_min2")
  ### bending
  leiden_12port_zigzag_bending = mapping(data['leiden12'], "zig-zag3")
  leiden_12port_ascending_bending = mapping(data['leiden12'], "ascending3")
  leiden_12port_localmin_bending = mapping(data['leiden12'], "local_min3")  
  leiden_12port_globalmin_bending = mapping(data['leiden12'], "global_min3")
  
  
  # girvan-newman
  ## 4port
  ### length
  girvan_4port_zigzag_length = mapping(data['girvan4'], "zig-zag")
  girvan_4port_ascending_length = mapping(data['girvan4'], "ascending")
  girvan_4port_localmin_length = mapping(data['girvan4'], "local_min")
  girvan_4port_globalmin_length = mapping(data['girvan4'], "global_min")   
  ### crossing
  girvan_4port_zigzag_crossing = mapping(data['girvan4'], "zig-zag2")
  girvan_4port_ascending_crossing = mapping(data['girvan4'], "ascending2")
  girvan_4port_localmin_crossing = mapping(data['girvan4'], "local_min2")  
  girvan_4port_globalmin_crossing = mapping(data['girvan4'], "global_min2")
  ### bending
  girvan_4port_zigzag_bending = mapping(data['girvan4'], "zig-zag3")
  girvan_4port_ascending_bending = mapping(data['girvan4'], "ascending3")
  girvan_4port_localmin_bending = mapping(data['girvan4'], "local_min3")  
  girvan_4port_globalmin_bending = mapping(data['girvan4'], "global_min3")
  
  ## 8port
  ### length
  girvan_8port_zigzag_length = mapping(data['girvan8'], "zig-zag")
  girvan_8port_ascending_length = mapping(data['girvan8'], "ascending")
  girvan_8port_localmin_length = mapping(data['girvan8'], "local_min")
  girvan_8port_globalmin_length = mapping(data['girvan8'], "global_min")   
  ### crossing
  girvan_8port_zigzag_crossing = mapping(data['girvan8'], "zig-zag2")
  girvan_8port_ascending_crossing = mapping(data['girvan8'], "ascending2")
  girvan_8port_localmin_crossing = mapping(data['girvan8'], "local_min2")  
  girvan_8port_globalmin_crossing = mapping(data['girvan8'], "global_min2")
  ### bending
  girvan_8port_zigzag_bending = mapping(data['girvan8'], "zig-zag3")
  girvan_8port_ascending_bending = mapping(data['girvan8'], "ascending3")
  girvan_8port_localmin_bending = mapping(data['girvan8'], "local_min3")  
  girvan_8port_globalmin_bending = mapping(data['girvan8'], "global_min3") 
  
  ## 12port
  ### length
  girvan_12port_zigzag_length = mapping(data['girvan12'], "zig-zag")
  girvan_12port_ascending_length = mapping(data['girvan12'], "ascending")
  girvan_12port_localmin_length = mapping(data['girvan12'], "local_min")
  girvan_12port_globalmin_length = mapping(data['girvan12'], "global_min")   
  ### crossing
  girvan_12port_zigzag_crossing = mapping(data['girvan12'], "zig-zag2")
  girvan_12port_ascending_crossing = mapping(data['girvan12'], "ascending2")
  girvan_12port_localmin_crossing = mapping(data['girvan12'], "local_min2")  
  girvan_12port_globalmin_crossing = mapping(data['girvan12'], "global_min2")
  ### bending
  girvan_12port_zigzag_bending = mapping(data['girvan12'], "zig-zag3")
  girvan_12port_ascending_bending = mapping(data['girvan12'], "ascending3")
  girvan_12port_localmin_bending = mapping(data['girvan12'], "local_min3")  
  girvan_12port_globalmin_bending = mapping(data['girvan12'], "global_min3")

  louvain_4port_v14_length = []
  louvain_4port_v30_length = []
  louvain_4port_v57_length = []
  louvain_4port_v118_length = []
  louvain_4port_v300_length = []
  louvain_4port_v1062_length = []
  louvain_4port_length = []
  louvain_4port_v14_length.extend([louvain_4port_zigzag_length[0], louvain_4port_ascending_length[0], louvain_4port_localmin_length[0], louvain_4port_globalmin_length[0]])
  louvain_4port_v30_length.extend([louvain_4port_zigzag_length[1], louvain_4port_ascending_length[1], louvain_4port_localmin_length[1], louvain_4port_globalmin_length[1]])
  louvain_4port_v57_length.extend([louvain_4port_zigzag_length[2], louvain_4port_ascending_length[2], louvain_4port_localmin_length[2], louvain_4port_globalmin_length[2]])
  louvain_4port_v118_length.extend([louvain_4port_zigzag_length[3], louvain_4port_ascending_length[3], louvain_4port_localmin_length[3], louvain_4port_globalmin_length[3]])
  louvain_4port_v300_length.extend([louvain_4port_zigzag_length[4], louvain_4port_ascending_length[4], louvain_4port_localmin_length[4], louvain_4port_globalmin_length[4]])
  louvain_4port_v1062_length.extend([louvain_4port_zigzag_length[5], louvain_4port_ascending_length[5], louvain_4port_localmin_length[5], louvain_4port_globalmin_length[5]])
  louvain_4port_length.extend([louvain_4port_v14_length, louvain_4port_v30_length, louvain_4port_v57_length,
                               louvain_4port_v118_length, louvain_4port_v300_length, louvain_4port_v1062_length])

  louvain_4port_v14_crossing = []
  louvain_4port_v30_crossing = []
  louvain_4port_v57_crossing = []
  louvain_4port_v118_crossing = []
  louvain_4port_v300_crossing = []
  louvain_4port_v1062_crossing = []
  louvain_4port_crossing = []
  louvain_4port_v14_crossing.extend([louvain_4port_zigzag_crossing[0], louvain_4port_ascending_crossing[0], louvain_4port_localmin_crossing[0], louvain_4port_globalmin_crossing[0]])
  louvain_4port_v30_crossing.extend([louvain_4port_zigzag_crossing[1], louvain_4port_ascending_crossing[1], louvain_4port_localmin_crossing[1], louvain_4port_globalmin_crossing[1]])
  louvain_4port_v57_crossing.extend([louvain_4port_zigzag_crossing[2], louvain_4port_ascending_crossing[2], louvain_4port_localmin_crossing[2], louvain_4port_globalmin_crossing[2]])
  louvain_4port_v118_crossing.extend([louvain_4port_zigzag_crossing[3], louvain_4port_ascending_crossing[3], louvain_4port_localmin_crossing[3], louvain_4port_globalmin_crossing[3]])
  louvain_4port_v300_crossing.extend([louvain_4port_zigzag_crossing[4], louvain_4port_ascending_crossing[4], louvain_4port_localmin_crossing[4], louvain_4port_globalmin_crossing[4]])
  louvain_4port_v1062_crossing.extend([louvain_4port_zigzag_crossing[5], louvain_4port_ascending_crossing[5], louvain_4port_localmin_crossing[5], louvain_4port_globalmin_crossing[5]])
  louvain_4port_crossing.extend([louvain_4port_v14_crossing, louvain_4port_v30_crossing, louvain_4port_v57_crossing,
                                 louvain_4port_v118_crossing, louvain_4port_v300_crossing, louvain_4port_v1062_crossing])

  louvain_4port_v14_bending = []
  louvain_4port_v30_bending = []
  louvain_4port_v57_bending = []
  louvain_4port_v118_bending = []
  louvain_4port_v300_bending = []
  louvain_4port_v1062_bending = []
  louvain_4port_bending = []
  louvain_4port_v14_bending.extend([louvain_4port_zigzag_bending[0], louvain_4port_ascending_bending[0], louvain_4port_localmin_bending[0], louvain_4port_globalmin_bending[0]])
  louvain_4port_v30_bending.extend([louvain_4port_zigzag_bending[1], louvain_4port_ascending_bending[1], louvain_4port_localmin_bending[1], louvain_4port_globalmin_bending[1]])
  louvain_4port_v57_bending.extend([louvain_4port_zigzag_bending[2], louvain_4port_ascending_bending[2], louvain_4port_localmin_bending[2], louvain_4port_globalmin_bending[2]])
  louvain_4port_v118_bending.extend([louvain_4port_zigzag_bending[3], louvain_4port_ascending_bending[3], louvain_4port_localmin_bending[3], louvain_4port_globalmin_bending[3]])
  louvain_4port_v300_bending.extend([louvain_4port_zigzag_bending[4], louvain_4port_ascending_bending[4], louvain_4port_localmin_bending[4], louvain_4port_globalmin_bending[4]])
  louvain_4port_v1062_bending.extend([louvain_4port_zigzag_bending[5], louvain_4port_ascending_bending[5], louvain_4port_localmin_bending[5], louvain_4port_globalmin_bending[5]])
  louvain_4port_bending.extend([louvain_4port_v14_bending, louvain_4port_v30_bending, louvain_4port_v57_bending,
                                louvain_4port_v118_bending, louvain_4port_v300_bending, louvain_4port_v1062_bending])

  louvain_8port_v14_length = []
  louvain_8port_v30_length = []
  louvain_8port_v57_length = []
  louvain_8port_v118_length = []
  louvain_8port_v300_length = []
  louvain_8port_v1062_length = []
  louvain_8port_length = []
  louvain_8port_v14_length.extend([louvain_8port_zigzag_length[0], louvain_8port_ascending_length[0], louvain_8port_localmin_length[0], louvain_8port_globalmin_length[0]])
  louvain_8port_v30_length.extend([louvain_8port_zigzag_length[1], louvain_8port_ascending_length[1], louvain_8port_localmin_length[1], louvain_8port_globalmin_length[1]])
  louvain_8port_v57_length.extend([louvain_8port_zigzag_length[2], louvain_8port_ascending_length[2], louvain_8port_localmin_length[2], louvain_8port_globalmin_length[2]])
  louvain_8port_v118_length.extend([louvain_8port_zigzag_length[3], louvain_8port_ascending_length[3], louvain_8port_localmin_length[3], louvain_8port_globalmin_length[3]])
  louvain_8port_v300_length.extend([louvain_8port_zigzag_length[4], louvain_8port_ascending_length[4], louvain_8port_localmin_length[4], louvain_8port_globalmin_length[4]])
  louvain_8port_v1062_length.extend([louvain_8port_zigzag_length[5], louvain_8port_ascending_length[5], louvain_8port_localmin_length[5], louvain_8port_globalmin_length[5]])
  louvain_8port_length.extend([louvain_8port_v14_length, louvain_8port_v30_length, louvain_8port_v57_length,
                               louvain_8port_v118_length, louvain_8port_v300_length, louvain_8port_v1062_length])

  louvain_8port_v14_crossing = []
  louvain_8port_v30_crossing = []
  louvain_8port_v57_crossing = []
  louvain_8port_v118_crossing = []
  louvain_8port_v300_crossing = []
  louvain_8port_v1062_crossing = []
  louvain_8port_crossing = []
  louvain_8port_v14_crossing.extend([louvain_8port_zigzag_crossing[0], louvain_8port_ascending_crossing[0], louvain_8port_localmin_crossing[0], louvain_8port_globalmin_crossing[0]])
  louvain_8port_v30_crossing.extend([louvain_8port_zigzag_crossing[1], louvain_8port_ascending_crossing[1], louvain_8port_localmin_crossing[1], louvain_8port_globalmin_crossing[1]])
  louvain_8port_v57_crossing.extend([louvain_8port_zigzag_crossing[2], louvain_8port_ascending_crossing[2], louvain_8port_localmin_crossing[2], louvain_8port_globalmin_crossing[2]])
  louvain_8port_v118_crossing.extend([louvain_8port_zigzag_crossing[3], louvain_8port_ascending_crossing[3], louvain_8port_localmin_crossing[3], louvain_8port_globalmin_crossing[3]])
  louvain_8port_v300_crossing.extend([louvain_8port_zigzag_crossing[4], louvain_8port_ascending_crossing[4], louvain_8port_localmin_crossing[4], louvain_8port_globalmin_crossing[4]])
  louvain_8port_v1062_crossing.extend([louvain_8port_zigzag_crossing[5], louvain_8port_ascending_crossing[5], louvain_8port_localmin_crossing[5], louvain_8port_globalmin_crossing[5]])
  louvain_8port_crossing.extend([louvain_8port_v14_crossing, louvain_8port_v30_crossing, louvain_8port_v57_crossing,
                                 louvain_8port_v118_crossing, louvain_8port_v300_crossing, louvain_8port_v1062_crossing])

  louvain_8port_v14_bending = []
  louvain_8port_v30_bending = []
  louvain_8port_v57_bending = []
  louvain_8port_v118_bending = []
  louvain_8port_v300_bending = []
  louvain_8port_v1062_bending = []
  louvain_8port_bending = []
  louvain_8port_v14_bending.extend([louvain_8port_zigzag_bending[0], louvain_8port_ascending_bending[0], louvain_8port_localmin_bending[0], louvain_8port_globalmin_bending[0]])
  louvain_8port_v30_bending.extend([louvain_8port_zigzag_bending[1], louvain_8port_ascending_bending[1], louvain_8port_localmin_bending[1], louvain_8port_globalmin_bending[1]])
  louvain_8port_v57_bending.extend([louvain_8port_zigzag_bending[2], louvain_8port_ascending_bending[2], louvain_8port_localmin_bending[2], louvain_8port_globalmin_bending[2]])
  louvain_8port_v118_bending.extend([louvain_8port_zigzag_bending[3], louvain_8port_ascending_bending[3], louvain_8port_localmin_bending[3], louvain_8port_globalmin_bending[3]])
  louvain_8port_v300_bending.extend([louvain_8port_zigzag_bending[4], louvain_8port_ascending_bending[4], louvain_8port_localmin_bending[4], louvain_8port_globalmin_bending[4]])
  louvain_8port_v1062_bending.extend([louvain_8port_zigzag_bending[5], louvain_8port_ascending_bending[5], louvain_8port_localmin_bending[5], louvain_8port_globalmin_bending[5]])
  louvain_8port_bending.extend([louvain_8port_v14_bending, louvain_8port_v30_bending, louvain_8port_v57_bending,
                                louvain_8port_v118_bending, louvain_8port_v300_bending, louvain_8port_v1062_bending])

  louvain_12port_v14_length = []
  louvain_12port_v30_length = []
  louvain_12port_v57_length = []
  louvain_12port_v118_length = []
  louvain_12port_v300_length = []
  louvain_12port_v1062_length = []
  louvain_12port_length = []
  louvain_12port_v14_length.extend([louvain_12port_zigzag_length[0], louvain_12port_ascending_length[0], louvain_12port_localmin_length[0], louvain_12port_globalmin_length[0]])
  louvain_12port_v30_length.extend([louvain_12port_zigzag_length[1], louvain_12port_ascending_length[1], louvain_12port_localmin_length[1], louvain_12port_globalmin_length[1]])
  louvain_12port_v57_length.extend([louvain_12port_zigzag_length[2], louvain_12port_ascending_length[2], louvain_12port_localmin_length[2], louvain_12port_globalmin_length[2]])
  louvain_12port_v118_length.extend([louvain_12port_zigzag_length[3], louvain_12port_ascending_length[3], louvain_12port_localmin_length[3], louvain_12port_globalmin_length[3]])
  louvain_12port_v300_length.extend([louvain_12port_zigzag_length[4], louvain_12port_ascending_length[4], louvain_12port_localmin_length[4], louvain_12port_globalmin_length[4]])
  louvain_12port_v1062_length.extend([louvain_12port_zigzag_length[5], louvain_12port_ascending_length[5], louvain_12port_localmin_length[5], louvain_12port_globalmin_length[5]])
  louvain_12port_length.extend([louvain_12port_v14_length, louvain_12port_v30_length, louvain_12port_v57_length,
                                louvain_12port_v118_length, louvain_12port_v300_length, louvain_12port_v1062_length])

  louvain_12port_v14_crossing = []
  louvain_12port_v30_crossing = []
  louvain_12port_v57_crossing = []
  louvain_12port_v118_crossing = []
  louvain_12port_v300_crossing = []
  louvain_12port_v1062_crossing = []
  louvain_12port_crossing = []
  louvain_12port_v14_crossing.extend([louvain_12port_zigzag_crossing[0], louvain_12port_ascending_crossing[0], louvain_12port_localmin_crossing[0], louvain_12port_globalmin_crossing[0]])
  louvain_12port_v30_crossing.extend([louvain_12port_zigzag_crossing[1], louvain_12port_ascending_crossing[1], louvain_12port_localmin_crossing[1], louvain_12port_globalmin_crossing[1]])
  louvain_12port_v57_crossing.extend([louvain_12port_zigzag_crossing[2], louvain_12port_ascending_crossing[2], louvain_12port_localmin_crossing[2], louvain_12port_globalmin_crossing[2]])
  louvain_12port_v118_crossing.extend([louvain_12port_zigzag_crossing[3], louvain_12port_ascending_crossing[3], louvain_12port_localmin_crossing[3], louvain_12port_globalmin_crossing[3]])
  louvain_12port_v300_crossing.extend([louvain_12port_zigzag_crossing[4], louvain_12port_ascending_crossing[4], louvain_12port_localmin_crossing[4], louvain_12port_globalmin_crossing[4]])
  louvain_12port_v1062_crossing.extend([louvain_12port_zigzag_crossing[5], louvain_12port_ascending_crossing[5], louvain_12port_localmin_crossing[5], louvain_12port_globalmin_crossing[5]])
  louvain_12port_crossing.extend([louvain_12port_v14_crossing, louvain_12port_v30_crossing, louvain_12port_v57_crossing,
                                  louvain_12port_v118_crossing, louvain_12port_v300_crossing, louvain_12port_v1062_crossing])

  louvain_12port_v14_bending = []
  louvain_12port_v30_bending = []
  louvain_12port_v57_bending = []
  louvain_12port_v118_bending = []
  louvain_12port_v300_bending = []
  louvain_12port_v1062_bending = []
  louvain_12port_bending = []
  louvain_12port_v14_bending.extend([louvain_12port_zigzag_bending[0], louvain_12port_ascending_bending[0], louvain_12port_localmin_bending[0], louvain_12port_globalmin_bending[0]])
  louvain_12port_v30_bending.extend([louvain_12port_zigzag_bending[1], louvain_12port_ascending_bending[1], louvain_12port_localmin_bending[1], louvain_12port_globalmin_bending[1]])
  louvain_12port_v57_bending.extend([louvain_12port_zigzag_bending[2], louvain_12port_ascending_bending[2], louvain_12port_localmin_bending[2], louvain_12port_globalmin_bending[2]])
  louvain_12port_v118_bending.extend([louvain_12port_zigzag_bending[3], louvain_12port_ascending_bending[3], louvain_12port_localmin_bending[3], louvain_12port_globalmin_bending[3]])
  louvain_12port_v300_bending.extend([louvain_12port_zigzag_bending[4], louvain_12port_ascending_bending[4], louvain_12port_localmin_bending[4], louvain_12port_globalmin_bending[4]])
  louvain_12port_v1062_bending.extend([louvain_12port_zigzag_bending[5], louvain_12port_ascending_bending[5], louvain_12port_localmin_bending[5], louvain_12port_globalmin_bending[5]])
  louvain_12port_bending.extend([louvain_12port_v14_bending, louvain_12port_v30_bending, louvain_12port_v57_bending,
                                 louvain_12port_v118_bending, louvain_12port_v300_bending, louvain_12port_v1062_bending])

  leiden_4port_v14_length = []
  leiden_4port_v30_length = []
  leiden_4port_v57_length = []
  leiden_4port_v118_length = []
  leiden_4port_v300_length = []
  leiden_4port_v1062_length = []
  leiden_4port_length = []
  leiden_4port_v14_length.extend([leiden_4port_zigzag_length[0], leiden_4port_ascending_length[0], leiden_4port_localmin_length[0], leiden_4port_globalmin_length[0]])
  leiden_4port_v30_length.extend([leiden_4port_zigzag_length[1], leiden_4port_ascending_length[1], leiden_4port_localmin_length[1], leiden_4port_globalmin_length[1]])
  leiden_4port_v57_length.extend([leiden_4port_zigzag_length[2], leiden_4port_ascending_length[2], leiden_4port_localmin_length[2], leiden_4port_globalmin_length[2]])
  leiden_4port_v118_length.extend([leiden_4port_zigzag_length[3], leiden_4port_ascending_length[3], leiden_4port_localmin_length[3], leiden_4port_globalmin_length[3]])
  leiden_4port_v300_length.extend([leiden_4port_zigzag_length[4], leiden_4port_ascending_length[4], leiden_4port_localmin_length[4], leiden_4port_globalmin_length[4]])
  leiden_4port_v1062_length.extend([leiden_4port_zigzag_length[5], leiden_4port_ascending_length[5], leiden_4port_localmin_length[5], leiden_4port_globalmin_length[5]])
  leiden_4port_length.extend([leiden_4port_v14_length, leiden_4port_v30_length, leiden_4port_v57_length,
                              leiden_4port_v118_length, leiden_4port_v300_length, leiden_4port_v1062_length])

  leiden_4port_v14_crossing = []
  leiden_4port_v30_crossing = []
  leiden_4port_v57_crossing = []
  leiden_4port_v118_crossing = []
  leiden_4port_v300_crossing = []
  leiden_4port_v1062_crossing = []
  leiden_4port_crossing = []
  leiden_4port_v14_crossing.extend([leiden_4port_zigzag_crossing[0], leiden_4port_ascending_crossing[0], leiden_4port_localmin_crossing[0], leiden_4port_globalmin_crossing[0]])
  leiden_4port_v30_crossing.extend([leiden_4port_zigzag_crossing[1], leiden_4port_ascending_crossing[1], leiden_4port_localmin_crossing[1], leiden_4port_globalmin_crossing[1]])
  leiden_4port_v57_crossing.extend([leiden_4port_zigzag_crossing[2], leiden_4port_ascending_crossing[2], leiden_4port_localmin_crossing[2], leiden_4port_globalmin_crossing[2]])
  leiden_4port_v118_crossing.extend([leiden_4port_zigzag_crossing[3], leiden_4port_ascending_crossing[3], leiden_4port_localmin_crossing[3], leiden_4port_globalmin_crossing[3]])
  leiden_4port_v300_crossing.extend([leiden_4port_zigzag_crossing[4], leiden_4port_ascending_crossing[4], leiden_4port_localmin_crossing[4], leiden_4port_globalmin_crossing[4]])
  leiden_4port_v1062_crossing.extend([leiden_4port_zigzag_crossing[5], leiden_4port_ascending_crossing[5], leiden_4port_localmin_crossing[5], leiden_4port_globalmin_crossing[5]])
  leiden_4port_crossing.extend([leiden_4port_v14_crossing, leiden_4port_v30_crossing, leiden_4port_v57_crossing,
                                leiden_4port_v118_crossing, leiden_4port_v300_crossing, leiden_4port_v1062_crossing])

  leiden_4port_v14_bending = []
  leiden_4port_v30_bending = []
  leiden_4port_v57_bending = []
  leiden_4port_v118_bending = []
  leiden_4port_v300_bending = []
  leiden_4port_v1062_bending = []
  leiden_4port_bending = []
  leiden_4port_v14_bending.extend([leiden_4port_zigzag_bending[0], leiden_4port_ascending_bending[0], leiden_4port_localmin_bending[0], leiden_4port_globalmin_bending[0]])
  leiden_4port_v30_bending.extend([leiden_4port_zigzag_bending[1], leiden_4port_ascending_bending[1], leiden_4port_localmin_bending[1], leiden_4port_globalmin_bending[1]])
  leiden_4port_v57_bending.extend([leiden_4port_zigzag_bending[2], leiden_4port_ascending_bending[2], leiden_4port_localmin_bending[2], leiden_4port_globalmin_bending[2]])
  leiden_4port_v118_bending.extend([leiden_4port_zigzag_bending[3], leiden_4port_ascending_bending[3], leiden_4port_localmin_bending[3], leiden_4port_globalmin_bending[3]])
  leiden_4port_v300_bending.extend([leiden_4port_zigzag_bending[4], leiden_4port_ascending_bending[4], leiden_4port_localmin_bending[4], leiden_4port_globalmin_bending[4]])
  leiden_4port_v1062_bending.extend([leiden_4port_zigzag_bending[5], leiden_4port_ascending_bending[5], leiden_4port_localmin_bending[5], leiden_4port_globalmin_bending[5]])
  leiden_4port_bending.extend([leiden_4port_v14_bending, leiden_4port_v30_bending, leiden_4port_v57_bending,
                               leiden_4port_v118_bending, leiden_4port_v300_bending, leiden_4port_v1062_bending])

  leiden_8port_v14_length = []
  leiden_8port_v30_length = []
  leiden_8port_v57_length = []
  leiden_8port_v118_length = []
  leiden_8port_v300_length = []
  leiden_8port_v1062_length = []
  leiden_8port_length = []
  leiden_8port_v14_length.extend([leiden_8port_zigzag_length[0], leiden_8port_ascending_length[0], leiden_8port_localmin_length[0], leiden_8port_globalmin_length[0]])
  leiden_8port_v30_length.extend([leiden_8port_zigzag_length[1], leiden_8port_ascending_length[1], leiden_8port_localmin_length[1], leiden_8port_globalmin_length[1]])
  leiden_8port_v57_length.extend([leiden_8port_zigzag_length[2], leiden_8port_ascending_length[2], leiden_8port_localmin_length[2], leiden_8port_globalmin_length[2]])
  leiden_8port_v118_length.extend([leiden_8port_zigzag_length[3], leiden_8port_ascending_length[3], leiden_8port_localmin_length[3], leiden_8port_globalmin_length[3]])
  leiden_8port_v300_length.extend([leiden_8port_zigzag_length[4], leiden_8port_ascending_length[4], leiden_8port_localmin_length[4], leiden_8port_globalmin_length[4]])
  leiden_8port_v1062_length.extend([leiden_8port_zigzag_length[5], leiden_8port_ascending_length[5], leiden_8port_localmin_length[5], leiden_8port_globalmin_length[5]])
  leiden_8port_length.extend([leiden_8port_v14_length, leiden_8port_v30_length, leiden_8port_v57_length,
                              leiden_8port_v118_length, leiden_8port_v300_length, leiden_8port_v1062_length])

  leiden_8port_v14_crossing = []
  leiden_8port_v30_crossing = []
  leiden_8port_v57_crossing = []
  leiden_8port_v118_crossing = []
  leiden_8port_v300_crossing = []
  leiden_8port_v1062_crossing = []
  leiden_8port_crossing = []
  leiden_8port_v14_crossing.extend([leiden_8port_zigzag_crossing[0], leiden_8port_ascending_crossing[0], leiden_8port_localmin_crossing[0], leiden_8port_globalmin_crossing[0]])
  leiden_8port_v30_crossing.extend([leiden_8port_zigzag_crossing[1], leiden_8port_ascending_crossing[1], leiden_8port_localmin_crossing[1], leiden_8port_globalmin_crossing[1]])
  leiden_8port_v57_crossing.extend([leiden_8port_zigzag_crossing[2], leiden_8port_ascending_crossing[2], leiden_8port_localmin_crossing[2], leiden_8port_globalmin_crossing[2]])
  leiden_8port_v118_crossing.extend([leiden_8port_zigzag_crossing[3], leiden_8port_ascending_crossing[3], leiden_8port_localmin_crossing[3], leiden_8port_globalmin_crossing[3]])
  leiden_8port_v300_crossing.extend([leiden_8port_zigzag_crossing[4], leiden_8port_ascending_crossing[4], leiden_8port_localmin_crossing[4], leiden_8port_globalmin_crossing[4]])
  leiden_8port_v1062_crossing.extend([leiden_8port_zigzag_crossing[5], leiden_8port_ascending_crossing[5], leiden_8port_localmin_crossing[5], leiden_8port_globalmin_crossing[5]])
  leiden_8port_crossing.extend([leiden_8port_v14_crossing, leiden_8port_v30_crossing, leiden_8port_v57_crossing,
                                leiden_8port_v118_crossing, leiden_8port_v300_crossing, leiden_8port_v1062_crossing])

  leiden_8port_v14_bending = []
  leiden_8port_v30_bending = []
  leiden_8port_v57_bending = []
  leiden_8port_v118_bending = []
  leiden_8port_v300_bending = []
  leiden_8port_v1062_bending = []
  leiden_8port_bending = []
  leiden_8port_v14_bending.extend([leiden_8port_zigzag_bending[0], leiden_8port_ascending_bending[0], leiden_8port_localmin_bending[0], leiden_8port_globalmin_bending[0]])
  leiden_8port_v30_bending.extend([leiden_8port_zigzag_bending[1], leiden_8port_ascending_bending[1], leiden_8port_localmin_bending[1], leiden_8port_globalmin_bending[1]])
  leiden_8port_v57_bending.extend([leiden_8port_zigzag_bending[2], leiden_8port_ascending_bending[2], leiden_8port_localmin_bending[2], leiden_8port_globalmin_bending[2]])
  leiden_8port_v118_bending.extend([leiden_8port_zigzag_bending[3], leiden_8port_ascending_bending[3], leiden_8port_localmin_bending[3], leiden_8port_globalmin_bending[3]])
  leiden_8port_v300_bending.extend([leiden_8port_zigzag_bending[4], leiden_8port_ascending_bending[4], leiden_8port_localmin_bending[4], leiden_8port_globalmin_bending[4]])
  leiden_8port_v1062_bending.extend([leiden_8port_zigzag_bending[5], leiden_8port_ascending_bending[5], leiden_8port_localmin_bending[5], leiden_8port_globalmin_bending[5]])
  leiden_8port_bending.extend([leiden_8port_v14_bending, leiden_8port_v30_bending, leiden_8port_v57_bending,
                               leiden_8port_v118_bending, leiden_8port_v300_bending, leiden_8port_v1062_bending])

  leiden_12port_v14_length = []
  leiden_12port_v30_length = []
  leiden_12port_v57_length = []
  leiden_12port_v118_length = []
  leiden_12port_v300_length = []
  leiden_12port_v1062_length = []
  leiden_12port_length = []
  leiden_12port_v14_length.extend([leiden_12port_zigzag_length[0], leiden_12port_ascending_length[0], leiden_12port_localmin_length[0], leiden_12port_globalmin_length[0]])
  leiden_12port_v30_length.extend([leiden_12port_zigzag_length[1], leiden_12port_ascending_length[1], leiden_12port_localmin_length[1], leiden_12port_globalmin_length[1]])
  leiden_12port_v57_length.extend([leiden_12port_zigzag_length[2], leiden_12port_ascending_length[2], leiden_12port_localmin_length[2], leiden_12port_globalmin_length[2]])
  leiden_12port_v118_length.extend([leiden_12port_zigzag_length[3], leiden_12port_ascending_length[3], leiden_12port_localmin_length[3], leiden_12port_globalmin_length[3]])
  leiden_12port_v300_length.extend([leiden_12port_zigzag_length[4], leiden_12port_ascending_length[4], leiden_12port_localmin_length[4], leiden_12port_globalmin_length[4]])
  leiden_12port_v1062_length.extend([leiden_12port_zigzag_length[5], leiden_12port_ascending_length[5], leiden_12port_localmin_length[5], leiden_12port_globalmin_length[5]])
  leiden_12port_length.extend([leiden_12port_v14_length, leiden_12port_v30_length, leiden_12port_v57_length,
                               leiden_12port_v118_length, leiden_12port_v300_length, leiden_12port_v1062_length])

  leiden_12port_v14_crossing = []
  leiden_12port_v30_crossing = []
  leiden_12port_v57_crossing = []
  leiden_12port_v118_crossing = []
  leiden_12port_v300_crossing = []
  leiden_12port_v1062_crossing = []
  leiden_12port_crossing = []
  leiden_12port_v14_crossing.extend([leiden_12port_zigzag_crossing[0], leiden_12port_ascending_crossing[0], leiden_12port_localmin_crossing[0], leiden_12port_globalmin_crossing[0]])
  leiden_12port_v30_crossing.extend([leiden_12port_zigzag_crossing[1], leiden_12port_ascending_crossing[1], leiden_12port_localmin_crossing[1], leiden_12port_globalmin_crossing[1]])
  leiden_12port_v57_crossing.extend([leiden_12port_zigzag_crossing[2], leiden_12port_ascending_crossing[2], leiden_12port_localmin_crossing[2], leiden_12port_globalmin_crossing[2]])
  leiden_12port_v118_crossing.extend([leiden_12port_zigzag_crossing[3], leiden_12port_ascending_crossing[3], leiden_12port_localmin_crossing[3], leiden_12port_globalmin_crossing[3]])
  leiden_12port_v300_crossing.extend([leiden_12port_zigzag_crossing[4], leiden_12port_ascending_crossing[4], leiden_12port_localmin_crossing[4], leiden_12port_globalmin_crossing[4]])
  leiden_12port_v1062_crossing.extend([leiden_12port_zigzag_crossing[5], leiden_12port_ascending_crossing[5], leiden_12port_localmin_crossing[5], leiden_12port_globalmin_crossing[5]])
  leiden_12port_crossing.extend([leiden_12port_v14_crossing, leiden_12port_v30_crossing, leiden_12port_v57_crossing,
                                 leiden_12port_v118_crossing, leiden_12port_v300_crossing, leiden_12port_v1062_crossing])

  leiden_12port_v14_bending = []
  leiden_12port_v30_bending = []
  leiden_12port_v57_bending = []
  leiden_12port_v118_bending = []
  leiden_12port_v300_bending = []
  leiden_12port_v1062_bending = []
  leiden_12port_bending = []
  leiden_12port_v14_bending.extend([leiden_12port_zigzag_bending[0], leiden_12port_ascending_bending[0], leiden_12port_localmin_bending[0], leiden_12port_globalmin_bending[0]])
  leiden_12port_v30_bending.extend([leiden_12port_zigzag_bending[1], leiden_12port_ascending_bending[1], leiden_12port_localmin_bending[1], leiden_12port_globalmin_bending[1]])
  leiden_12port_v57_bending.extend([leiden_12port_zigzag_bending[2], leiden_12port_ascending_bending[2], leiden_12port_localmin_bending[2], leiden_12port_globalmin_bending[2]])
  leiden_12port_v118_bending.extend([leiden_12port_zigzag_bending[3], leiden_12port_ascending_bending[3], leiden_12port_localmin_bending[3], leiden_12port_globalmin_bending[3]])
  leiden_12port_v300_bending.extend([leiden_12port_zigzag_bending[4], leiden_12port_ascending_bending[4], leiden_12port_localmin_bending[4], leiden_12port_globalmin_bending[4]])
  leiden_12port_v1062_bending.extend([leiden_12port_zigzag_bending[5], leiden_12port_ascending_bending[5], leiden_12port_localmin_bending[5], leiden_12port_globalmin_bending[5]])
  leiden_12port_bending.extend([leiden_12port_v14_bending, leiden_12port_v30_bending, leiden_12port_v57_bending,
                                leiden_12port_v118_bending, leiden_12port_v300_bending, leiden_12port_v1062_bending])

  girvan_4port_v14_length = []
  girvan_4port_v30_length = []
  girvan_4port_v57_length = []
  girvan_4port_v118_length = []
  girvan_4port_v300_length = []
  girvan_4port_v1062_length = []
  girvan_4port_length = []
  girvan_4port_v14_length.extend([girvan_4port_zigzag_length[0], girvan_4port_ascending_length[0], girvan_4port_localmin_length[0], girvan_4port_globalmin_length[0]])
  girvan_4port_v30_length.extend([girvan_4port_zigzag_length[1], girvan_4port_ascending_length[1], girvan_4port_localmin_length[1], girvan_4port_globalmin_length[1]])
  girvan_4port_v57_length.extend([girvan_4port_zigzag_length[2], girvan_4port_ascending_length[2], girvan_4port_localmin_length[2], girvan_4port_globalmin_length[2]])
  girvan_4port_v118_length.extend([girvan_4port_zigzag_length[3], girvan_4port_ascending_length[3], girvan_4port_localmin_length[3], girvan_4port_globalmin_length[3]])
  girvan_4port_v300_length.extend([girvan_4port_zigzag_length[4], girvan_4port_ascending_length[4], girvan_4port_localmin_length[4], girvan_4port_globalmin_length[4]])
  girvan_4port_v1062_length.extend([girvan_4port_zigzag_length[5], girvan_4port_ascending_length[5], girvan_4port_localmin_length[5], girvan_4port_globalmin_length[5]])
  girvan_4port_length.extend([girvan_4port_v14_length, girvan_4port_v30_length, girvan_4port_v57_length,
                              girvan_4port_v118_length, girvan_4port_v300_length, girvan_4port_v1062_length])

  girvan_4port_v14_crossing = []
  girvan_4port_v30_crossing = []
  girvan_4port_v57_crossing = []
  girvan_4port_v118_crossing = []
  girvan_4port_v300_crossing = []
  girvan_4port_v1062_crossing = []
  girvan_4port_crossing = []
  girvan_4port_v14_crossing.extend([girvan_4port_zigzag_crossing[0], girvan_4port_ascending_crossing[0], girvan_4port_localmin_crossing[0], girvan_4port_globalmin_crossing[0]])
  girvan_4port_v30_crossing.extend([girvan_4port_zigzag_crossing[1], girvan_4port_ascending_crossing[1], girvan_4port_localmin_crossing[1], girvan_4port_globalmin_crossing[1]])
  girvan_4port_v57_crossing.extend([girvan_4port_zigzag_crossing[2], girvan_4port_ascending_crossing[2], girvan_4port_localmin_crossing[2], girvan_4port_globalmin_crossing[2]])
  girvan_4port_v118_crossing.extend([girvan_4port_zigzag_crossing[3], girvan_4port_ascending_crossing[3], girvan_4port_localmin_crossing[3], girvan_4port_globalmin_crossing[3]])
  girvan_4port_v300_crossing.extend([girvan_4port_zigzag_crossing[4], girvan_4port_ascending_crossing[4], girvan_4port_localmin_crossing[4], girvan_4port_globalmin_crossing[4]])
  girvan_4port_v1062_crossing.extend([girvan_4port_zigzag_crossing[5], girvan_4port_ascending_crossing[5], girvan_4port_localmin_crossing[5], girvan_4port_globalmin_crossing[5]])
  girvan_4port_crossing.extend([girvan_4port_v14_crossing, girvan_4port_v30_crossing, girvan_4port_v57_crossing,
                                girvan_4port_v118_crossing, girvan_4port_v300_crossing, girvan_4port_v1062_crossing])

  girvan_4port_v14_bending = []
  girvan_4port_v30_bending = []
  girvan_4port_v57_bending = []
  girvan_4port_v118_bending = []
  girvan_4port_v300_bending = []
  girvan_4port_v1062_bending = []
  girvan_4port_bending = []
  girvan_4port_v14_bending.extend([girvan_4port_zigzag_bending[0], girvan_4port_ascending_bending[0], girvan_4port_localmin_bending[0], girvan_4port_globalmin_bending[0]])
  girvan_4port_v30_bending.extend([girvan_4port_zigzag_bending[1], girvan_4port_ascending_bending[1], girvan_4port_localmin_bending[1], girvan_4port_globalmin_bending[1]])
  girvan_4port_v57_bending.extend([girvan_4port_zigzag_bending[2], girvan_4port_ascending_bending[2], girvan_4port_localmin_bending[2], girvan_4port_globalmin_bending[2]])
  girvan_4port_v118_bending.extend([girvan_4port_zigzag_bending[3], girvan_4port_ascending_bending[3], girvan_4port_localmin_bending[3], girvan_4port_globalmin_bending[3]])
  girvan_4port_v300_bending.extend([girvan_4port_zigzag_bending[4], girvan_4port_ascending_bending[4], girvan_4port_localmin_bending[4], girvan_4port_globalmin_bending[4]])
  girvan_4port_v1062_bending.extend([girvan_4port_zigzag_bending[5], girvan_4port_ascending_bending[5], girvan_4port_localmin_bending[5], girvan_4port_globalmin_bending[5]])
  girvan_4port_bending.extend([girvan_4port_v14_bending, girvan_4port_v30_bending, girvan_4port_v57_bending,
                               girvan_4port_v118_bending, girvan_4port_v300_bending, girvan_4port_v1062_bending])

  girvan_8port_v14_length = []
  girvan_8port_v30_length = []
  girvan_8port_v57_length = []
  girvan_8port_v118_length = []
  girvan_8port_v300_length = []
  girvan_8port_v1062_length = []
  girvan_8port_length = []
  girvan_8port_v14_length.extend([girvan_8port_zigzag_length[0], girvan_8port_ascending_length[0], girvan_8port_localmin_length[0], girvan_8port_globalmin_length[0]])
  girvan_8port_v30_length.extend([girvan_8port_zigzag_length[1], girvan_8port_ascending_length[1], girvan_8port_localmin_length[1], girvan_8port_globalmin_length[1]])
  girvan_8port_v57_length.extend([girvan_8port_zigzag_length[2], girvan_8port_ascending_length[2], girvan_8port_localmin_length[2], girvan_8port_globalmin_length[2]])
  girvan_8port_v118_length.extend([girvan_8port_zigzag_length[3], girvan_8port_ascending_length[3], girvan_8port_localmin_length[3], girvan_8port_globalmin_length[3]])
  girvan_8port_v300_length.extend([girvan_8port_zigzag_length[4], girvan_8port_ascending_length[4], girvan_8port_localmin_length[4], girvan_8port_globalmin_length[4]])
  girvan_8port_v1062_length.extend([girvan_8port_zigzag_length[5], girvan_8port_ascending_length[5], girvan_8port_localmin_length[5], girvan_8port_globalmin_length[5]])
  girvan_8port_length.extend([girvan_8port_v14_length, girvan_8port_v30_length, girvan_8port_v57_length,
                              girvan_8port_v118_length, girvan_8port_v300_length, girvan_8port_v1062_length])

  girvan_8port_v14_crossing = []
  girvan_8port_v30_crossing = []
  girvan_8port_v57_crossing = []
  girvan_8port_v118_crossing = []
  girvan_8port_v300_crossing = []
  girvan_8port_v1062_crossing = []
  girvan_8port_crossing = []
  girvan_8port_v14_crossing.extend([girvan_8port_zigzag_crossing[0], girvan_8port_ascending_crossing[0], girvan_8port_localmin_crossing[0], girvan_8port_globalmin_crossing[0]])
  girvan_8port_v30_crossing.extend([girvan_8port_zigzag_crossing[1], girvan_8port_ascending_crossing[1], girvan_8port_localmin_crossing[1], girvan_8port_globalmin_crossing[1]])
  girvan_8port_v57_crossing.extend([girvan_8port_zigzag_crossing[2], girvan_8port_ascending_crossing[2], girvan_8port_localmin_crossing[2], girvan_8port_globalmin_crossing[2]])
  girvan_8port_v118_crossing.extend([girvan_8port_zigzag_crossing[3], girvan_8port_ascending_crossing[3], girvan_8port_localmin_crossing[3], girvan_8port_globalmin_crossing[3]])
  girvan_8port_v300_crossing.extend([girvan_8port_zigzag_crossing[4], girvan_8port_ascending_crossing[4], girvan_8port_localmin_crossing[4], girvan_8port_globalmin_crossing[4]])
  girvan_8port_v1062_crossing.extend([girvan_8port_zigzag_crossing[5], girvan_8port_ascending_crossing[5], girvan_8port_localmin_crossing[5], girvan_8port_globalmin_crossing[5]])
  girvan_8port_crossing.extend([girvan_8port_v14_crossing, girvan_8port_v30_crossing, girvan_8port_v57_crossing,
                                girvan_8port_v118_crossing, girvan_8port_v300_crossing, girvan_8port_v1062_crossing])

  girvan_8port_v14_bending = []
  girvan_8port_v30_bending = []
  girvan_8port_v57_bending = []
  girvan_8port_v118_bending = []
  girvan_8port_v300_bending = []
  girvan_8port_v1062_bending = []
  girvan_8port_bending = []
  girvan_8port_v14_bending.extend([girvan_8port_zigzag_bending[0], girvan_8port_ascending_bending[0], girvan_8port_localmin_bending[0], girvan_8port_globalmin_bending[0]])
  girvan_8port_v30_bending.extend([girvan_8port_zigzag_bending[1], girvan_8port_ascending_bending[1], girvan_8port_localmin_bending[1], girvan_8port_globalmin_bending[1]])
  girvan_8port_v57_bending.extend([girvan_8port_zigzag_bending[2], girvan_8port_ascending_bending[2], girvan_8port_localmin_bending[2], girvan_8port_globalmin_bending[2]])
  girvan_8port_v118_bending.extend([girvan_8port_zigzag_bending[3], girvan_8port_ascending_bending[3], girvan_8port_localmin_bending[3], girvan_8port_globalmin_bending[3]])
  girvan_8port_v300_bending.extend([girvan_8port_zigzag_bending[4], girvan_8port_ascending_bending[4], girvan_8port_localmin_bending[4], girvan_8port_globalmin_bending[4]])
  girvan_8port_v1062_bending.extend([girvan_8port_zigzag_bending[5], girvan_8port_ascending_bending[5], girvan_8port_localmin_bending[5], girvan_8port_globalmin_bending[5]])
  girvan_8port_bending.extend([girvan_8port_v14_bending, girvan_8port_v30_bending, girvan_8port_v57_bending,
                               girvan_8port_v118_bending, girvan_8port_v300_bending, girvan_8port_v1062_bending])

  girvan_12port_v14_length = []
  girvan_12port_v30_length = []
  girvan_12port_v57_length = []
  girvan_12port_v118_length = []
  girvan_12port_v300_length = []
  girvan_12port_v1062_length = []
  girvan_12port_length = []
  girvan_12port_v14_length.extend([girvan_12port_zigzag_length[0], girvan_12port_ascending_length[0], girvan_12port_localmin_length[0], girvan_12port_globalmin_length[0]])
  girvan_12port_v30_length.extend([girvan_12port_zigzag_length[1], girvan_12port_ascending_length[1], girvan_12port_localmin_length[1], girvan_12port_globalmin_length[1]])
  girvan_12port_v57_length.extend([girvan_12port_zigzag_length[2], girvan_12port_ascending_length[2], girvan_12port_localmin_length[2], girvan_12port_globalmin_length[2]])
  girvan_12port_v118_length.extend([girvan_12port_zigzag_length[3], girvan_12port_ascending_length[3], girvan_12port_localmin_length[3], girvan_12port_globalmin_length[3]])
  girvan_12port_v300_length.extend([girvan_12port_zigzag_length[4], girvan_12port_ascending_length[4], girvan_12port_localmin_length[4], girvan_12port_globalmin_length[4]])
  girvan_12port_v1062_length.extend([girvan_12port_zigzag_length[5], girvan_12port_ascending_length[5], girvan_12port_localmin_length[5], girvan_12port_globalmin_length[5]])
  girvan_12port_length.extend([girvan_12port_v14_length, girvan_12port_v30_length, girvan_12port_v57_length,
                               girvan_12port_v118_length, girvan_12port_v300_length, girvan_12port_v1062_length])

  girvan_12port_v14_crossing = []
  girvan_12port_v30_crossing = []
  girvan_12port_v57_crossing = []
  girvan_12port_v118_crossing = []
  girvan_12port_v300_crossing = []
  girvan_12port_v1062_crossing = []
  girvan_12port_crossing = []
  girvan_12port_v14_crossing.extend([girvan_12port_zigzag_crossing[0], girvan_12port_ascending_crossing[0], girvan_12port_localmin_crossing[0], girvan_12port_globalmin_crossing[0]])
  girvan_12port_v30_crossing.extend([girvan_12port_zigzag_crossing[1], girvan_12port_ascending_crossing[1], girvan_12port_localmin_crossing[1], girvan_12port_globalmin_crossing[1]])
  girvan_12port_v57_crossing.extend([girvan_12port_zigzag_crossing[2], girvan_12port_ascending_crossing[2], girvan_12port_localmin_crossing[2], girvan_12port_globalmin_crossing[2]])
  girvan_12port_v118_crossing.extend([girvan_12port_zigzag_crossing[3], girvan_12port_ascending_crossing[3], girvan_12port_localmin_crossing[3], girvan_12port_globalmin_crossing[3]])
  girvan_12port_v300_crossing.extend([girvan_12port_zigzag_crossing[4], girvan_12port_ascending_crossing[4], girvan_12port_localmin_crossing[4], girvan_12port_globalmin_crossing[4]])
  girvan_12port_v1062_crossing.extend([girvan_12port_zigzag_crossing[5], girvan_12port_ascending_crossing[5], girvan_12port_localmin_crossing[5], girvan_12port_globalmin_crossing[5]])
  girvan_12port_crossing.extend([girvan_12port_v14_crossing, girvan_12port_v30_crossing, girvan_12port_v57_crossing,
                                 girvan_12port_v118_crossing, girvan_12port_v300_crossing, girvan_12port_v1062_crossing])

  girvan_12port_v14_bending = []
  girvan_12port_v30_bending = []
  girvan_12port_v57_bending = []
  girvan_12port_v118_bending = []
  girvan_12port_v300_bending = []
  girvan_12port_v1062_bending = []
  girvan_12port_bending = []
  girvan_12port_v14_bending.extend([girvan_12port_zigzag_bending[0], girvan_12port_ascending_bending[0], girvan_12port_localmin_bending[0], girvan_12port_globalmin_bending[0]])
  girvan_12port_v30_bending.extend([girvan_12port_zigzag_bending[1], girvan_12port_ascending_bending[1], girvan_12port_localmin_bending[1], girvan_12port_globalmin_bending[1]])
  girvan_12port_v57_bending.extend([girvan_12port_zigzag_bending[2], girvan_12port_ascending_bending[2], girvan_12port_localmin_bending[2], girvan_12port_globalmin_bending[2]])
  girvan_12port_v118_bending.extend([girvan_12port_zigzag_bending[3], girvan_12port_ascending_bending[3], girvan_12port_localmin_bending[3], girvan_12port_globalmin_bending[3]])
  girvan_12port_v300_bending.extend([girvan_12port_zigzag_bending[4], girvan_12port_ascending_bending[4], girvan_12port_localmin_bending[4], girvan_12port_globalmin_bending[4]])
  girvan_12port_v1062_bending.extend([girvan_12port_zigzag_bending[5], girvan_12port_ascending_bending[5], girvan_12port_localmin_bending[5], girvan_12port_globalmin_bending[5]])
  girvan_12port_bending.extend([girvan_12port_v14_bending, girvan_12port_v30_bending, girvan_12port_v57_bending,
                                girvan_12port_v118_bending, girvan_12port_v300_bending, girvan_12port_v1062_bending])
  
  plot_group_bar_chart("vertex", "length", "louvain_4port_length", groupNames, labelNames, np.transpose(louvain_4port_length), colors_6)
  plot_group_bar_chart("vertex", "crossing", "louvain_4port_crossing", groupNames, labelNames, np.transpose(louvain_4port_crossing), colors_6)
  plot_group_bar_chart("vertex", "bending", "louvain_4port_bending", groupNames, labelNames, np.transpose(louvain_4port_bending), colors_6)
  plot_group_bar_chart("vertex", "length", "louvain_8port_length", groupNames, labelNames, np.transpose(louvain_8port_length), colors_6)
  plot_group_bar_chart("vertex", "crossing", "louvain_8port_crossing", groupNames, labelNames, np.transpose(louvain_8port_crossing), colors_6)
  plot_group_bar_chart("vertex", "bending", "louvain_8port_bending", groupNames, labelNames, np.transpose(louvain_8port_bending), colors_6)
  plot_group_bar_chart("vertex", "length", "louvain_12port_length", groupNames, labelNames, np.transpose(louvain_12port_length), colors_6)
  plot_group_bar_chart("vertex", "crossing", "louvain_12port_crossing", groupNames, labelNames, np.transpose(louvain_12port_crossing), colors_6)
  plot_group_bar_chart("vertex", "bending", "louvain_12port_bending", groupNames, labelNames, np.transpose(louvain_12port_bending), colors_6)
  
  plot_group_bar_chart("vertex", "length", "leiden_4port_length", groupNames, labelNames, np.transpose(leiden_4port_length), colors_6)
  plot_group_bar_chart("vertex", "crossing", "leiden_4port_crossing", groupNames, labelNames, np.transpose(leiden_4port_crossing), colors_6)
  plot_group_bar_chart("vertex", "bending", "leiden_4port_bending", groupNames, labelNames, np.transpose(leiden_4port_bending), colors_6)
  plot_group_bar_chart("vertex", "length", "leiden_8port_length", groupNames, labelNames, np.transpose(leiden_8port_length), colors_6)
  plot_group_bar_chart("vertex", "crossing", "leiden_8port_crossing", groupNames, labelNames, np.transpose(leiden_8port_crossing), colors_6)
  plot_group_bar_chart("vertex", "bending", "leiden_8port_bending", groupNames, labelNames, np.transpose(leiden_8port_bending), colors_6)
  plot_group_bar_chart("vertex", "length", "leiden_12port_length", groupNames, labelNames, np.transpose(leiden_12port_length), colors_6)
  plot_group_bar_chart("vertex", "crossing", "leiden_12port_crossing", groupNames, labelNames, np.transpose(leiden_12port_crossing), colors_6)
  plot_group_bar_chart("vertex", "bending", "leiden_12port_bending", groupNames, labelNames, np.transpose(leiden_12port_bending), colors_6)
  
  plot_group_bar_chart("vertex", "length", "girvan_4port_length", groupNames, labelNames, np.transpose(girvan_4port_length), colors_6)
  plot_group_bar_chart("vertex", "crossing", "girvan_4port_crossing", groupNames, labelNames, np.transpose(girvan_4port_crossing), colors_6)
  plot_group_bar_chart("vertex", "bending", "girvan_4port_bending", groupNames, labelNames, np.transpose(girvan_4port_bending), colors_6)
  plot_group_bar_chart("vertex", "length", "girvan_8port_length", groupNames, labelNames, np.transpose(girvan_8port_length), colors_6)
  plot_group_bar_chart("vertex", "crossing", "girvan_8port_crossing", groupNames, labelNames, np.transpose(girvan_8port_crossing), colors_6)
  plot_group_bar_chart("vertex", "bending", "girvan_8port_bending", groupNames, labelNames, np.transpose(girvan_8port_bending), colors_6)
  plot_group_bar_chart("vertex", "length", "girvan_12port_length", groupNames, labelNames, np.transpose(girvan_12port_length), colors_6)
  plot_group_bar_chart("vertex", "crossing", "girvan_12port_crossing", groupNames, labelNames, np.transpose(girvan_12port_crossing), colors_6)
  plot_group_bar_chart("vertex", "bending", "girvan_12port_bending", groupNames, labelNames, np.transpose(girvan_12port_bending), colors_6)

draw_algorithm_port("", "", data)


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
  plot_group_bar_chart('Algorithm', 'Length', '4port_zigzag_length', groupNames, labelNames, np.transpose(length_4port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', '8port_zigzag_length', groupNames, labelNames, np.transpose(length_8port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', '12port_zigzag_length', groupNames, labelNames, np.transpose(length_12port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', '4port_ascending_length', groupNames, labelNames, np.transpose(length_4port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', '8port_ascending_length', groupNames, labelNames, np.transpose(length_8port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', '12port_ascending_length', groupNames, labelNames, np.transpose(length_12port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', '4port_localmin_length', groupNames, labelNames, np.transpose(length_4port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', '8port_localmin_length', groupNames, labelNames, np.transpose(length_8port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', '12port_localmin_length', groupNames, labelNames, np.transpose(length_12port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', '4port_globalmin_length', groupNames, labelNames, np.transpose(length_4port_globalmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', '8port_globalmin_length', groupNames, labelNames, np.transpose(length_8port_globalmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Length', '12port_globalmin_length', groupNames, labelNames, np.transpose(length_12port_globalmin), colors_6)
  
  plot_group_bar_chart('Algorithm', 'Crossing', '4port_zigzag_crossing', groupNames, labelNames, np.transpose(crossing_4port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', '8port_zigzag_crossing', groupNames, labelNames, np.transpose(crossing_8port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', '12port_zigzag_crossing', groupNames, labelNames, np.transpose(crossing_12port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', '4port_ascending_crossing', groupNames, labelNames, np.transpose(crossing_4port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', '8port_ascending_crossing', groupNames, labelNames, np.transpose(crossing_8port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', '12port_ascending_crossing', groupNames, labelNames, np.transpose(crossing_12port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', '4port_localmin_crossing', groupNames, labelNames, np.transpose(crossing_4port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', '8port_localmin_crossing', groupNames, labelNames, np.transpose(crossing_8port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', '12port_localmin_crossing', groupNames, labelNames, np.transpose(crossing_12port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', '4port_globalmin_crossing', groupNames, labelNames, np.transpose(crossing_4port_globalmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', '8port_globalmin_crossing', groupNames, labelNames, np.transpose(crossing_8port_globalmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Crossing', '12port_globalmin_crossing', groupNames, labelNames, np.transpose(crossing_12port_globalmin), colors_6)
  
  plot_group_bar_chart('Algorithm', 'Bending', '4port_zigzag_bending', groupNames, labelNames, np.transpose(bending_4port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', '8port_zigzag_bending', groupNames, labelNames, np.transpose(bending_8port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', '12port_zigzag_bending', groupNames, labelNames, np.transpose(bending_12port_zigzag), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', '4port_ascending_bending', groupNames, labelNames, np.transpose(bending_4port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', '8port_ascending_bending', groupNames, labelNames, np.transpose(bending_8port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', '12port_ascending_bending', groupNames, labelNames, np.transpose(bending_12port_ascending), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', '4port_localmin_bending', groupNames, labelNames, np.transpose(bending_4port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', '8port_localmin_bending', groupNames, labelNames, np.transpose(bending_8port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', '12port_localmin_bending', groupNames, labelNames, np.transpose(bending_12port_localmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', '4port_globalmin_bending', groupNames, labelNames, np.transpose(bending_4port_globalmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', '8port_globalmin_bending', groupNames, labelNames, np.transpose(bending_8port_globalmin), colors_6)
  plot_group_bar_chart('Algorithm', 'Bending', '12port_globalmin_bending', groupNames, labelNames, np.transpose(bending_12port_globalmin), colors_6)

# draw_port_layout("", "", data)

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
  plot_group_bar_chart("PortNum", "length", "louvain_zigzag_length", groupNames, labelNames, np.transpose(length_louvain_zigzag), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "louvain_zigzag_crossing", groupNames, labelNames, np.transpose(crossing_louvain_zigzag), colors_6)
  plot_group_bar_chart("PortNum", "bending", "louvain_zigzag_bending", groupNames, labelNames, np.transpose(bending_louvain_zigzag), colors_6)
  
  plot_group_bar_chart("PortNum", "length", "louvain_ascending_length", groupNames, labelNames, np.transpose(length_louvain_ascending), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "louvain_ascending_crossing", groupNames, labelNames, np.transpose(crossing_louvain_ascending), colors_6)
  plot_group_bar_chart("PortNum", "bending", "louvain_ascending_bending", groupNames, labelNames, np.transpose(bending_louvain_ascending), colors_6)
  
  plot_group_bar_chart("PortNum", "length", "louvain_localmin_length", groupNames, labelNames, np.transpose(length_louvain_localmin), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "louvain_localmin_crossing", groupNames, labelNames, np.transpose(crossing_louvain_localmin), colors_6)
  plot_group_bar_chart("PortNum", "bending", "louvain_localmin_bending", groupNames, labelNames, np.transpose(bending_louvain_localmin), colors_6)

  plot_group_bar_chart("PortNum", "length", "louvain_globalmin_length", groupNames, labelNames, np.transpose(length_louvain_globalmin), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "louvain_globalmin_crossing", groupNames, labelNames, np.transpose(crossing_louvain_globalmin), colors_6)
  plot_group_bar_chart("PortNum", "bending", "louvain_globalmin_bending", groupNames, labelNames, np.transpose(bending_louvain_globalmin), colors_6)
  
  ## leiden
  plot_group_bar_chart("PortNum", "length", "leiden_zigzag_length", groupNames, labelNames, np.transpose(length_leiden_zigzag), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "leiden_zigzag_crossing", groupNames, labelNames, np.transpose(crossing_leiden_zigzag), colors_6)
  plot_group_bar_chart("PortNum", "bending", "leiden_zigzag_bending", groupNames, labelNames, np.transpose(bending_leiden_zigzag), colors_6)
  
  plot_group_bar_chart("PortNum", "length", "leiden_ascending_length", groupNames, labelNames, np.transpose(length_leiden_ascending), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "leiden_ascending_crossing", groupNames, labelNames, np.transpose(crossing_leiden_ascending), colors_6)
  plot_group_bar_chart("PortNum", "bending", "leiden_ascending_bending", groupNames, labelNames, np.transpose(bending_leiden_ascending), colors_6)
  
  plot_group_bar_chart("PortNum", "length", "leiden_localmin_length", groupNames, labelNames, np.transpose(length_leiden_localmin), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "leiden_localmin_crossing", groupNames, labelNames, np.transpose(crossing_leiden_localmin), colors_6)
  plot_group_bar_chart("PortNum", "bending", "leiden_localmin_bending", groupNames, labelNames, np.transpose(bending_leiden_localmin), colors_6)

  plot_group_bar_chart("PortNum", "length", "leiden_globalmin_length", groupNames, labelNames, np.transpose(length_leiden_globalmin), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "leiden_globalmin_crossing", groupNames, labelNames, np.transpose(crossing_leiden_globalmin), colors_6)
  plot_group_bar_chart("PortNum", "bending", "leiden_globalmin_bending", groupNames, labelNames, np.transpose(bending_leiden_globalmin), colors_6)
  
  # girvan-newman
  plot_group_bar_chart("PortNum", "length", "girvan_zigzag_length", groupNames, labelNames, np.transpose(length_girvan_zigzag), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "girvan_zigzag_crossing", groupNames, labelNames, np.transpose(crossing_girvan_zigzag), colors_6)
  plot_group_bar_chart("PortNum", "bending", "girvan_zigzag_bending", groupNames, labelNames, np.transpose(bending_girvan_zigzag), colors_6)
  
  plot_group_bar_chart("PortNum", "length", "girvan_ascending_length", groupNames, labelNames, np.transpose(length_girvan_ascending), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "girvan_ascending_crossing", groupNames, labelNames, np.transpose(crossing_girvan_ascending), colors_6)
  plot_group_bar_chart("PortNum", "bending", "girvan_ascending_bending", groupNames, labelNames, np.transpose(bending_girvan_ascending), colors_6)
  
  plot_group_bar_chart("PortNum", "length", "girvan_localmin_length", groupNames, labelNames, np.transpose(length_girvan_localmin), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "girvan_localmin_crossing", groupNames, labelNames, np.transpose(crossing_girvan_localmin), colors_6)
  plot_group_bar_chart("PortNum", "bending", "girvan_localmin_bending", groupNames, labelNames, np.transpose(bending_girvan_localmin), colors_6)

  plot_group_bar_chart("PortNum", "length", "girvan_globalmin_length", groupNames, labelNames, np.transpose(length_girvan_globalmin), colors_6)
  plot_group_bar_chart("PortNum", "crossing", "girvan_globalmin_crossing", groupNames, labelNames, np.transpose(crossing_girvan_globalmin), colors_6)
  plot_group_bar_chart("PortNum", "bending", "girvan_globalmin_bending", groupNames, labelNames, np.transpose(bending_girvan_globalmin), colors_6)
  
# draw_algorithm_layout("", "", data)