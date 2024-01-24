#!/usr/bin/env python3

"""
Module for using Redis database
"""
import uuid

import redis


class Cache:
    """
    Redis Cache class
    """

    def __init__(self) -> None:
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: [str, bytes, int, float]) -> str:
        """ Stores data to redis """
        key_data = str(uuid.uuid4())
        self._redis.set(key_data, data)
        
        return key_data
