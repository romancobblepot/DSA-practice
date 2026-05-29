class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        n=len(people)
        boat=0
        max_limit=limit
        current_limit=max_limit
        people.sort()
        l=0
        r=n-1
        while l<=r:
            if l!=r and people[l]+people[r]<=current_limit:
                current_limit=max_limit
                boat+=1
                l+=1
                r-=1
            else:
                current_limit=max_limit
                boat+=1
                r-=1
        return boat
                





            



        