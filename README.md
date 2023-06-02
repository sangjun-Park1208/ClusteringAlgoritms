## Community Detection을 위한 Clustering algorithms (연구실 서버 배포용)
### Orthogonal Graph
#### 1. Girvan-Newman Algorithm
##### 예시: http://SERVER_BASE_URL:#PORT/girvan-newman/?data=1062&iter=8
##### 예시: http://SERVER_BASE_URL:#PORT/girvan-newman/?data=300&iter=8
#### 2. Louvain Algorithm
##### 예시: http://SERVER_BASE_URL:#PORT/louvain/?data=1062&resolution=0.1&threshold=0.0000001&seed=0
##### 예시: http://SERVER_BASE_URL:#PORT/louvain/?data=300&resolution=0.1&threshold=0.0000001&seed=0
#### 3. Leiden Algorithm
##### 예시: http://SERVER_BASE_URL:#PORT/leiden/?data=1062
##### 예시: http://SERVER_BASE_URL:#PORT/leiden/?data=300

### Patient Flow
#### 1. Girvan-Newman Algorithm
##### 예시: http://SERVER_BASE_URL:#PORT/girvan-newman/pf/?p=1&iter=8
##### 예시: http://SERVER_BASE_URL:#PORT/girvan-newman/pf/?p=2&iter=9
##### 예시: http://SERVER_BASE_URL:#PORT/girvan-newman/pf/?p=3&iter=8
#### 2. Louvain Algorithm
##### 예시: http://SERVER_BASE_URL:#PORT/louvain/pf/?p=1&resolution=0.1&threshold=0.0000001&seed=0
##### 예시: http://SERVER_BASE_URL:#PORT/louvain/pf/?p=2&resolution=0.1&threshold=0.0000001&seed=0
##### 예시: http://SERVER_BASE_URL:#PORT/louvain/pf/?p=3&resolution=0.1&threshold=0.0000001&seed=0
#### 3. Leiden Algorithm
##### 예시: http://SERVER_BASE_URL:#PORT/leiden/pf/?p=1
##### 예시: http://SERVER_BASE_URL:#PORT/leiden/pf/?p=2
##### 예시: http://SERVER_BASE_URL:#PORT/leiden/pf/?p=3

#### - Local 환경 flask 구동 명령어
`flask --app clustering run` or `python ./clustering.py` <br/>
(python3인 경우 `python3 ./clustering.py`)

#### - Data 추가
`/data/bus-1062.csv`, `/data/branch-1062.csv`, <br/>
`/data/bus-300.csv`, `/data/branch-300.csv`, <br/>
`/data/bus-118.csv`, `/data/branch-118.csv`, <br/>
`/data/bus-57.csv`, `/data/branch-57.csv`, <br/>
`/data/bus-30.csv`, `/data/branch-30.csv`, <br/>
`/data/bus-14.csv`, `/data/branch-14.csv` 추가 (Orthogonal layout) <br/><br/>
`p1_region.csv`, `p2_region.csv`, `p3_region.csv`, <br/>
`p1_type1.csv`, `p1_type4.csv`, <br/>
`p2_type1.csv`, `p2_type4.csv`, <br/>
`p3_type1.csv`, `p3_type4.csv` 추가 (Patient Flow)
