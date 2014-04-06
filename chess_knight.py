# CaptureThemAll
#
# http://community.topcoder.com/stat?c=problem_statement&pm=2915&rd=5853

def gen_move(pos):
    for move in [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2]]:
        x = pos[0] + move[0]
        y = pos[1] + move[1]
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            yield [x, y]

def dist(a, b):
    if a == b:
        return 0

    a = [ord(a[0])-ord("a"), ord(a[1])-ord("0")-1]
    b = [ord(b[0])-ord("a"), ord(b[1])-ord("0")-1]

    open = [a]
    closed = {}
    closed[a[0]*8+a[1]] = True
    count = 0

    while open:
        new_open = []
        count += 1

        for pos in open:
            for new in gen_move(pos):
                if closed.get(new[0]*8+new[1]):
                    continue
                if new == b:
                    return count
                closed[new[0]*8+new[1]] = pos
                new_open.append(new)

        open = new_open

    return -1

def knight_run(knight, rook, queen):
    d_r = dist(knight, rook)
    d_q = dist(knight, queen)
    d_rq = dist(rook, queen)

    if d_r < d_q:
        return d_r + d_rq
    else:
        return d_q + d_rq

print knight_run("a1", "b3", "c5")
print knight_run("b1", "c3", "a3")
print knight_run("a1", "a2", "b2")
print knight_run("a5", "b7", "e4")
print knight_run("h8", "e2", "d2")
