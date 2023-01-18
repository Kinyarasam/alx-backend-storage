#!/usr/bin/env python3
""" Task 11's module """


def schools_by_topic(mongo_collection, topic):
    """get list of schools having a specific topic

    Args:
        mongo_collection: pymongo collection object.
        topic (string): the topic to search by.

    Returns:
        (List(string)): list of schools having a specific topic.
    """
    return [top for top in mongo_collection.find({
        'topics': {
            "$elemMatch": {
                "$eq": topic
            },
        },
    })]
