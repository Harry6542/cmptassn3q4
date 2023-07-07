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
    if container_type == 's':
        container = Stack()
    elif container_type == 'q':
        container = Queue()

    while True:
        command = input("Please enter a command: ")

        if command == 'add':
            value = input("Please enter a value to add: ")
            container.push(value)
        elif command == 'peak':
            if container.is_empty():
                print("Container is empty")
            else:
                print(container.peek())
        elif command == 'remove':
            if container.is_empty():
                print("Container is empty")
            else:
                print(container.pop())
        elif command == 'help':
            print("Possible actions: ")
            print("- add: Add a value to the container")
            print("- peak: Get the first value in the container")
            print("- remove: Remove the first value from the container")
            print("- help: Print available actions")
            print("- quit: End the program")
        elif command == 'quit':
            print("Goodbye.")
            break
        else:
            print("Invalid command. Type 'help' to see available actions.")
if __name__ == "__main__":
    main()