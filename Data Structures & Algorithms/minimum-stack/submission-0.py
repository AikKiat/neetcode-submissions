

class MinStack:

    """
    push --> push element into stack 
    pop --> remove element on top of stack
    top --> get top element
    min --> retrieve minimum element (keep track of running record of mins. We can priority queue, but we would need to perform min heapify across all leaf nodes which leads to nlogn)

   -1 -1
    0  0
    2  1
    1  1

    Instead of brute forcing O(n) to find the minimum, we can maintain another stack that keeps a running record of the current min at every point in time. When we first bring in a number we see --> is this nunber smaller than the current minimum? If so then we add this number to the top of this extra stack. Otherwise, we will continue to add the current top element of this extra stack, again --> because it is the current running minimum. Both actual and minimum stacks should be of same lengths always. Therefore when we pop an element from the actual stack, we also pop the top off the minimum stack because it represents the running minimum at that time, when there were this amount of items in the stack. Removing from the minimum stack is like going back in time, to find the minimum at that point when there were fewer items in the stack.
    """
    
    
    stack : list[int] = []
    min_stack : list[int] = []
    seen = set()

    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        #push to min stack as well as actual stack
        #but for min_stack, we push the min(current minimum vs this new val)
        
        self.stack.append(val)
        
        if len(self.min_stack) > 0:
            self.min_stack.append(min(self.min_stack[-1], val))
        else:
            self.min_stack.append(val) #this is the first minimum to be recorded, when there is only 1 item in the stack


    def pop(self) -> None:
        self.stack.pop(-1)
        self.min_stack.pop(-1)


    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

        return None
        

    def getMin(self) -> int:
        if len(self.min_stack) > 0:
            return self.min_stack[-1]

        return None
        
