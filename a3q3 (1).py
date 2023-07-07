# CMPT 145 Course material
# Copyright (c) 2017-2023 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#    Question nodechain_sumcountreplace starter code

import node as n


#Name-Harry Patel
#NSID-ozc189
#studentNumber-11358887
#course-CMPT145

import node as n
import a3q2
from a3q2 import to_string
def sumnc(node_chain):
    """
    Purpose:
    Given a node chain with numeric data values, calculate
    the sum of the data values.
    Pre-conditions:
    :param node_chain: a node-chain, possibly empty, containing
    numeric data values
    Post-condition:
    None
    Return
    :return: the sum of the data values in the node chain
    """
    if node_chain is None:
        return 0

    current = node_chain
    total_sum = 0

    while current is not None:
        total_sum += current.get_data()
        current = current.get_next()

    return total_sum


empty_chain = None
chain = n.Node(1, n.Node(2, n.Node(3)))
print('empty chain has the sum', sumnc(empty_chain))
print('chain has the sum', sumnc(chain))
def count_in(node_chain, value):
    """
    Purpose:
    Counts the number of times a value appears in a node chain
    Pre-conditions:
    :param node_chain: a node chain, possibly empty
    :param value: a data value
    Return:
    :return: The number times the value appears in the node chain
    """
    count = 0
    current = node_chain

    while current is not None:
        if current.get_data() == value:
            count += 1
        current = current.get_next()

    return count


empty_chain = None
chain = n.Node(1, n.Node(2, n.Node(1)))

print('empty chain has', count_in(empty_chain, 1), 'occurrences of the value 1')
print('chain has', count_in(chain, 1), 'occurrences of the value 1')
