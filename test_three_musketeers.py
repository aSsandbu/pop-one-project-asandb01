import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    #eventually add at least two more test cases

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M
    #eventually add some board2 and at least 3 tests with it

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    assert string_to_location('A1') == (0,0)
    #eventually add at least one more exception test and two more
    #test with correct inputs

def test_location_to_string():
    assert location_to_string((0, 4)) == 'A5'
    assert location_to_string((2,3)) == 'C4'

def test_at():
    create_board()
    assert at((0,0)) == 'R'
    assert at((2,2)) == 'M'

def test_all_locations():
    assert len(all_locations()) == 25
    assert all_locations() == [(0,0), (0,1), (0,2), (0,3), (0,4),
    (1,0), (1,1), (1,2), (1,3), (1,4),
    (2,0), (2,1), (2,2), (2,3), (2,4),
    (3,0), (3,1), (3,2), (3,3), (3,4),
    (4,0), (4,1), (4,2), (4,3), (4,4)]

def test_player_locations():
    assert player_locations('M') == [(0,4), (2,2), (4,0)]

def test_adjacent_location():
    assert adjacent_location((1,1), 'up') == (0,1)
    assert adjacent_location((1,1), 'left') == (1,0)

def test_is_legal_move_by_musketeer():
    assert is_legal_move_by_musketeer((2,2), 'left') == True

def test_is_legal_move_by_enemy():
    assert is_legal_move_by_enemy((1,2), 'right') == False

def test_is_legal_move():
    assert is_legal_move((2,2), 'up') == True
    assert is_legal_move((2,2), 'down') == True
    assert is_legal_move((2,2), 'left') == True
    assert is_legal_move((2,2), 'down') == True

def test_can_move_piece_at():
    assert can_move_piece_at((2,2)) == True
    assert can_move_piece_at((0,0)) == False

def test_has_some_legal_move_somewhere():
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == False
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    assert len(possible_moves_from((2,2))) == 4
    assert possible_moves_from((2,2)) == ['up', 'down', 'left', 'right']

def test_is_legal_location():
    assert is_legal_location((2,2)) == True

def test_is_within_board():
    assert is_within_board((0,0), 'left') == False
    assert is_within_board((0,0), 'down') == True
    assert is_within_board((3,4), 'right') == False

def test_all_possible_moves_for():
    # Returns every possible move for the player ('M' or 'R') as a list(location, direction) tuples.
    assert len(all_possible_moves_for('M')) == 8
    assert all_possible_moves_for('M') == [((0,4), 'down'), ((0,4), 'left'),
    ((2,2), 'up'), ((2,2), 'down'), ((2,2), 'left'), ((2,2), 'right'),
    ((4,0), 'up'), ((4,0), 'right')]

def test_make_move():
    make_move((0,4), 'down')
    assert at((0,4)) == '-'
    assert at((1,4)) == 'M'

def test_distance():
    #Linear distance formula
    '''assert distance((0,0), (4,4)) == 8
    assert distance((0,0), (2,2)) == 4
    assert distance((4,1), (0,3)) == 6'''

    #Sqrt distance formula
    assert distance((0,0), (4,4)) == 4
    assert distance((0,0), (2,2)) == 2 * math.sqrt(2)
    assert distance((4,1), (0,3)) == 2 + math.sqrt(2)

def test_musketeer_distance():
    create_board()
    assert musketeer_distance((2,2), 'left') == 5 + math.sqrt(3) + 2 * math.sqrt(2)
    assert at((2,2)) == 'M'

def test_choose_computer_move_musketeer():
    create_board()
    make_move((2,2), 'up')
    make_move((2,3), 'left')
    assert choose_computer_move_musketeer() == ((1,2), 'down')

def test_choose_computer_move():
    create_board()
    move = choose_computer_move('M')
    assert is_legal_move(move[0], move[1])

def test_is_enemy_win():
    assert is_enemy_win() == False
