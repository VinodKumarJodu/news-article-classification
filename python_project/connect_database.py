import os
import csv
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
         'secure_connect_bundle': '/home/v/news-article-classification/secure-connect-ml-db.zip'
}
auth_provider = PlainTextAuthProvider('apKAnWibUwXIfUfcHwxWItGt', 'xEZZZ9Xo1NE+ZoOYXWyJvQxBvDhYEYMb69MabYOFptPHD82rT9mW.ZlDz-XkPbq-070IoemZbGWsB1NeHweXJ4eeMT2WDSpAeD5_gAIUHRnZz8oR,xL0ZmTXZ6geU13N')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

# print(cloud_config)
# rows = session.execute("select * from ml_keyspace.news_article_train")
# print(rows)
train_file_path = "/home/v/news-article-classification/feat_store/train.csv"
test_file_path = "/home/v/news-article-classification/feat_store/test.csv"
# os.makedirs(train_file_path, exist_ok=True)

with open(train_file_path,'w') as f:
      writer = csv.writer(f)
      writer.writerow(['ArticleId','Text','Category'])
      rows = session.execute("select * from ml_keyspace.news_article_train")
      for row in rows[1:]:
            # print(str(row.Text))
            writer.writerow([int(row.ArticleId), str(row.Text),str(row.Category)])

# os.makedirs(test_file_path, exist_ok=True)
with open(test_file_path,'w') as f:
      writer = csv.writer(f)
      writer.writerow(['ArticleId','Text'])
      rows = session.execute("select * from ml_keyspace.news_article_test")
      for row in rows[1:]:
            # print(str(row.Text))
            writer.writerow([int(row.ArticleId), str(row.Text)])
