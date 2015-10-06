import sys, random


PLAYER_NAME = sys.argv[1]

class Board:
    def __init__(self):
        self.num_ships = 0
        self.grid_width = 0
        self.grid_height = 0
        self.num_ships = 0
        self.ship_sizes = []
        self.ship_locations = []
        self.my_board = {}
        self.opp_board = {}
    def set_grid(self, w, h):
        self.grid_width = w
        self.grid_height = h
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                my_board[(x,y)] = 'empty'
                opp_board[(x,y)] = 'empty'
        return
    def set_num_ships(self, ships):
        self.num_ships = ships
        return
    def get_num_ships(self):
        return self.num_ships
    def set_ship_sizes(self, sizes):
        self.ship_sizes = sizes
        return
    def record_shot(self, x, y, result):
        self.opp_board[(x,y)] = result
    def can_ship_fit(self, x, y, pos, size):
        pass
    def place_ships(self):
        pass
    def get_ship_locations(self):
        return self.ship_locations
    def get_shots(self, num_shots):
        pass # array of tuples





def parse_info(board, message):
    if message[1] == 'grid size':
        coords = message[2].split(' ')
        board.set_grid(w = int(coords[0]), h = int(coords[1]))
    elif message[1] == 'num ships':
        board.set_num_ships(int(message[2]))
    elif message[1] == 'ship size':
        num_ships = board.get_num_ships()
        sizes = message[2:2 + num_ships]
        sizes = [int(i) for i in sizes]
        board.set_ship_sizes(sizes)
    elif message[1] == 'you hit':
        coords = message[2].split(' ')
        board.record_shot(
            x = int(coords[0]),
            y = int(coords[1]),
            result = 'hit'
        )
    elif message[1] == 'you miss':
        coords = message[2].split(' ')
        board.record_shot(
            x = int(coords[0]),
            y = int(coords[1]),
            result = 'miss'
        )
    return
def parse_query(board, message):
    if message[1] == 'ship locations':
        board.place_ships()
        locations = ['{x} {y} {p}'.format(
            x = loc[0],
            y = loc[1],
            p = loc[2]
            ) for loc in get_ship_locations()]
        locs_string = '|'.join(locations)
        response = '|RESPONSE|ship locations|{locs}|END|\n'.format(
            locs = locs_string
        )
        sys.stdout.write(response)
        return
    elif message[1] == 'shots':
        shots = ['{x} {y}'.format(x = loc[0], y = loc[1])
            for loc in board.get_shots(int(message[2]))]
        shots_string = '|'.join(shots)
        response = '|RESPONSE|shots|{locs}|END|\n'.format(
            locs = shots_string
        )
        sys.stdout.write(response)
        return
    else:
        return
def game_loop():
    board = Board()
    while True:
        line = raw_input().strip('\n')
        assert(line.endswith("|END|"))
        if line == "|INFO|end game|END|":
            return

        parsed = line.strip('|').split('|')
        if parsed[0] == 'INFO':
            parse_info(board, parsed)
        elif parsed[0] == 'QUERY':
            parse_query(board, parsed)
        else:
            error_message = "Unknown command (Frank): {line}".format(line = line)
            sys.stderr.write(error_message)
            return






#-------------------------------------------------------------
#Unit Tests
board = Board()
print board.grid_width
board.set_grid(3,4)
print board.grid_width
