#!/usr/bin/env python3
"""Pymongo: List all documents"""


def list_all(mongo_collection):
    """
        function to list all documents of a collection
    """
    return [doc for doc in mongo_collection.find()]
