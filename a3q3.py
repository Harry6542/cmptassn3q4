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
def replace_in(node_chain, target, replacement):
    """
    Purpose:
    Replaces each occurrence of the target value with the replacement
    Pre-conditions:
    :param node_chain: a node-chain, possibly empty
    :param target: a value that might appear in the node chain
    :param replacement: the value to replace the target
    Post-conditions:
    Each occurrence of the target value in the chain is replaced with
    the replacement value.
    Return:
    None
    """
    current = node_chain

    while current is not None:
        if current.get_data() == target:
            current.set_data(replacement)
        current = current.get_next()
chain1 = n . Node (1 ,
n . Node (1 ,
n . Node (9)))
chain2 = n . Node (2 ,
n . Node (7 ,
n . Node (15)))
print ( ' chain1 before : ' , to_string ( chain1 ))
replace_in ( chain1 , 1 , 10)
print ( ' chain1 after : ' , to_string ( chain1 ))
print ( ' chain2 before : ' , to_string( chain2 ))
replace_in ( chain2 , 7 , 1007)
print ( ' chain2 after : ' , to_string ( chain2 ))
