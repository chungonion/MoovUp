from copy import deepcopy

routes = {"A": ["B", "D", "H"],
          "B": ["A", "C", "D"],
          "C": ["B", "D", "F"],
          "D": ["A", "B", "C", "E"],
          "E": ["D", "F", "H"],
          "F": ["C", "E", "G"],
          "G": ["F", "H"],
          "H": ["A", "E", "G"]
          }

start = "A"
end = "H"


# def next_hop(origin: list[str], current: str): # For reference on typing, this line only works with python >=3.9
def next_hop(origin, current):
    # get the possible nodes for the node currently in
    next_route = routes[current]
    possible_routes = []
    # add the current node in the path
    origin.append(current)
    for i in next_route:
        # reached destination => successful path
        if current == end:
            possible_routes.append(deepcopy(origin))
            return deepcopy(possible_routes)
        # Loop => ignore that node
        if i in origin:
            continue
        # concat the results with those in recusion
        possible_routes = possible_routes + next_hop(deepcopy(origin), deepcopy(i))

    # return possible_routes
    return deepcopy(possible_routes)


def q1_1():
    result = next_hop([], "A")
    return result


def q1_2():
    q1_result = q1_1()
    # base on result of all possible paths, get the min length of possible paths
    q2_result = min([len(i) for i in q1_result])
    return q2_result
    pass


# if __name__ == '__main__':
print(q1_1())
print(q1_2())
