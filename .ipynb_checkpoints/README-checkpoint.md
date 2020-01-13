# 2020. 01. 13

## 개발 환경 
- conda env list 
- conda create -n bioeng python=3.7
- activate bioeng 

## jupyterlab 설치 
- conda install -c conda-forge jupyterlab

## root 디렉토리 c:\kribb 만들기 

## 실행 
jupyter lab --ip=0.0.0.0 --notebook-dir="c:\\kribb\\"

## github 저장소 만들기 
https://github.com/greendaygh/sasa.git

## git 설치

## 로컬 저장소와 github 저장소 연결
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


## git data 받아오기
git clone https://github.com/greendaygh/sasa

## project directory 
