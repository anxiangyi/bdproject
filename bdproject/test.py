HOST = '127.0.0.1'
# 端口号 ---------类型为整数！！！----------
PORT = 3306
# 用户名
USER = 'root'
# 密码
PASSWD = 'root'
# 需要存入的数据库
DB = 'spider01'
# 指定字符集，注意uft-8中的‘-’，识别不了！！
CHARACTER = 'utf8'
import pymysql
# 加载settings文件
from scrapy.utils.project import get_project_settings


class MySQL_Pipeline:
    def __init__(self):
        settings = get_project_settings()
        self.host = settings['HOST']
        self.port = settings['PORT']
        self.user = settings['USER']
        self.passwd = settings['PASSWD']
        self.db = settings['DB']
        self.character = settings['CHARACTER']
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.passwd,
            db=self.db,
            charset=self.character
        )
        # 创建游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into book(name,src) values("{}","{}")'.format(item['name'], item['src'])
        # 执行sql语句
        self.cursor.execute(sql)
        # 提交事务
        self.conn.commit()
        return item

    def __del__(self):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()