
### 팀 이름 `t2`

#### 팀원 `정미은` `이정훈` `김태영`

#### 프로젝트 주제
영화박스오피스 데이터 수집(Extract)/처리(Transform)/보관 및 활용(Load)

#### 프로젝트 내용
영화 박스오피스 데이터 수집/처리/보관 및 활용에 대하여 
각 단계에 대한 파이썬 프로그램을 package(PIP 설치) 단위로  개발
개발 package를 airflow 적용 및 운영

#### 특별 미션
모든 PIP package에 Ice_breaking 함수를 생성하여 이를 호출하면 
아스키아트로 변환된 팀원 사진이 호출

#### 소스 데이터
[https://www.kobis.or.kr/kobisopenapi/homepg/main/main.do]
*******

#### 테스트 환경
```
$ uname -a
Linux DESKTOP-HPO7GCU 5.15.153.1-microsoft-standard-WSL2 #1 SMP Fri Mar 29 23:14:13 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux

$ cat /etc/issue
Ubuntu 24.04 LTS \n \l

$ pyenv -v
pyenv 2.4.7

# python version 3.11.9로 맞추기
$ pyenv global 3.11.9

# 팀플을 위한 가상환경 만들기
$ pyenv virtualenv 3.11.9 t2

# 프롬프트에서 사용하기 위한 설정
$ pyenv shell t2

(t2) $ python -V
Python 3.11.9

(t2) $ airflow version
3.11.9

(t2)$ git init
(t2)$ pdm init

# 패키지 설치
(t2)$ pdm add pytest pytest-cov figlet requests pandas
```

#### 환경변수 설정
```
$ tail -n 4 ~/.zshrc
# AIRFLOW
export AIRFLOW_HOME=~/airflow_team
export AIRFLOW__CORE__DAGS_FOLDER=~/code/team1/movie_airflow/dags
export AIRFLOW__CORE__LOAD_EXAMPLES=False

# 새로운 admin 암호확인
$ cat ~/airflow_team/standalone_admin_password.txt
```
*****
#### Extract
2022년 영화 데이터 월 단위로 추출
parquet 파일로 저장

#### Transform
parquet 파일을 DataFrame으로 저장
중복 데이터 값 merge
movieCnt(일별 관객수)를 월 단위로 합계하여 매월 인기 영화 집계

#### Load
tabulate 모듈을 활용하여 산출된 DataFrame을 예쁘게🌸 출력


