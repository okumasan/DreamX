from flask import Flask,render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
'''
WEB页面主要代码
'''
app = Flask(__name__)
app.config['SECRET_KEY'] = '**sbjtxy2017'
bootstrap = Bootstrap(app)
manager = Manager(app)
@app.route('/')
def index():
        return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
        return render_template('404.html')
@app.errorhandler(500)
def internal_sever_error(e):
        return render_template('500.html')

@app.route('/user/<name>')
def user(name):
        return render_template("SleepRecord.html",name=name)

if __name__=='__main__':
    app.run(debug=True)