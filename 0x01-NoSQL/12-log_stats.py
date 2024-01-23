#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB:
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(
            '\tmethod {method}: {collection.count_documents({"method", method})}')
    print(f'{collection.count_documents({"path": "/status"})} status check')
