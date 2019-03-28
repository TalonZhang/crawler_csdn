import pymongo
from crawler_csdn.settings import mongo_host, mongo_db_name, mongo_port, url_collection


class CrawlerCsdnGetUrl():
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.mycol = mydb[url_collection]

    def get_url_list(self):
        url_list = self.mycol.find({}, {"_id": 0, "blog_address": 1})

        new_lis = [x['blog_address'] for x in url_list]
        return new_lis
        # print(new_lis)
        # print(len(new_lis))


#CrawlerCsdnGetUrl().get_url_list()