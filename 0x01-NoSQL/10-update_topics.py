#!/usr/bin/env python3
"""Task 10 Module"""


def update_topics(mongo_collection, name, topics):
    """Update function"""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
