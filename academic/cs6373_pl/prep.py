
source = 'review-final.md'

questions = []
with open(source, 'r') as sourcefile:
    data = sourcefile.read()
    for i in data.split('#####'):
        questions.append((i.split('\n')[0], '\n'.join(i.split('\n')[1:])))

results = {}
# print questions
from random import shuffle
try:
    while True:
        shuffle(questions)
        question = questions[0]
        # print question
        i = raw_input(question[0] + '. Do you know this? Yes/No')
        results[question[0]] = i
        print question[1]
except KeyboardInterrupt:
    with open('result.log', 'wb') as w:
        for r in results:
            w.write(results[r] + ' >>> ' + r + '\n')

