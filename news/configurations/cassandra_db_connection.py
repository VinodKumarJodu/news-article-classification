import os, sys
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from news.exception import NewsException

class CassandraDBConnection:
    def __init__(self):
        self.CLOUD_CONFIG_PATH = os.getenv('CLOUD_CONFIG_PATH')
        self.CLIENT_ID = os.getenv('CLIENT_ID')
        self.CLIENT_KEY = os.getenv('CLIENT_KEY')
        
    def connect(self):
        try:
            self.cloud_config = {'secure_connect_bundle': self.CLOUD_CONFIG_PATH}
            self.auth_provider = PlainTextAuthProvider(self.CLIENT_ID, self.CLIENT_KEY)
            self.cluster = Cluster(cloud=self.cloud_config, auth_provider=self.auth_provider)
            self.session = self.cluster.connect()
            return self.session
        except Exception as e:
            raise NewsException(e, sys)
        
    def close(self):
        self.session.shutdown()
        self.cluster.shutdown()

# cassandra = CassandraDBConnection()
# session = cassandra.connect()

# rows = session.execute("select * from ml_keyspace.news_article_train").one()
# print(rows)
# train_file_path = "/home/v/news-article-classification/feat_store/train.csv"
# test_file_path = "/home/v/news-article-classification/feat_store/test.csv"
# # os.makedirs(train_file_path, exist_ok=True)

# with open(train_file_path,'w') as f:
#       writer = csv.writer(f)
#       writer.writerow(['ArticleId','Text','Category'])
#       rows = session.execute("select * from ml_keyspace.news_article_train")
#       for row in rows[1:]:
#             # print(str(row.Text))
#             writer.writerow([int(row.ArticleId), str(row.Text),str(row.Category)])

# # os.makedirs(test_file_path, exist_ok=True)
# with open(test_file_path,'w') as f:
#       writer = csv.writer(f)
#       writer.writerow(['ArticleId','Text'])
#       rows = session.execute("select * from ml_keyspace.news_article_test")
#       for row in rows[1:]:
#             # print(str(row.Text))
#             writer.writerow([int(row.ArticleId), str(row.Text)])
