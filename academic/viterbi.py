TAGS = ['NNP', 'NN', 'TO', 'VB']

A = [
    [.003, .004, .23, .35],
    [.07, .08, .28, .36],
    [.1, .08, .00001, .4],
    [.2, .12, .3, .28],
]

# for i in range(len(A)):
#     for j in range(len(A[0])):
#         A[i][j] /= sum(A[i])

S = [.2, .3, .09, .3]
for i in S:
    print i/sum(S)

B = [
    [.008, .0004, .005],
    [.3, .0, .4],
    [.0, .8, .0],
    [.6, .0, .5],
]

C = [0.15, 0.3, 0.15, 0.35]

# for i in range(len(B)):
#     for j in range(len(B[0])):
#         B[i][j] /= C[i] / sum(C)

v = [[0] * 3 for i in TAGS]
bp = [[0] * 3 for i in TAGS]

# init
for s in range(len(TAGS)):
    v[s][0] = (S[s] / sum(S)) * B[s][0]
    bp[s][0] = ''

for t in range(1, 3):
    for s in range(len(TAGS)):
        bpvalue = 0
        for s_before in range(len(TAGS)):
            if v[s_before][t-1] * A[s_before][s] > bpvalue:
                bpvalue = v[s_before][t-1] * A[s_before][s]
                bp[s][t] = TAGS[s_before]
            v[s][t] = max(v[s_before][t-1] * A[s_before][s] * B[s][t], v[s][t])

for i in v:
    print i

for i in bp:
    print i
