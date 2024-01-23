#!/usr/bin/env python3
"""Function that changes all topics of a school"""

from pymongo import collection


def update_topics(mongo_collection, name, topics):
    """Function that changes all topics of a school"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
