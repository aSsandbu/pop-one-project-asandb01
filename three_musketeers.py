# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "m", "r", or "-".
#        "m" = Musketeer, "r" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

import random, math, copy

def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]
       """
    x = ord(s[0])-65
    y = int(s[1])-1
    location = (x, y)
    if not is_legal_location(location):
        raise ValueError
    return location

def location_to_string(location):
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range
    """
    return chr(location[0]+65) + str(location[1]+1)

def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    return at_local(board, location)

def at_local(board_local, location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    return board_local[location[0]][location[1]]

def all_locations():
    """Returns a list of all 25 locations on the board."""
    locations = [(i,j) for i in range(5) for j in range(5)]
    return locations

def player_locations(player):
    return player_locations_local(board, player)

def player_locations_local(board_local, player):
    return [location for location in all_locations() if at_local(board_local, location) == player]

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""
    (row, column) = location
    if direction == 'up':
        row -= 1
    elif direction == 'down':
        row += 1
    elif direction == 'left':
        column -= 1
    elif direction == 'right':
        column += 1
    return (row, column)

def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'"""
    if at(location) == 'M':
        return is_legal_move(location, direction) and is_within_board(location, direction)
    else:
        raise ValueError

def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'R'"""
    if at(location) == 'R':
        return is_legal_move(location, direction) and is_within_board(location, direction)
    else:
        raise ValueError

def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    You can assume that input will always be in correct range."""
    if not is_within_board(location, direction):
        return False
    move = adjacent_location(location, direction)
    if at(location) == 'M' and at(move) == 'R':
        return True
    elif at(location) == 'R' and at(move) == '-':
        return True
    else:
        return False

def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
    You can assume that input will always be in correct range."""
    directions = ['up', 'down', 'left', 'right']
    for dir in directions:
        if is_legal_move(location, dir):
            return True
    return False

def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    You can assume that input will always be in correct range."""
    for location in player_locations(who):
        if can_move_piece_at(location):
            return True
    return False

def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""
    legal_moves = []
    directions = ['up', 'down', 'left', 'right']
    for dir in directions:
        if is_legal_move(location, dir):
            legal_moves.append(dir)
    return legal_moves

def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board.
    You can assume that input will always be in correct range."""
    return 0 <= location[0] <= 4 and 0 <= location[1] <= 4

def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range."""
    move = adjacent_location(location, direction)
    return 0 <= move[0] <= 4 and 0 <= move[1] <= 4

def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples.
       You can assume that input will always be in correct range."""
    possible_moves = [(location, move) for location in player_locations(player)
                                       for move in possible_moves_from(location)]
    return possible_moves

def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range."""
    return make_move_local(board, location, direction)

def make_move_local(local_board, location, direction):
    move = adjacent_location(location, direction)
    local_board[move[0]][move[1]] = at(location)
    local_board[location[0]][location[1]] = '-'

def distance(a, b):
    #math.sqrt() version
    return math.sqrt(abs(a[0] - b[0])) + math.sqrt(abs(a[1] - b[1]))

def musketeer_distance(location, direction):
    board_copy = copy.deepcopy(board)
    make_move_local(board_copy, location, direction)
    locs = player_locations_local(board_copy, 'M')
    d1 = distance(locs[0], locs[1])
    d2 = distance(locs[0], locs[2])
    d3 = distance(locs[1], locs[2])
    mdist = d1 + d2 + d3
    return mdist

def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual.
       You can assume that input will always be in correct range."""
    if who == 'M':
        return random.choice(choose_computer_move_musketeer())
    moves = all_possible_moves_for(who)
    return random.choice(moves)

def choose_computer_move_musketeer():
    moves = all_possible_moves_for('M')
    max_distance = 0
    max_moves = [(0,0)]
    for move in moves:
        distance = musketeer_distance(move[0], move[1])
        if distance > max_distance: #What if two are the same?
            max_move = [(0,0)]
            max_moves[0] = move
            max_distance = distance
        elif distance == max_distance:
            max_moves.append(move)
    return max_moves

def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    loc = player_locations('M')
    if loc[0][0] == loc[1][0] and loc[1][0] == loc[2][0]:
        return True
    if loc[0][1] == loc[1][1] and loc[1][1] == loc[2][1]:
        return True
    return False

#---------- Communicating with the user ----------
#----you do not need to modify code below unless you find a bug
#----a bug in it before you move to stage 3

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')
        make_move(location, direction)
        describe_move("Musketeer", location, direction)

def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break

if __name__ == "__main__":
    start()
