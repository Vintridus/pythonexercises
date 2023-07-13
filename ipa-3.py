'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    namelist = list(social_graph.keys())
    personA = ''
    personB = ''
    followA = False
    followB = False
    for i in range(0,len(social_graph)):
        if f'{social_graph[namelist[i]]["first_name"]} {social_graph[namelist[i]]["last_name"]}' == from_member:
            personA += namelist[i]
        if f'{social_graph[namelist[i]]["first_name"]} {social_graph[namelist[i]]["last_name"]}' == to_member:
            personB += namelist[i]
    for i in range(0,len(social_graph[personA]["following"])):
        if social_graph[personA]["following"][i] == personB:
            followA = True
    for i in range(0,len(social_graph[personB]["following"])):
        if social_graph[personB]["following"][i] == personA:
            followB = True
    if followA + followB == 2:
        return "friends"
    elif followA == True and followB == False:
        return "follower"
    elif followA == False and followB == True:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    winner = ""
    size = len(board)
    players = ["X","O"]
    for check in players:
        for i in range(0,size):
            row = board[i]
            if row.count(check) == size:
                winner = check
            column = []
            for j in range(0, size):
                column += board[j][i]
            if column.count(check) == size:
                winner = check
            diagonal = []
            for j in range(0, size):
                diagonal += board[j][j]
            if diagonal.count(check) == size:
                winner = check
            diagonal2 = []
            for j in range(0, size):
                diagonal2 += board[j][size-1-j]
            if diagonal2.count(check) == size:
                winner = check
    if winner == "":
        return "NO WINNER"
    statement = f'{check}'
    return statement

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    routelist = list(route_map.keys())
    time = 0
    current = first_stop
    while current != second_stop:
        for i in range(0, len(routelist)):
            if current == routelist[i][0]:
                time += route_map[routelist[i]]["travel_time_mins"]
                current = routelist[i][1]
            if current == second_stop:
                return time
    return time
