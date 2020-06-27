class Cell:
    def __init__(self, cell_info):
        self.status_value = cell_info[0]
        self.value = cell_info[1]

    def is_flagged(self):
        if self.status_value == 4:
            return True
        else:
            return False

    def get_cell_info(self):
        return [self.status_value, self.value]


game_board = [Cell([1, 2]), Cell([2, 3]), Cell([3, 4]), Cell([4, 5])]


def get_flagged_cells():
    flagged_cells = list()

    for cell in game_board:
        if cell.is_flagged():
            flagged_cells.append(cell)
    return flagged_cells


if __name__ == "__main__":
    for flagged_cell in get_flagged_cells():
        print(flagged_cell.get_cell_info())
