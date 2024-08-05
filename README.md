README

### 팀 이름 `t2`
#### 팀원 `정미은` `이정훈` `김태영`
***
#### 프로젝트 주제

영화박스오피스 데이터 수집(Extract)/처리(Transform)/보관 및 활용(Load)

#### 프로젝트 내용

영화 박스오피스 데이터 수집/처리/보관 및 활용에 대하여 
각 단계에 대한 파이썬 프로그램을 package(PIP 설치) 단위로  개발
개발 package를 airflow 적용 및 운영

#### 특별 미션
 
모든 PIP package에 Ice_breaking 함수를 생성하여 이를 호출하면 
아스키아트로 변환된 팀원 사진이 호출
***
#### 기본설정
```
# python version 3.11.9로 맞추기
$ pyenv global 3.11.9
# 팀플을 위한 가상환경 만들기
$ pyenv virtualenv 3.11.9 t2
# 프롬프트에서 사용하기 위한 설정
$ pyenv shell t2
# pdm 설치
$ cd code/t2/Extract
$ git init
$ pdm init
```
#### 패키지 설치 
[dependencies]
pytest
pytest -cov
figlet
requets
pandas

#### 활용 코드
```
코드
```
***
### 진행상황 

#### DAY 1 
- [ ] 작성 package 분배 (4개월 단위로 2022년 자료 수집)
- [ ] 분배 package  개발 진행
- [ ] pytest 통과
- [ ] airflow 가동
- [ ] 팀프로젝트 READ.ME 작성
- [ ] Icd_breaking 함수 생성 후 호출
- [ ] 1차 배포

#### DAY 2
- [ ] 데이터 변환을 위한 함수 생성
- [ ] pytest통과
- [ ] airflow 가동
- [ ] 팀프로젝트 READ.ME 작성
- [ ] 2차 배포

#### DAY 3
- [ ] 3차 배포
- [ ] 4차 최종 배포  및 버그 픽스 
- [ ] 최종발표 및 시연

