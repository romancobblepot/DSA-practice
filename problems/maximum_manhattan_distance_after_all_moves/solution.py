class Solution(object):
    def maxDistance(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        n=len(moves)
        mapp={"L":(-1,0),"R":(1,0),"U":(0,1),"D":(0,-1)}
        x=0
        y=0
        count=0
        for i in range(len(moves)):
            if moves[i]!="_":
                x+=mapp[moves[i]][0]
                y+=mapp[moves[i]][1]
            else:
                count+=1
        return count+abs(x)+abs(y)
                