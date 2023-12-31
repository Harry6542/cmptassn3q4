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
class LList(object):
    def __init__(self):
        """
        Purpose
            creates an empty list
        """
        self._size = 0  # how many elements in the stack
        self._head = None  # the node chain starts here; initially empty
        self._tail = None
        self._temp = None
        self._counter = 0
        self._prev = None
    def is_empty(self):
        """
        Purpose
            Checks if the given list has no data in it
        Return:
            :return True if the list has no data, or False otherwise
        """

        return self._head is None
    def size(self):
        """
        Purpose
            Returns the number of data values in the given list
        Return:
            :return The number of data values in the list
        """
        return self._size

    def prepend(self, val):
        """
        Purpose
            Insert val at the front of the node chain
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            The list increases in size.
            The new value is at index 0.
            The values previously in the list appear after the new value.
        Return:
            :return None
        """
        self._size += 1
        if self.is_empty():
            self._head = node(val)
            self._tail = self._head
        else:
            self._head = node(val, self._head)
    def append(self, val):
        """
        Purpose
            Insert val at the end of the node chain
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            The list increases in size.
            The new value is last in the list.
        Return:
            :return None
        """
        self._size += 1
        if self.is_empty():
            self._head = node(val)
            self._tail = self._head
        else:
            self._tail.next = node(val)
            self._tail = self._tail.next

    def get_index_of_value(self, val):
        """
        Purpose
            Return the smallest index of the given val.
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            none
        Return:
            :return True, idx if the val appears in self
            :return False, None if the vale does not appear in self
        """
        self._temp = self._head
        self._counter = 0
        while self._temp is not None:
            if self._temp.data == val:
                return True, self._counter
            else:
                self._temp = self._temp.next
                self._counter += 1
        return False, None
    def remove_from_front(self):
        """
        Purpose
            Removes and returns the first value
        Post-conditions:
            The list decreases in size.
            The returned value is no longer in in the list.
        Return:
            :return The pair (True, value) if self is not empty
            :return The pair (False, None) if self is empty
        """
        if self.is_empty():
            return False, None
        else:
            self._size -= 1
            self._temp = self._head
            if self._size == 0:
                self._tail = self._head = None
            else:
                self._head = self._head.next
            return True, self._temp.data

    def remove_from_back(self):
        """
        Purpose
            Removes and returns the last value
        Post-conditions:
            The list decreases in size.
            The returned value is no longer in in the list.
        Return:
            :return The pair True, value if self is not empty
            :return The pair False, None if self is empty
        """
        if self.is_empty():
            return False, None
        else:
            self._size -= 1
            self._temp = self._head
            if self._size == 0:
                self._head = self._tail = None
            else:
                self._prev = self._head
                while self._temp != self._tail:
                    self._prev = self._temp
                    self._temp = self._temp.next
                self._tail = self._prev
                self._tail.next = None
            return True, self._temp.data

    def remove_from_back(self, idx):
        """
        Purpose
            Return the value stored at the index idx
        Preconditions:
            :param idx:   a non-negative integer
        Post-conditions:
            none
        Return:
            :return (True, val) if val is stored at index idx and idx is valid
            :return (False, None) if the idx is not valid for the list
        """
        self._temp = self._head
        self._counter = 0
        while self._temp is not None:
            if self._counter == idx:
                return True, self._temp.data
            else:
                self._temp = self._temp.next
                self._counter += 1
        return False, None

    def set_data(self, idx, val):
        """
        Purpose
            Store val at the index idx
        Preconditions:
            :param val:   a value of any kind
            :param idx:   a non-negative integer
        Post-conditions:
            The value stored at index idx changes to val
        Return:
            :return True if the index was valid, False otherwise
        """
        if self.retrieve_data(idx)[0]:
            self._temp.data = val
            return True
        else:
            return False
