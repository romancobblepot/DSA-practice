class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        null_blocks={}
        for row,seat in reservedSeats:
            if row not in null_blocks:
                null_blocks[row]=[False,False,False]
                if seat==1 or seat==10:
                    continue
                if 2<=seat<=3:
                    null_blocks[row][0]=True
                elif 4<=seat<=5:
                    null_blocks[row][0]=True
                    null_blocks[row][1]=True
                elif 6<=seat<=7:
                    null_blocks[row][1]=True
                    null_blocks[row][2]=True
                else:
                    null_blocks[row][2]=True
            else:
                if seat==1 or seat==10:
                    continue
                if 2<=seat<=3:
                    null_blocks[row][0]=True
                elif 4<=seat<=5:
                    null_blocks[row][0]=True
                    null_blocks[row][1]=True
                elif 6<=seat<=7:
                    null_blocks[row][1]=True
                    null_blocks[row][2]=True
                else:
                    null_blocks[row][2]=True
        ans=0
        for row,blocks in null_blocks.items():
            if blocks[0] and blocks[1] and blocks[2]:
                continue
            if not blocks[0] and not blocks[1] and not blocks[2]:
                ans+=2
            else:
                ans+=1
        return 2*(n-len(null_blocks))+ans
        




        