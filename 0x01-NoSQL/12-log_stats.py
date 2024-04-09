#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB:

    Database: logs
    Collection: nginx
    Display (same as the example):
        first line: x logs where x is the number of docs in this collection
        second line: Methods:
        5 lines with the number of documents with the method =
        ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
        one line with the number of documents with:
            method=GET
            path=/status
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017')
    collection = client.logs.nginx

    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        # print(collection.count_documents({"method": method}))
        print(
            f'\tmethod {method}: {collection.count_documents({"method": method})}'
        )
    print(f"{collection.count_documents({'path': '/status'})} status check")
