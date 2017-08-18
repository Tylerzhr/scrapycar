from scrapy.exceptions import DropItem
from scrapycar.items import CarItem
import pymysql
from scrapycar import settings
MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

db = pymysql.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB)
db.set_charset('utf8')
cursor = db.cursor()
cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')
class ScrapycarPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,CarItem):
            carbrand=item['carbrand']
            cartype=item['cartype']
            pinyin=item['pinyin']
            model=item['carmodel']
            sql = """INSERT INTO carbrand1(carbrand,pinyin,cartype,model) VALUES (%s,%s,%s,%s)"""
            value=(carbrand,pinyin,cartype,model)
            print(value)
            cursor.execute(sql,value)
            db.commit()

