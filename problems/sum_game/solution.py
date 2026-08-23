class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        num_arr=list(int(nums) if nums!='?' else '?' for nums in num)
        l=0
        r=len(num_arr)-1
        left_sum=0
        right_sum=0
        num_q=0
        left_q=0
        right_q=0
        while l<r:
            if num_arr[l]!='?':
                left_sum+=num_arr[l]
            else:
                num_q+=1
                left_q+=1
            if num_arr[r]!='?':
                right_sum+=num_arr[r]
            else:
                num_q+=1
                right_q+=1
            l+=1
            r-=1
        if num_q%2!=0:
            return True
        if num_q%2==0:
            if left_sum==right_sum:
                if left_q==right_q:
                    return False
                else:
                    return True
            else:
                if left_sum<right_sum:
                    if right_q>left_q:
                        return True
                    else:
                        if right_sum-left_sum==9*(left_q-right_q)//2:
                            return False
                        else:
                            return True
                else:
                    if right_q<left_q:
                        return True
                    else:
                        if left_sum-right_sum==9*(right_q-left_q)//2:
                                return False
                        else:
                            return True
        return True
                    
        
        
        
            

        