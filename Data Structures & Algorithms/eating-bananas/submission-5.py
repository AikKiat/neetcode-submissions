class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        piles:
        1 4 3 2   h = 9
        can eat k bananas in 1 hour.
        if a pile has less than k bananas, can finish that entire pile but cannot eat from another pile in the same hour. Basically, for every hourly step we can only subtract from 1 pile. (choose a pile, subtract from there. Eat finish cannot use extra time/k-piles left rate to eat from another pile)

        Thoughts:
        if we sort the array --> smallest to largest.Basically we can slowly find the value of k that allows us to finish the job within h hours. Upper bound for k is the largest pile ever at the end,but that is not optimal.
        If k is greater than all pile numbers, we still need to spend len(nums) time to eat all piles hour by hour. So, the additional time taken (during which we spend > 1 hour on a any pile) is h - len(piles)

        If we do binary search on the sorted pile, we land on a number of k that works --> check the adjacent value down by 1. If that also works, then perhaps there is lower values we havent seen yet. 

        How to guage if a k value "works" --> for now --> once obtaining a key take all values divided by k to get rounded remainer --> add to len(nums) --> if < h ok, and perform the above. If == h immediately return, because this shows that we have reached an optimal k value already. if > h then update our bounds.


        Edge cases:
        if length of piles is just 1, return piles[0] / h, rounded up


        FIX:
        We have to binary search on the value range of 1, max(piles) NOT the piles themselves...
        """


        if len(piles) == 1:
            if piles[0] % h > 0:
                return int(piles[0]/h) + 1
            return int(piles[0]/h)


        low = 1
        high = max(piles)

        while low < high:
            middle = (low + high) // 2

            total = 0
            for pile in piles:
                total += int(pile/middle)
                if pile % middle > 0:
                    total += 1

            if total > h:
                low = middle + 1

            else:
                high = middle

        return high






        