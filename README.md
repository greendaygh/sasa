# ========== 2020.01.17 ==========

### 각자 다른 app 개발하는 것으로 방향 수정 (주제는 변함 없음)
### 본인 app 소스 코드는 각자의 github branch에 저장되어 있음 
### 본인 branch에서 source clone 받아서 실행 (아래 명령어 사용)
### 코드 이해 필요 
#### 현우
```
git clone -b hw https://github.com/greendaygh/sasa.git
```
#### 태웅
```
git clone -b tu https://github.com/greendaygh/sasa.git
```
#### 용환 
```
git clone -b yh https://github.com/greendaygh/sasa.git
```

### 최종 발표 준비
- 시간: 오후 1시 (생명연 연구동 세미나실)
- 각 10분 내외 (ppt 준비 및 발표)
- 프로젝트 공통 title:  합성생물학을 위한 유전자회로 설계 툴 개발
- 목표: 각자 맡은 분야 목표
- 배경지식: 각자 맡은 분야 개요/배경 (인터넷 검색)
- 수행내용 및 결과: 각자 맡은 분야 (내용, 결과, 코드/스크립트 설명 가능)
- 느낀점 



# ========== 2020 01 16 ==========
- MDBootstrap 사용 인터페이스 개선 (https://mdbootstrap.com/education/bootstrap/quick-start/)
- 특정 branch git clone 할 때 (sasa 상위 디렉토리에서 실행)
```
git clone -b hw https://github.com/greendaygh/sasa.git
```
- 특정 branch git push 할 때
```
git status
git branch
git checkout yh
git branch
git add .
git commit -m "message"
git push
```
- 특정 branch 로 옮기기 전 현재 branch의 코드를 잠시 저장하고 옮긴 후 데이터 받아오기 
``` 
git stash
git stash list
git checkout hw
git fetch
git merge
```
- 참고로 fetch 는 원격 저장소의 내용 확인, 병합은 하지 않음. 대신 원격 저장소의 최신 이력 확인시 사용
- merge 는 병합, pull = fetch + merge 임




## 현우 (flask)
- Part 조합으로 Circuit 제작 코딩 
- html rendering 을 위해 mdbootstrap 사용 (https://mdbootstrap.com/education/bootstrap/quick-start/)
- form submit은 모두 onclick 자바스크립트로 변경 (flag 변수 값 변경 후 submit)

## 용환 (biopython)
- matplotlib 이용 part, circiut 서열과 위치 정보로 그래프 그리기 

## 태웅 (dynamics modeling)
- modeling 코드 flask에 적용 



# ========== 2020 01 15 ==========

- 시작할 때 명령프롬프트 창 2개 띄우기 (jupyter lab, flask)
- flask app structure & run 
- flask 이용한 html rendering 기술 
- html 값 주고 받기 
  - GET / POST 방식 차이점 

## 현우 (flask)
- Part 입력, 출력, (삭제, 편집)
  - 파일에 입력 후 list 출력 
- Part 조합으로 Circuit 제작
  - part 정보 저장 시 index 같이 저장
  - checkbox 이용 리스트에서 part 선택 후 조합 전략
  - circuit 정보 파일 저장

## 용환 (biopython)
- Sequence 
  - alignment 
  - visualization
- biopython에서 part, circiut 서열과 위치 정보로 그래프 그리기 
 

## 태웅 (dynamics modeling)
- modeling (odeint 함수이용)
  - x: the number of mRNAs, y: the number of proteins
  - dx/dt = a - bx
  - dy/dt = cx - dy
- part/circuit class에 정량적 값 저장할 변수 추가
- circuit 선택 후 버튼 누르면 시뮬레이션 실행
- 그래프 출력



# ========== 2020. 01. 14 ==========

## 클래스 만들기
- class: circuit 
- class: part
- https://github.com/greendaygh/sasa/blob/master/excercies20200114.ipynb

## python에서 naming 규칙 
- https://ruriro.tistory.com/11
- 언더스코어의 특별한 의미
 - 접미사 하나를 사용한 경우 : 내부에서 사용한다는 의미
 - 접미사 두개를 사용한 경우 : 클래스 내부에 protect로 사용한다는 의미
 - 접두사 하나를 사용한 경우 : 파이썬 키워드와의 충돌을 방지한다는 의미

- 명명규칙
 - 패키지와 모듈 이름 : 짧은 소문자 + 언더스코어
 - 클래스 이름 : CapWords규칙을 따른다.
 - 예외 이름 : 예외는 클래스이므로 CapWords규칙을 따르고 Error 접미사를 사용한다.
 - 전역 변수 이름 : 언더스코어를 붙여서 해당 모듈에서만 쓰이도록 한다.
 - 함수 이름 : 소문자 + 언더스코어
 - 메서드 이름과 인스턴스 변수 : 소문자 + 언더스코어
 - 상수 : 대문자 + 언더스코어
- 출처: https://ruriro.tistory.com/11 [ruriro]


## biopython 설치 및 사용법
- http://biopython.org/DIST/docs/tutorial/Tutorial.html


## biopython 이용한 그래프 그리는 방법
- Chapter 17  Graphics including GenomeDiagram




# ========== 2020. 01. 13 ==========

## 개발 환경 
```
conda env list 
conda create -n bioeng python=3.7
activate bioeng 
```

## jupyterlab 설치 
```
conda install -c conda-forge jupyterlab
```
## root 디렉토리 c:\kribb 만들기 

## command line에서 jupyter lab 실행 
```
jupyter lab --ip=0.0.0.0 --notebook-dir="c:\\kribb\\"
```

## github 저장소 만들기 
- github 저장소 생성
- https://github.com/greendaygh/sasa.git

## 로컬 머신 git 설치
- https://gitforwindows.org/

## 로컬 저장소와 github 저장소 연결
```
PS C:\kribb\sasa> echo "# sasa project" >> README.md
PS C:\kribb\sasa> git init
Initialized empty Git repository in C:/kribb/sasa/.git/
PS C:\kribb\sasa> git add .
PS C:\kribb\sasa> git commit -m "init"
[master (root-commit) 72ab56e] init
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
PS C:\kribb\sasa> git remote add origin https://github.com/greendaygh/sasa.git
PS C:\kribb\sasa> git push -u origin master
```

## git data 받아오기 (상위 디렉토리에서 실행)
```
git clone https://github.com/greendaygh/sasa
```

## 로컬 저장소에서 원격으로 commit 
```
git add .
git commit -m "message for the update"
git push
```

## 로컬 저장소 업데이트 
```
git pull
```

## anaconda 이용 flask framework 설치하기 
- google에서 "anaconda install flask" 키워드 검색
```
anaconda -c anaconda flask
```

## flask 예제 실행
- https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application


## Q1
- http://127.0.0.1:5000/my/ 라고 브라우저에 입력하면 "you" 출력

## python 문법 실습 (튜토리얼 참고)
```
https://github.com/greendaygh/bioengml/blob/master/%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC1-%EC%8B%A4%EC%8A%B5-20191219.ipynb
```
- 파일 읽기 쓰기 전까지 코드 실행, 이해 노력

