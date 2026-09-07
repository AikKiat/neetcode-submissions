
class LinkedListElement:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.value = value
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.cache_store = {}
        self.end_point = LinkedListElement(None, None) #represents the end of the cache, .next is oldest value
        self.head_point = LinkedListElement(None, None) #represents start of cache, .prev is most recent value
        self.capacity = capacity

    def remove_specific_element(self, linked_list_element):
        before = linked_list_element.prev
        after = linked_list_element.next
        before.next = after
        after.prev = before


    def insert_at_head(self,new_element):
        current_head_point = self.head_point.prev
        
        if current_head_point:
            new_element.prev = current_head_point
            current_head_point.next = new_element
        else:
            new_element.prev = self.end_point
            self.end_point.next = new_element
        
        new_element.next = self.head_point
        self.head_point.prev = new_element
        

    def get(self, key: int) -> int:
        if key in self.cache_store:
            linked_list = self.cache_store[key]
            value = linked_list.value
            #Update the placement
            #First remove, and then insert at head
            self.remove_specific_element(linked_list)
            self.insert_at_head(linked_list)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_store:
            linked_list_element = self.cache_store[key]
            linked_list_element.value = value
            self.remove_specific_element(linked_list_element)
            self.insert_at_head(linked_list_element)
            return

        if self.capacity > 0:
            new_element = LinkedListElement(key, value)
            self.cache_store[key] = new_element
            self.insert_at_head(new_element)
            self.capacity -= 1

        else:
            oldest_element = self.end_point.next
            self.remove_specific_element(oldest_element)
            del self.cache_store[oldest_element.key]
            new_element = LinkedListElement(key, value)
            self.cache_store[key] = new_element
            self.insert_at_head(new_element)
            

            


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
Designing an LRU CACHE
Key-Value pairs
1 : x
2 : y
3 : z
Then getting an item --> 3
order:
3 : z
1 : x
2 : y
oldest -> 3 -> 2 -> 1 -> newest
newest.prev = the newest cache key
oldes.next = oldest cache key.
So we can have a linked list to keep track (doubly linked) of all of the cache keys, and to retrieve the value for a particular cache key in O(1) we can use a hashmap.

Thus: 
1. Linked list class to keep track of recency of cache keys
2. Main LRU class that has key-value pair mappings, as well as get, put, remove, insert methods
3. Each linked list element is therefore in essence a class with attributes of left, next and val
"""