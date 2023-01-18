#!/usr/bin/env python3
""" Task 10's module """


def update_topics(mongo_collection, name, topics):
    """Changes all the topics of a school document based on the name

    Args:
        mongo_collection: pymongo collection object,
        name (string): school name to update.
        topics (List[string]): list of topics to be approached in the school.

    Returns:
        nothing.
    """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}},
        )
