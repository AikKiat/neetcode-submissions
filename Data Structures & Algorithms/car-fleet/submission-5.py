class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        position
        speed

        destination, at target miles
        [1,4]
        [3,2]
        0th car at position 1, speed 3
        1th car at position 4, speed 2 
        target = 10
        0 1 2 3 4 5 6 7 8 9 10
          i     j   j   j   j
                i     i     i

        To reach the target, 0th car got into as many future positions as 1th car.

        We can see that car d, car a eavh take a total of 4 positions on the range. car b taks 6, car c takes 10 --> hence, 3 different car fleets.
        
        Because taking the same number of positions on a range, means that both carsdid eventually catch up to one another and can thus be considered under 1 fleet.
        
        All values of position are also unique because single lane highway.

        **If a car catches up to a car ahead of it, then it will drive at that speed and this becomes like 1 car. --> 1 fleet


        [4 1 0 7]
        [2 2 1 1]

        c b     a           d
        0 1 2 3 4 5 6 7 8 9 10
        
        a-> 3
        b-> 5
        c-> 10
        d-> 3


        Thoughts:
        All these present the number of time taken to reach the target
        How about catching up to each other?
        given a car at some position, how many cars behind it can successfully stack up behind it? Just before and as it reaches its destination.

        When we encounter a car at a further position up the lane, how many others we have seen beforehad, can stack up to it?

        Sort the positions first, and this helps us to make sure we dont lose out any cars..





        [10,8,0,5,3]
        [2,4,1,1,3]

        [0 3 5 8 10]

        hashmap of position --> steps

        a-> 10,1
        b-> 8,2
        c-> 0,12
        d->5,7
        e->3,3

        |0,12 5,7 10,1

        Plan:
        > calculate steps for every car first
        > create hashmap of position to step
        > now for th stack. --> look through the items in the stack, for a new given car at position x, taking steps y look at the top car and see: is this car at a smaller position and is this car taking less steps than y? if it is then pop this car out. Else, skip and look at the next top element. finally, when we resolved all possible cars that can stack up to this little car, add it to the stack as top element.
        > return length of stack.


        Edge case: 
        if target is 0, then all cars have made it. Just 1 fleet?

        UPDATE --> ITS NOT STEPS, BUT ACTUAL TIME TAKEN!!! SO, dont just round everything to integer. We have to calculate to by actual time taken to reach destination hence at cases where cars are at the same speed but different positions, and the speeds determine that they will reach the destination within 1 hour / 1 step --> the actual time taken in terms of fractions of the hour are very different, owing to their different positions.
        """

        if len(position) == 1:
            return 1

        if target == 0:
            return 1

        positions_steps_map = defaultdict(int)

        for car in range(len(position)): 
            steps = (target - position[car]) / speed[car] #calculate by actual time taken! Not just steps of the hour
            positions_steps_map[position[car]] = steps
            

        position.sort()

        fleet = [position[len(position)-1]] #the last car, closest to target
        for car in range(len(position)-2, -1, -1):
            if positions_steps_map[position[car]] > positions_steps_map[fleet[-1]]:
                #then this car can never catch up. It forms another blockade
                fleet.append(position[car])

        return len(fleet)


        """
        8:1
        3:3
        7:1
        4:2
        6:1
        5:2
        """



















