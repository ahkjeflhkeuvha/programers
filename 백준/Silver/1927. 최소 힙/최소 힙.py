import sys

N = int(input())

min_heap = [None]

def swap(a, b):
    global min_heap
    min_heap[a], min_heap[b] = min_heap[b], min_heap[a]

def push(n):
    global min_heap
    min_heap.append(n)
    cur_idx = len(min_heap) - 1
    par_idx = cur_idx // 2

    while cur_idx > 1 and min_heap[cur_idx] < min_heap[par_idx]:
        swap(cur_idx, par_idx)
        cur_idx = par_idx
        par_idx = cur_idx // 2

def pop():
    global min_heap

    if len(min_heap) == 1:
        return 0

    min_num = min_heap[1]

    if len(min_heap) == 2:
        return min_heap.pop()

    min_heap[1] = min_heap.pop()

    par_idx = 1
    left_idx = par_idx * 2
    right_idx = par_idx * 2 + 1

    while left_idx < len(min_heap):
        smaller_idx = left_idx

        if right_idx < len(min_heap) and min_heap[left_idx] > min_heap[right_idx]:
            smaller_idx = right_idx

        if min_heap[par_idx] > min_heap[smaller_idx]:
            swap(par_idx, smaller_idx)
            par_idx = smaller_idx
            left_idx = par_idx * 2
            right_idx = par_idx * 2 + 1
        else:
            break

    return min_num

for _ in range(N):
    X = int(sys.stdin.readline().strip())

    if X == 0:
        print(pop())
    else:
        push(X)
