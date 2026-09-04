"""
time based key value store
store multiple values for the same key, at diff time stamps
retrieve the key's value at certain timestamp
"""


class TimeMap:

    def __init__(self):
        self.key_timestamps_store = {} #stores key, to timestamps array:
        #timestaps array: [2,3,5,7,9] --> diff timestamps associated to this key, when it was updated.
        #timestamps_to_value = {} --> timestamps to values hashmap, which maps at that point in time, when we update at a said timestamp what value was set. Unique to key

        self.key_value_updates_store = {} #key --> timestamps_to_value hashmap
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.key_timestamps_store.keys():
            self.key_timestamps_store[key] = [timestamp]

        else:
            current_timestamps_array = self.key_timestamps_store[key]
            current_timestamps_array.append(timestamp) #all timestamps of set are strictly increasing based on qn, so we do not need to sort.
            self.key_timestamps_store[key] = current_timestamps_array

        if key not in self.key_value_updates_store.keys():
            self.key_value_updates_store[key] = {timestamp : value}

        else:
            timestamps_to_value = self.key_value_updates_store[key]
            timestamps_to_value[timestamp] = value
            self.key_value_updates_store[key] = timestamps_to_value
        

    def get(self, key: str, timestamp: int) -> str:
        #Here, perform binary search on the timestamps array that according to qn is in non-decreasing order.
        #So, binary search on the latest timestamp_prev, relative to this timestamp we are searching at.

        if key not in self.key_timestamps_store.keys():
            return ""

        timestamps = self.key_timestamps_store[key]

        low = 0
        high = len(timestamps)-1
        latest_timestamp = None
        
        while low <= high:
            middle = (low+high) // 2
            if timestamps[middle] <= timestamp:
                latest_timestamp = timestamps[middle]
                low = middle + 1
            else:
                high = middle - 1

        if latest_timestamp is None:
            return ""

        timestamps_to_value = self.key_value_updates_store[key]
        return timestamps_to_value[latest_timestamp]
