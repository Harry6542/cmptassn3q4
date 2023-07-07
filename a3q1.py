#Name-Harry Patel
#NSID-ozc189
#studentNumber-11358887
#course-CMPT145
import sys
from Stack import Stack
from Queue import Queue


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ['s', 'q']:
        print("Usage: python3 a3q1.py <container_type>")
        print("Container types: 's' for stack, 'q' for queue")
        return

    container_type = sys.argv[1]
    container = None