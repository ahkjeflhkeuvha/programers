import sys

N = int(input())

max_heap = [None]

def swap(a, b):
    global max_heap
    max_heap[a], max_heap[b] = max_heap[b], max_heap[a]

def push(n):
    global max_heap

    max_heap.append(n)

    cur_idx = len(max_heap) - 1
    par_idx = cur_idx // 2

    while cur_idx > 1 and max_heap[cur_idx] > max_heap[par_idx]:
        swap(cur_idx, par_idx)
        cur_idx = par_idx
        par_idx = cur_idx // 2


def pop():
    global max_heap

    if len(max_heap) == 1:
        return 0
    
    max_num = max_heap[1]

    if len(max_heap) == 2:
        return max_heap.pop()

    max_heap[1] = max_heap.pop()

    cur_idx = 1
    left_idx = cur_idx * 2
    right_idx = cur_idx * 2 + 1

    while left_idx < len(max_heap):
        bigger_idx = left_idx
        if right_idx < len(max_heap) and max_heap[left_idx] < max_heap[right_idx]:
            bigger_idx = right_idx
        
        if max_heap[bigger_idx] > max_heap[cur_idx]:
            swap(cur_idx, bigger_idx)
            cur_idx = bigger_idx
            left_idx = cur_idx * 2
            right_idx = cur_idx * 2 + 1
        else:
            break

    return max_num

for _ in range(N):
    num = int(sys.stdin.readline().strip())

    if num == 0:
        print(pop())
    else:
        push(num)