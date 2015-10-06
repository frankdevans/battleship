#-------------------------------------------------------------
#Unit Tests


board = Board()
board.set_grid(10,10)
print board
for i in board.get_shots(5):
    board.record_shot(i[0], i[1], 'miss')
print board
shots = board.get_shots(4)
for i in shots[1:]:
    board.record_shot(i[0], i[1], 'miss')
board.record_shot(shots[0][0], shots[0][1], 'hit')
print board
for i in board.get_shots(5):
    board.record_shot(i[0], i[1], 'miss')
print board
for i in board.get_shots(5):
    board.record_shot(i[0], i[1], 'miss')
print board
for i in board.get_shots(5):
    board.record_shot(i[0], i[1], 'miss')
print board
for i in board.get_shots(5):
    board.record_shot(i[0], i[1], 'miss')
print board
for i in board.get_shots(5):
    board.record_shot(i[0], i[1], 'miss')
print board
for i in board.get_shots(5):
    board.record_shot(i[0], i[1], 'miss')
print board


board = Board()
board.set_grid(10,10)
print board
shots = board.get_shots(5)
print shots
for i in shots:
    board.record_shot(i[0], i[1], 'miss')
print board
shots = board.get_shots(4)
for i in shots:
    board.record_shot(i[0], i[1], 'miss')
print board
shots = board.get_shots(4)
for i in shots:
    board.record_shot(i[0], i[1], 'miss')
print board


board = Board()
board.set_grid(10,10)
print board
print board.get_shots(5)
board.record_shot(4,4,'miss')
board.record_shot(5,5,'miss')
board.record_shot(3,3,'hit')
board.record_shot(6,6,'hit')
board.record_shot(7,7,'miss')
print board
shots = board.get_shots(4)
print shots
for i in shots:
    board.record_shot(i[0], i[1], 'miss')
print board
shots = board.get_shots(4)
for i in shots:
    board.record_shot(i[0], i[1], 'miss')
print board


board = Board()
board.set_grid(10,10)
print board.get_shots(5)
print board
board.record_shot(4,4,'miss')
board.record_shot(5,5,'miss')
board.record_shot(3,3,'hit')
board.record_shot(6,6,'hit')
board.record_shot(7,7,'miss')
print board.opp_board
print board.get_shots(4)


board = Board()
board.set_grid(10,10)
print board.opp_board


board = Board()
print board.grid_width
board.set_grid(3,4)
print board.grid_width


board = Board()
board.place_ships()
print board.get_ship_locations()
