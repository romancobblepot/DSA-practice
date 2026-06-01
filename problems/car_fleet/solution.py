
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        arr=[]
        for i in range(len(position)):
            arr.append((position[i],speed[i]))
        arr.sort(reverse=True)
        time=[]
        last_time=0
        fleets=0
        for position,speed in arr:
            time_taken=float(target-position)/speed
            if time_taken>last_time:
                fleets+=1
                last_time=time_taken
        return fleets





        