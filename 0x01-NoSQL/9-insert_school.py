#!/usr/bin/env python3
""" Task 9's module """

def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection.

    Args:
        mongo_collection (object): pymongo collection object
        kwargs (any): __

    Returns:
        new _id.
    """
    return mongo_collection.insert_one(kwargs)
