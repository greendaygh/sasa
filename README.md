# 2020. 01. 13

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


# 2020. 01. 14

## 클래스 만들기
- class: circuit 
- class: part


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
