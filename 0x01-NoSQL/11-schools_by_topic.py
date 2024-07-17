#!/usr/bin/env python3
"""Task 11 Module"""


def schools_by_topic(mongo_collection, topic):
    """sorting by topic"""
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
