# coding=utf-8


def main(step, initial):
    state = {'left': [], 'right': []}
    result = []
    for k, v in enumerate(initial):
        if v == 'L':
            state['left'].append(k)
        elif v == 'R':
            state['right'].append(k)

    while True:
        print state
        current = []
        empty = True
        for i in range(len(initial)):
            if i not in state['left'] and i not in state['right']:
                current.append('.')
            else:
                empty = False
                current.append('x')
        result.append(''.join(current))
        if empty:
            break

        # move
        for k, v in enumerate(state['left']):
            if v and v >= 2:
                state['left'][k] -= 2
            else:
                state['left'][k] = None
        for k, v in enumerate(state['right']):
            if v and v <= len(initial) - 3:
                state['right'][k] += 2
            else:
                state['right'][k] = None
    return result


if __name__ == '__main__':
    # step = int(raw_input('type step: '))
    # initial = raw_input('type a initial state: ')
    step = 2
    initial = 'LRLR.LRLR'
    for i in main(step, initial):
        print i
