# 2020. 01. 13

## 개발 환경 
- conda env list 
- conda create -n bioeng python=3.7
- activate bioeng 

## jupyterlab 설치 
- conda install -c conda-forge jupyterlab

## root 디렉토리 c:\kribb 만들기 

## 실행 
- jupyter lab --ip=0.0.0.0 --notebook-dir="c:\\kribb\\"

## github 저장소 만들기 
- https://github.com/greendaygh/sasa.git

## git 설치

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

## git data 받아오기
```
git clone https://github.com/greendaygh/sasa
```

## anaconda에 flask framework 설치하기 
https://anaconda.org/anaconda/flask


## flask 예제 실행
https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application


## Q1
- http://127.0.0.1:5000/my/ 라고 브라우저에 입력하면 "you" 출력

## python 문법 실습
```
from flask import myfunction 
myfunction(~~~)
flask::myfunction(~~~)
```


##  튜토리얼 예제 실행
```
https://github.com/greendaygh/bioengml/blob/master/%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC1-%EC%8B%A4%EC%8A%B5-20191219.ipynb
```
- 파일 읽기 쓰기 전까지 코드 실행, 이해 노력


## 클래스 만들기

- class: circuit 
- class: part




