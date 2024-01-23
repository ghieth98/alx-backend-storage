#!/usr/bin/env python3
"""Function that returns the list of school having a specific topic:"""
from pymongo import collection


def schools_by_topic(mongo_collection, topic):
    """Function that returns the list of school having a specific"""
    return list(mongo_collection.find({'topic': topic}))
