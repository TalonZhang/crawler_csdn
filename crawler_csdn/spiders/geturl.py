import pymongo


class CrawlerCsdnGetUrl():
    def __init__(self):
        # host = mongo_host
        # port = mongo_port
        # dbname = mongo_db_name
        # sheetname = mongo_db_collection
        client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        mydb = client['csdn']
        self.mycol = mydb['csdn_blog']

    def get_url_list(self):
        url_list = self.mycol.find({}, {"_id": 0, "blog_address": 1})

        new_lis = [x['blog_address'] for x in url_list]
        return new_lis
        # print(new_lis)
        # print(len(new_lis))


#CrawlerCsdnGetUrl().get_url_list()