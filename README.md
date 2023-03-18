## Flask 笔记
[Python 宋宋flask第一章](https://www.bilibili.com/video/BV1rE411w7Xq/?spm_id_from=333.999.0.0&vd_source=0b01033d74816b5cfa3e938e08f9b69b)

#### 环境配置
`app.run(host='0.0.0.0', port=8000, debug=True)`

或者
`app.config["DEBUG"] = True`

或者
设置一个py文件专门作为环境变量配置 
config.py ：
`import os
ENV = 'development'
DEBUG = True
SECRET_KEY = os.urandom(32)`

`app.config.from_object(config) # 或者
app.config.from_pyfile('config.py')`


#### 路由
必须要有返回值
返回值类型：str  dict  tuple  response  instance

1. str -----> 自己装载为response对象返回
2. dict ----> jsonify response
3. make_response(s) -----> 自己构建response对象， response.header['xx'] = value
4. jonsify()
5. redirect() 重定向
6. render_template() 模板渲染


#### 路由的方式
1. @app.route('/')
2. @app.route('/', endpoint='xxx') + url_for
3. @app.route('/', methods=['POST', 'GET']) 如果不添加post请求，则默认只允许get方法
4. @app.route('/news/<int:age>)  指定类型

#### request

request.args ----> GET
request.form ----> POST
都是字典结构,利用get()方法取值
request.FILES ----> 文件上传
request.cookies ----> cookies 取值



request.url
request.method
request.path
.....


