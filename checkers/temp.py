checker = 31
possible_go_cell = []
terms = [11, -11, 9, -9]
borders = [
           18, 28, 38, 48, 58, 68, 78, 88,
           17, 27, 37, 47, 57, 67, 77, 87,
           16, 26, 36, 46, 56, 66, 76, 86,
           15, 25, 35, 45, 55, 65, 75, 85,
           14, 24, 34, 44, 54, 64, 74, 84,
           13, 23, 33, 43, 53, 63, 73, 83,
           12, 22, 32, 42, 52, 62, 72, 82,
           11, 21, 31, 41, 51, 61, 71, 81,
           ]

for term in terms:
    possible_stap_for_queen = checker + term
    temp_possible_go_cell = []
    while possible_stap_for_queen in borders:
        temp_possible_go_cell.append(possible_stap_for_queen)
        possible_stap_for_queen += term
    possible_go_cell.append(temp_possible_go_cell)

print(possible_go_cell)
# print(borders[-8:])#[11, 21, 31, 41, 51, 61, 71, 81] black
# print(borders[:8])#[18, 28, 38, 48, 58, 68, 78, 88] white


