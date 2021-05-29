# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter


class Ch4SpyderPipeline:
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):
    def open_spider(self, spider):
        # 获取配置文件中的配置信息
        # 连接数据库服务器
        db_name = spider.settings.get("MONGODB_NAME", "mingyantong")
        host = spider.settings.get("MONGODB_HOST", "localhost")
        port = spider.settings.get("MONGODB_PORT", 27017)
        collection_name = spider.settings.get("MONGODB_COLLECTION", "mingyantong_g")
        self.db_client = pymongo.MongoClient(host=host, port=port)
        self.db = self.db_client[db_name]
        self.db_collection = self.db[collection_name]

    def process_item(self, item, spider):
        # 获取spider的各个字段，保存于元组中
        # 设计插入操作的sql语句
        # 执行语句实现插入

        try:
            item_dict = dict(item)
            self.db_collection.insert_one(item_dict)
            # print("成功插入数据")
        except:
            pass

        return item

    def close_spider(self, spider):
        # spider关闭时，执行数据库关闭操作
        # 提交数据、关闭游标、关闭数据库
        self.db_client.close()
