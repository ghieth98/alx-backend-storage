#!/usr/bin/env python3
"""Function that lists all documents in a collection"""
from pymongo import collection


def list_all(mongo_collection):
    """List all documents in a collection"""
    return list(mongo_collection.find())
