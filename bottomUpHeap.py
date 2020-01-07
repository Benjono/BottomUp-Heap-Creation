def bottomUpHeap(heap):
    #takes list as  input
    newHeap = []
    currentItem = len(heap)-1
    while currentItem>=0:
        if(currentItem<(len(heap)-1)/2):
            bubbled=False;
            currentPlace = currentItem
            while(not bubbled and currentPlace<len(heap)/2):
                print(heap)
                if(currentPlace*2+1>len(heap)-1):
                    bubbled=True;
                    #no children
                else:
                    if(currentPlace*2+2>len(heap)-1):
                        #if one child
                        if(heap[currentPlace*2+1]>heap[currentPlace]):
                            temp = heap[currentPlace]
                            heap[currentPlace]=heap[currentPlace*2+1]
                            heap[currentPlace*2+1]=temp
                            #perform swap
                            currentPlace=currentPlace*2+1
                            #move pointer
                        else:
                            bubbled=True;
                    else:
                        #if two children
                        if heap[currentPlace*2+1]>heap[currentPlace] or heap[currentPlace*2+2]>heap[currentPlace]:
                            #if either children are larger
                            if heap[currentPlace*2+1]>heap[currentPlace*2+2]:
                                #choose which one
                                temp = heap[currentPlace]
                                heap[currentPlace]=heap[currentPlace*2+1]
                                heap[currentPlace*2+1]=temp
                                #perform swap
                                currentPlace=currentPlace*2+1
                                #move pointer
                            else:
                                temp = heap[currentPlace]
                                heap[currentPlace]=heap[currentPlace*2+2]
                                heap[currentPlace*2+2]=temp
                                #perform swap
                                currentPlace=currentPlace*2+2
                                #move pointer
                        else:
                            bubbled=True;
                            #if the children are less than it, then it's in the right place
        currentItem-=1
    return heap
print(bottomUpHeap([0,1,2,3,4,5,6,7,8,9]))

