from datetime import datetime
from flask import render_template, request,redirect
from run import app


@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return redirect('http://43.154.93.134')


@app.route('/image/<filename>/')
def get_image(filename):
    return redirect("http://43.154.93.134/image/<filename>/")


# 识别动物的参数回调
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        return redirect("http://43.154.93.134/uploader")
     

# 点击动物的参数回调
@app.route('/introduce', methods = ['GET', 'POST'])
def introduce():
    if request.method == 'POST':
        return redirect("http://43.154.93.134/introduce")

# 查询动物的参数回调
@app.route('/animal_query', methods = ['GET', 'POST'])
def animal_query():
    if request.method == 'POST':
       return redirect("http://43.154.93.134/animal_query")

# 查询地方法规的参数回调
@app.route('/province_query', methods = ['GET', 'POST'])
def province_query():
    if request.method == 'POST':
        return redirect("http://43.154.93.134/province_query")

# 查询国家法规的参数回调
@app.route('/nation_query', methods = ['GET', 'POST'])
def nation_query():
    if request.method == 'POST':
        return redirect("http://43.154.93.134/nation_query")
# 查询相关案例的参数回调
@app.route('/example_query', methods = ['GET', 'POST'])
def example_query():
    if request.method == 'POST':
        return redirect("http://43.154.93.134/example_query")


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8080")
