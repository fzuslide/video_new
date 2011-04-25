#coding=utf-8

from flask import Flask

from views.spider import spider

app = Flask(__name__)
app.register_module(spider)



if __name__ == '__main__':
    app.debug=True
    app.run()


