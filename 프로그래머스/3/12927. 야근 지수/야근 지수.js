class MaxHeap {
    constructor() {
        this.heap = [null]
    }
    
    get() {
        return this.heap;
    }
    
    getMax() {
        return this.heap[1]
    }
    
    swap(a, b) {
        [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]]
    }
    
    push(item) {
        this.heap.push(item)
        
        let cur_idx = this.heap.length - 1
        let par_idx = cur_idx / 2 >> 0
        
        while (cur_idx > 1 && this.heap[par_idx] < this.heap[cur_idx]) {
            this.swap(cur_idx, par_idx)
            cur_idx = par_idx
            par_idx = cur_idx / 2 >> 0
        }
    }
    
    pop() {
       const max = this.heap[1];
        
	    if (this.heap.length <= 2) {
	        this.heap = [ null ];
	        return max;
	    }
        
        this.heap[1] = this.heap.pop();
        
        let cur_idx = 1;
        let left_idx = cur_idx * 2
        let right_idx = cur_idx * 2 + 1
        
        while (this.heap[left_idx]) {
            let bigger_idx = left_idx
            
            if (this.heap[bigger_idx] && this.heap[bigger_idx] < this.heap[right_idx]) {
                bigger_idx = right_idx
            }
            
            if (this.heap[bigger_idx] && this.heap[bigger_idx] > this.heap[cur_idx]) {
                this.swap(cur_idx, bigger_idx)
                cur_idx = bigger_idx
                left_idx = cur_idx * 2
                right_idx = cur_idx * 2 + 1
            }
            else break 
        }
        
        return max
    }
    
}

function solution(n, works) {
    var answer = 0;
    let maxheap = new MaxHeap();
    for(let work of works) {
        maxheap.push(work)
    }
    
    while (n > 0) {
        let max_work = maxheap.pop()
        if (max_work == 0) break
        max_work -= 1
        n -= 1
        maxheap.push(max_work)
    }
    return maxheap.get().reduce((a, c) => a + c**2);
}