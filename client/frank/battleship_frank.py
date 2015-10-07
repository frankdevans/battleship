import sys


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
    def __str__(self):
        rep = {
            'hit':'H',
            'miss':'M',
            'shot': 'S',
            'empty':'_'
        }
        collector = []
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                status = self.opp_board[(x,y)]
                collector.append(rep[status])
                collector.append(' ')
            collector.append('\n')
        return ''.join(collector)
    def set_grid(self, w, h):
        self.grid_width = w
        self.grid_height = h
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                self.my_board[(x,y)] = 'empty'
                self.opp_board[(x,y)] = 'empty'
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
    def can_opp_ship_fit(self, x, y, pos, size):
        pass
    def place_ships(self):
        # Hardcode 5 ships
        self.ship_locations.append((0,2,'H'))  # 2 Destroyer
        self.ship_locations.append((0,6,'V'))  # 3 Submarine
        self.ship_locations.append((7,0,'V'))  # 3 Battleship
        self.ship_locations.append((6,5,'H'))  # 4 Cruiser
        self.ship_locations.append((4,9,'H'))  # 5 Carrier
    def get_ship_locations(self):
        return self.ship_locations
    def get_surrounding_cells(self, x, y):
        collector = []
        if (x + 1, y) in self.opp_board:
            collector.append((x + 1, y))
        if (x - 1, y) in self.opp_board:
            collector.append((x - 1, y))
        if (x, y + 1) in self.opp_board:
            collector.append((x, y + 1))
        if (x, y - 1) in self.opp_board:
            collector.append((x, y - 1))
        return collector
    def get_diagonal_cells(self, x, y):
        collector = []
        if (x + 1, y + 1) in self.opp_board:
            collector.append((x + 1, y + 1))
        if (x + 1, y - 1) in self.opp_board:
            collector.append((x + 1, y - 1))
        if (x - 1, y + 1) in self.opp_board:
            collector.append((x - 1, y + 1))
        if (x - 1, y - 1) in self.opp_board:
            collector.append((x - 1, y - 1))
        return collector
    def get_shots(self, num_shots):
        collector = []
        # Get orphan hits
        for i in self.opp_board:
            if self.opp_board[i] == 'hit':
                surr = self.get_surrounding_cells(x = i[0], y = i[1])
                for c in surr:
                    if self.opp_board[c] == 'empty':
                        collector.append(c)

        #TODO: Expectorization Max

        # Normal Search Grid
        for i in self.opp_board:
            if self.opp_board[i] in ('miss','shot'):
                diag = self.get_diagonal_cells(x = i[0], y = i[1])
                for c in diag:
                    if self.opp_board[c] == 'empty':
                        collector.append(c)
                        self.record_shot(c[0], c[1], 'shot')


        # remove shots with miss on all 4 sides
        delete_shots = []
        for i in collector:
            surr = self.get_surrounding_cells(x = i[0], y = i[1])
            misses = 0
            for c in surr:
                if self.opp_board[c] in ('miss','shot'):
                    misses += 1
            if (misses == len(surr)) or (self.opp_board[i] == 'hit'):
                delete_shots.append(i)
                self.record_shot(i[0], i[1], 'empty')

        for i in delete_shots:
            collector.remove(i)

        # Check for reserved shots
        for i in self.opp_board:
            if (self.opp_board[i] == 'shot') and (i not in collector):
                collector.append(i)

        # Default Starter
        if len(collector) == 0:
            collector.append((5,5))
            collector.append((4,4))
            collector.append((3,3))
            collector.append((6,6))
            collector.append((7,7))

        return collector[:num_shots]


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
            ) for loc in board.get_ship_locations()]
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
        #print board
        line = raw_input()
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


if __name__ == '__main__':
    game_loop()
