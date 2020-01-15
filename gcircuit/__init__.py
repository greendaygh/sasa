from flask import Flask,render_template,request

app= Flask(__name__)

@app.route('/')
def helloworld():
    return"HelloWorld!!"

# @app.route('/hello')
# def helloworld_from_html():
#     return render_template('hello.html')
    
@app.route("/test")
def test():
    return render_template("html_test.html")

    
@app.route("/result", methods=['POST'])
def post():
    return render_template('hello.html')
    
    
@app.route("/login1")
def login1():
    return render_template("method_test.html")

    
@app.route("/login")
def login():
    if request.method=='POST':
        return "login"