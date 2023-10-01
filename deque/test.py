from collections import deque
from termcolor import colored

from main import Deque, QueueEmptyException


def check_queue_equivalent(q0: deque, q1: Deque) -> bool:
    q1 = q1.to_array()

    if len(q0) != len(q1):
        return False

    for i in range(len(q0)):
        if q0[i] != q1[i]:
            return False

    return True


cases = [
    [('f', 0), ('f', 1), ('f', 2)],       # 0
    [('f', 0), ('b', 1), ('b', 2)],       # 1
    [('b', 0), ('b', 1), ('b', 2)],       # 2
    [('b', 0), ('f', 1), ('f', 2)],       # 3
    [('b', 0), ('b', 1), 'b', ('b', 2)],  # 4
    [('b', 0), ('b', 1), 'f', ('b', 2)],  # 5
    [('b', 0), ('b', 1), 'b', 'b'],       # 6
    [('b', 0), ('b', 1), 'f', 'f'],       # 7
    [('b', 0), 'b', 'b'],                 # 8
    [('f', 0), 'f', 'f'],                 # 9
]

q0 = deque()
q1 = Deque()


for case_i, case in enumerate(cases):
    print(f'\n=== Case: {case_i} ===')
    for step_i, step in enumerate(case):

        # push
        if isinstance(step, tuple):
            op, n = step
            if op == 'f':
                q0.appendleft(n)
                q1.push_front(n)
            else:
                q0.append(n)
                q1.push_back(n)

        # pop
        else:
            if step == 'f':
                try:
                    q0.popleft()
                except IndexError:
                    print('q0 is empty')
                try:
                    q1.pop_front()
                except QueueEmptyException:
                    print('q1 is empty')
            else:
                try:
                    q0.pop()
                except IndexError:
                    print('q0 is empty')
                try:
                    q1.pop_back()
                except QueueEmptyException:
                    print('q1 is empty')

        # check
        if not check_queue_equivalent(q0, q1):
            print(colored(f'Case {case_i}, step {step_i} failed', 'red'))
            print(q0)
            print(q1.to_array())
            break

    else:
        print(colored(f'Case {case_i} success', 'green'))
