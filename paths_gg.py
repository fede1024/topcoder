#
# Given a matrix, find the longest sequence of consecutive (horizontally,
# vertically) cells, such that each cell value is +1 or -1 in respect
# to the previous one (example: 1 2 1 2 3)
#

# Returns a sequence of valid moves, given position 'pos' and matrix 'm'
def gen_moves(pos, m):
    w = len(m[0])
    h = len(m)
    l = []
    for move in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        x = pos[0] + move[0]
        y = pos[1] + move[1]
        if x >= 0 and x < w and y >= 0 and y < h\
           and abs(m[y][x]-m[pos[1]][pos[0]]) == 1:
            l.append([x, y])
    return l

# Returns the longest path starting from position 'pos'
def paths_from(pos, m):
    paths = []

    moves = gen_moves(pos, m)
    tmp = m[pos[1]][pos[0]]
    m[pos[1]][pos[0]] = -10

    for new in moves:
        paths.append([new] + paths_from(new, m))

    m[pos[1]][pos[0]] = tmp

    if paths:
        return max(paths, key=len)
    else:
        return []

# Returns the longest path, given 'm'
def longest_path(m):
    paths = []

    for x in xrange(len(m[0])):
        for y in xrange(len(m)):
            paths.append([[x, y]] + paths_from([x, y], m))

    return max(paths, key=len)

m = [[2, 3, 2, 1],
     [2, 3, 2, 1],
     [4, 2, 3, 2]]

longest_path(m)
# => [[0, 1], [1, 1], [1, 2], [2, 2], [2, 1], [3, 1], [3, 2]]

m = [[2, 4, 3, 1],
     [2, 3, 2, 1],
     [3, 2, 3, 2],
     [2, 3, 4, 1]]

longest_path(m)
# => [[0, 1],
#     [0, 2],
#     [0, 3],
#     [1, 3],
#     [2, 3],
#     [2, 2],
#     [1, 2],
#     [1, 1],
#     [1, 0],
#     [2, 0],
#     [2, 1],
#     [3, 1],
#     [3, 2],
#     [3, 3]]

