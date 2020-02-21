from room import Room
from player import Player
from world import World
from util import Queue, Stack
# from queue import Queue

from typing import Deque
import random
from ast import literal_eval

# Load world
world = World()

# class Queue():
#     def __init__(self):
#         # self.queue = Deque()
#         self.queue = []

#     def enqueue(self, value):
#         self.queue.append(value)

#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop()
#         else:
#             return None

#     def size(self):
#         return len(self.queue)

def bfs(dict, room):
    visited = set()
    q = Queue()
    q.enqueue([current_room])
    directions = []
    path_keeper = ''

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        unvisited = []
        for direction in dict[v]:
            if dict[v][direction] == '?':
                unvisited.append(direction)

        if len(unvisited) > 0:
            path_keeper = path
            break

        if v not in visited:
            visited.add(v)
            for edge in dict[v]:
                node = dict[v][edge]
                path_copy = path.copy()
                path_copy.append(node)
                q.enqueue(path_copy)

    directions = []
    while len(path_keeper) >= 2:
        location = path.pop(0)
        for r in dict[location]:
            if dict[location][r] == path[0]:
                directions.append(r)

    for d in directions:
        player.travel(d)

    return directions

# backup = {'s': 'n', 'n': 's', 'w': 'e', 'e': 'w'}
def backup(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'e':
        return 'w'
    elif direction == 'w':
        return 'e'

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

print(len(room_graph))

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# You may find the commands `player.current_room.id`,
# `player.current_room.get_exits()`
#  `player.travel(direction)` useful.

# Fill this out with directions to walk
traversal_path = []

# def bfs(self, starting_room, rooms_not_explored=499):
# traversal_path = []
q = Queue()
# q.enqueue( [player.current_room.id] )
# visited = set()
visited = {}
steps = 0

# visited[player.current_room.id] = player.current_room.get_exits()

while len(visited) < len(room_graph):
    room = player.current_room.id
    exits = player.current_room.get_exits()
    unvisited = []
    if room not in visited:
    #     visited[room] = {
    #         direction: '?' for direction in player.current_room.get_exits()}
    # unvisited = [direction for direction in visited[room] if visited[room][direction] == '?']
        room_exits = {}
        for doors in exits:
            room_exits[doors] = '?'
        visited[room] = room_exits

    for exit in visited[room]:
        if visited[room][exit] == '?':
            unvisited.append(exit)

    if len(unvisited) > 0:
        # direction = unvisited[(random.choice(len(unvisited)))]
        direction = unvisited[(random.randint(0, len(unvisited) - 1))]
        player.travel(direction)

        traversal_path.append(direction)

        current_room = player.current_room.id
        current_exits = player.current_room.get_exits()
        # visited[room][direction] = current_room

        if current_room not in visited:
        #     visited[current_room] = {direction: '?' for direction in player.current_room.get_exits()}
            new_exits = {}
            for door in current_exits:
                new_exits[door] = '?'
            visited[current_room] = new_exits

        turn_around = backup(direction)
        visited[room][direction] = current_room
        visited[current_room][turn_around] = room

    else:
        directions = bfs(visited, player.current_room)
        # traversal_path = traversal_path.add(directions)
        # traversal_path.append(directions)
        # traversal_path = traversal_path + directions
        # for direction in directions:
        #     player.travel(direction)
        if len(directions) > 0:
            for d in directions:
                traversal_path.append(d)


    # if player.current_room.id not in visited:
    #     visited[player.current_room.id] = player.current_room.get_exits()
    #     v = traversal_path[-1]
    #     visited[player.current_room.id].remove(v)

    # while len(visited[player.current_room.id]) < 1:
    #     previous_direction = traversal_path.pop()
    #     traversal_path.append(previous_direction)
    #     player.travel(previous_direction)

    # backup = {'s': 'n', 'n': 's', 'w': 'e', 'e': 'w'}
    # move = visited[player.current_room.id].pop(0)
    # traversal_path.append(move)
    # traversal_path.append(backup[move])
    # player.travel(move)

# while q.size() > 0:
#     room = player.current_room.id
#     if room not in visited:
#         visited[room] = {
#             direction: '?' for direction in player.current_room.get_exits()
#         }
#         unvisited = [direction for direction in visited[room] if visited[room][direction] == '?']

#     if unvisited is not None:
#         direction = random.choice(unvisited)
#         player.travel(direction)
#         traversal_path.append(direction)

#         current_room = player.current_room.id
#         visited[room][direction] = current_room

#         if current_room not in visited:
#             visited[current_room] == 

# print(q)
# while player.current_room.get_exits() is not None:
# while q.size() > 0:
    # # steps += 1
    # path = q.dequeue()
    # exits = player.current_room.get_exits()
    # room = path[-1]
    # if exits == 'n':
    #     player.travel('n')
    #     visited.add(player.current_room.id)
    #     q.enqueue( [player.current_room.id] )
    #     if room not in visited:
    #         random_route = random.choice(exits)
    #         player.travel(random_route)
    #         # new_room = player.current_room
    #         # visited.add(player.current_room.id)
    # print(visited)

    # path = q.dequeue()
    # if path not in visited:
    #     visited.add(path)
    #     print(player.current_room.get_exits()[1])

# while q.size > 0:
#     steps += 1
#     print(counter)
#     path = q.dequeue()
#     v = path[-1]
#     if rooms_not_explored == 0:
#         return path
#     if v not in visited:
#         visited.add(v)
#         for neighbor in self.get_neighbors(v):
#             path_copy = path.copy()
#             path_copy.append(neighbor)
#             q.enqueue(path_copy)

# traversal_path.append('n')
# traversal_path.append('n')

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# ######
# UNCOMMENT TO WALK AROUND
# ######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
