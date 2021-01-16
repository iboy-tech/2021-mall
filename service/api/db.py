from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
# from requests.api import options
import datetime
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import random
import string

#通用组件
app = Flask(__name__,static_folder='../../dist/static',template_folder='../../dist')
# app = Flask(__name__,static_folder='../../dist',template_folder='../../dist')
# r'/*' 是通配符，让本服务器所有的 URL 都允许跨域请求
CORS(app, resources=r'/*')
# cors = CORS(app, resources={r"/*": {"origins": "*"}})
# ip limit
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["800 per day", "200 per hour"]
)

# #避免与vue冲突
# app.jinja_env.variable_start_string = '{['
# app.jinja_env.variable_end_string = ']}'

#路径设置
SQL_PATH = os.path.join(os.path.dirname(__file__),'../../public/sql')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'   #本地
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///'+os.path.join(SQL_PATH,'kamifaka.db')   #默认数据库
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@127.0.0.1:336/KAFAKA?charset=utf8mb4'   #本地Docker
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://faka:xxxxx@154:3306/faka?charset=utf8mb4'   #远程
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://docker_db_1:root@127.0.0.1:3306/KAFAKA?charset=utf8mb4'   #本地
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://root:password@127.0.0.1:5432/KAFAKA'   #本地
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://cmmpjjkinayyhk:2428996ef24132a272c88374071448af13aa3169ac551492e7046b264876080a@ec2-52-2-82-109.compute-1.amazonaws.com:5432/deail3ojvojiia'   #远程
# docker run --name postgres -e POSTGRES_PASSWORD=password -e POSTGRES_USER=root -e POSTGRES_DB=KAFAKA -p 5432:5432 -d postgres

app.config['SQLALCHEMY_BINDS'] =  {'order':'sqlite:///'+os.path.join(SQL_PATH,'middle.db')}   #中间转移数据库
# mysql mysql+pymysql://root:wujing0126@127.0.0.1:3306/gbs?charset=utf8
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Setup the Flask-JWT-Extended extension. Read more: https://flask-jwt-extended.readthedocs.io/en/stable/options/
# app.config['JWT_SECRET_KEY'] = ''.join(random.sample(string.ascii_letters + string.digits, 46))  # Change this!
app.config['JWT_SECRET_KEY'] = 'a44545de51d5e4deaswdedcecvrcrfr5f454fd1cec415r4f'  # Change this!
app.config['JWT_ACCESS_TOKEN EXPIRES'] = datetime.timedelta(days=2)
jwt = JWTManager(app)

db = SQLAlchemy(app)

