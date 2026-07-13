class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        def make_sequential(digit,length):
            num=digit
            prev_digit=digit
            for i in range(length-1):
                new_digit=prev_digit+1
                num=num*10 + new_digit
                prev_digit=new_digit
            return num
        len_low=len(str(low))
        len_high=len(str(high))
        arr=[]
        for l in range(len_low,len_high+1):
            for digits in range(1,11-l):
                number=make_sequential(digits,l)
                if number<low or number>high:
                    continue
                else:
                    arr.append(number)
        return arr





        