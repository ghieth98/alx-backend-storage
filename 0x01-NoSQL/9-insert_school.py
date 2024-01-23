#!/usr/bin/env python3
"""Function to insert a new document in  collection"""
from pymongo import collection


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in  collection"""
    new_doc = mongo_collection.insert_one(kwargs)

    return new_doc.inserted_id
