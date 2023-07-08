# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#     Defines the List ADT


#Name-Harry Patel
#NSID-ozc189
#studentNumber-11358887
#course-CMPT145
class node(object):
    """ A version of the Node class with public attributes.
        This makes the use of node objects a bit more convenient for
        implementing LList class.

        Since there are no setters and getters, we use the attributes directly.

        This is safe because the node class is defined in this module.
        No one else will use this version of the class.
    """

    def __init__(self, data, next=None):
        """
        Create a new node for the given data.
        Pre-conditions:
            data:  Any data value to be stored in the node
            next:  Another node (or None, by default)
        """
        self.data = data
        self.next = next
    # Note: use the attributes directly; no setters or getters!