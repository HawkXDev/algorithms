from collections import deque

my_graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [], "peggy": [], "thom": [], "jonny": []
}


def person_is_seller(name):
    return name[-1] == 'm'


def breadth_first_search(graph):
    search_queue = deque()  # Creating a new queue
    search_queue += graph["you"]  # All neighbors are added to the search queue
    searched = []  # This array is used to track already verified people

    while search_queue:  # While the queue is not empty...
        person = search_queue.popleft()  # The first person is removed from the queue
        if person not in searched:  # A person is checked only if he has not been checked before
            if person_is_seller(person):  # We check whether this person is a mango seller
                print(person + " is а mango seller!")  # Yes, it's a mango seller
                return True
            else:
                search_queue += graph[person]  # No, it is not. All the friends of this person are added to the search queue
                searched.append(person)  # The person is marked as already verified

    return False  # If the execution has reached this line, then there is no mango seller in the queue


print(breadth_first_search(my_graph))
