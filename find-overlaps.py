#
# Find overlapping intervals in N*log(N) time
#

# http://stackoverflow.com/questions/4542892/possible-interview-question-how-to-find-all-overlapping-intervals

def overlapping(intervals):
    last = (-1, -1)
    overlapping = set()

    for curr in sorted(intervals, key=lambda p: p[0]):
        if curr[0] < last[1]:
            overlapping.add(curr)
            overlapping.add(last)
        last = max(curr, last, key=lambda p: p[1])

    return list(overlapping - set((-1, -1)))

print overlapping([(1, 3), (12, 14), (2, 4), (13, 15), (5, 10)])
#=> [(1, 3), (13, 15), (2, 4), (12, 14)]


