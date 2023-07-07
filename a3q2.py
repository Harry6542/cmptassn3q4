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
#    Question nodechain_tostring starter code
#Name-Harry Patel
#NSID-ozc189
#studentNumber-11358887
#course-CMPT145
import node as n


def to_string(node_chain):
    """
        Create a string representation of the node chain. E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
        """
    # special case: empty node chain
    if node_chain is None:
        return 'EMPTY'

    # walk along the chain
    walker = node_chain
    result = '[ {} |'.format(str(walker.get_data()))
    while walker.get_next() is not None:
        walker = walker.get_next()
        value = walker.get_data()
        # represent the next with an arrow-like figure
        result += ' *-]-->[ {} |'.format(str(value))


