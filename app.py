from flask import Flask, redirect, url_for, request
import config

app = Flask(__name__)

# app.config.from_pyfile('config.py')

app.config.from_object(config)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/abc')
def show_abc():
    # GET 方法
    return '<h1>this is the abc ! <h1>'


# endpoint : url_for 中以endpoint或函数名为依据获取url

# 如果没有定义endpoint则以函数名为endpoint
# 如果定义了endpoint，则函数名与endpoint均可以奏效
# endpoint 可以做复杂或者不明了的函数名的替代

@app.route('/show_endpoint', endpoint='what_is_endpoint')
def show_endpoint():
    return "show_the_endpoint"


@app.route('/test_endpoint')
def test_endpoint():
    return redirect(url_for('what_is_endpoint'))


@app.route('/test_endpoint_2')
def test_endpoint_2():
    return redirect(url_for('test_endpoint'))


@app.route('/show_request')
def show_request():
    print(request)
    print(request.url)
    print(request.path)
    print(request.full_path)
    print(request.base_url)
    print(request.method)
    return "to the Pycharm Run"


# 响应 response
# make_response() 构建 response 对象 可以给response对象添加一些头部信息
# jsonify(datas) 将datas转换为JSON格式，dict默认使用此函数
# render_template() 渲染模板html
# redirect() 重定向








if __name__ == '__main__':
    app.run()
