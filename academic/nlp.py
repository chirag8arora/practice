tennis = {
    "referee": 4,
    "spin": 3,
    "net": 5,
    "player": 2,
    "serve": 2,
    "hit": 2,
    "fault": 3,
    "ball": 4,
    "bat": 5,
    "winner": 3,
    "call": 0,
}

pingpong = {
    "referee": 1,
    "spin": 5,
    "net": 2,
    "player": 3,
    "serve": 4,
    "hit": 5,
    "fault": 2,
    "ball": 1,
    "bat": 2,
    "winner": 7,
    "call": 0,
}


c = "player serve spin ball ball hit net referee call fault winner fault referee"

t, p = 1, 1
s = set()
for i in c.split(' '):
    s.add(i)
    t *= float(tennis[i]+1)/44
    # print 'tennis', i, float(tennis[i]+1)/44
    p *= float(pingpong[i]+1)/43
    # print 'pingpong', i, float(pingpong[i]+1)/43
print t, p, t/p

for i in s:
    print i, c.count(i)
