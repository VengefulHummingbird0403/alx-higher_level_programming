#!/usr/bin/python3
"""
Develops a LockedClass class that restricts the user from dynamically generating new instance attributes, with the exception of when the new instance attribute is named "first_name:
"""


class LockedClass:
    """Allow only first name attribute"""
    __slots__ = ['first_name']
