def bottomUpHeap(heap):
    #takes list as  input
    newHeap = []
    for i in range(len(heap)-1,-1,-1):
        print(heap[i])
    return newHeap
bottomUpHeap([0,1,2,3,4,5])

