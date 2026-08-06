class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        if n==100 or n==10:
            return n
        if n<10:
            if n<=t:
                return t
            for i in range(n,10):
                if i%t==0:
                    return i
            return 10
        first_digit=int(str(n)[0])
        second_digit=int(str(n)[1])
        for i in range(second_digit,10):
            if (i*first_digit)%t==0:
                return int(str(first_digit)+str(i))
        first_digit+=1
        second_digit=0
        return int(str(first_digit)+str(second_digit))


        