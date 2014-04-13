# http://community.topcoder.com/stat?c=problem_statement&pm=3935&rd=6532

def constrained(word, constraints):
    for c in constraints:
        if word[0] in c[0] and word[1] in c[1] and\
           word[2] in c[2] and word[3] in c[3]:
            return 1
    return 0

def inc_c(c):
    return chr((ord(c)-97+1)%26+97)

def dec_c(c):
    return chr((ord(c)-97-1)%26+97)

def toy(start, finish, cons):
    if start == finish:
        return 0

    cons = [x.split() for x in cons]

    found = {}
    found[start] = 1
    curr = [start]
    it = 0

    while curr:
        new = []

        for word in curr:
            for i in xrange(0, 4):
                new.append(word[:i] + inc_c(word[i]) + word[i+1:])
                new.append(word[:i] + dec_c(word[i]) + word[i+1:])

        curr = []
        for word in new:
            if word == finish:
                return it+1
            if not constrained(word, cons) and not found.get(word):
                found[word] = 1
                curr.append(word)

        it += 1

    return -1

cons = ["a a a z", "a a z a", "a z a a", "z a a a", "a z z z", "z a z z", "z z a z", "z z z a"]
toy("aaaa", "zzzz", cons)

toy("aaaa", "bbbb", [])

toy("aaaa", "bbbb", ["bz a a a", "a bz a a", "a a bz a", "a a a bz"])

toy("aaaa", "mmnn", [])

import time
start_time = time.time()
toy("mmma", "yyyy", ["qwertyuiopasdfg qwertyuiopasdfg qwertyuiopasdfg z", "qwertyuiopasdfg qwertyuiopasdfg hjklzxvcbnm z", "qwertyuiopasdfg hjklzxvcbnm qwertyuiopasdfg z", "qwertyuiopasdfg hjklzxvcbnm hjklzxvcbnm z", "hjklzxvcbnm qwertyuiopasdfg qwertyuiopasdfg z", "hjklzxvcbnm qwertyuiopasdfg hjklzxvcbnm z", "hjklzxvcbnm hjklzxvcbnm qwertyuiopasdfg z", "hjklzxvcbnm hjklzxvcbnm hjklzxvcbnm z", "qwertyuiopasdfg qwertyuiopasdfg z qwertyuiopasdfg", "qwertyuiopasdfg qwertyuiopasdfg z hjklzxvcbnm", "qwertyuiopasdfg hjklzxvcbnm z qwertyuiopasdfg", "qwertyuiopasdfg hjklzxvcbnm z hjklzxvcbnm", "hjklzxvcbnm qwertyuiopasdfg z qwertyuiopasdfg", "hjklzxvcbnm qwertyuiopasdfg z hjklzxvcbnm", "hjklzxvcbnm hjklzxvcbnm z qwertyuiopasdfg", "hjklzxvcbnm hjklzxvcbnm z hjklzxvcbnm", "qwertyuiopasdfg z qwertyuiopasdfg qwertyuiopasdfg", "qwertyuiopasdfg z qwertyuiopasdfg hjklzxvcbnm", "qwertyuiopasdfg z hjklzxvcbnm qwertyuiopasdfg", "qwertyuiopasdfg z hjklzxvcbnm hjklzxvcbnm", "hjklzxvcbnm z qwertyuiopasdfg qwertyuiopasdfg", "hjklzxvcbnm z qwertyuiopasdfg hjklzxvcbnm", "hjklzxvcbnm z hjklzxvcbnm qwertyuiopasdfg", "hjklzxvcbnm z hjklzxvcbnm hjklzxvcbnm", "z qwertyuiopasdfg qwertyuiopasdfg qwertyuiopasdfg", "z qwertyuiopasdfg qwertyuiopasdfg hjklzxvcbnm", "z qwertyuiopasdfg hjklzxvcbnm qwertyuiopasdfg", "z qwertyuiopasdfg hjklzxvcbnm hjklzxvcbnm", "z hjklzxvcbnm qwertyuiopasdfg qwertyuiopasdfg", "z hjklzxvcbnm qwertyuiopasdfg hjklzxvcbnm", "z hjklzxvcbnm hjklzxvcbnm qwertyuiopasdfg", "z hjklzxvcbnm hjklzxvcbnm hjklzxvcbnm", "n ablm ablm abcdefghijkl", "n ablm abcdefghijkl ablm", "n abcdefghijkl ablm ablm", "abcdefghijklm n abcdefghijklm abcdefghijklm", "abcdefghijklm abcdefghijklm n abcdefghijklm", "abcdefghijklm abcdefghijklm abcdefghijklm n", "bcdefghijklm bcdefghijkl ablm ablm", "abcdefghijkl ablm bcdefghijkl ablm", "ablm bcdefghijklm bcdefghijkl ablm", "abcdefghijkl ablm ablm bcdefghijkl", "ablm abcdefghijkl ablm bcdefghijkl", "ablm ablm bcdefghijklm bcdefghijkl"])
print time.time() - start_time, "seconds"
