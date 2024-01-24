#!/usr/bin/env python3

"""
Module for using Redis database
"""
import uuid
from typing import Callable, Union

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

    def get(self, key: str, fn: Callable = None) -> Union[
        str, bytes, int, float]:
        """ Retrieves data from redis """
        data = self._redis.get(key)

        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """ Retrieves a string value form redis"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """ Retrieves a integer value from redis"""
        return self.get(key, lambda x: x.int(x))
