class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        n=len(tokens)
        characters="*/-+"
        stack=[]
        for i in range(n):
            if tokens[i] not in characters:
                stack.append(int(tokens[i]))
            else:
                op2=stack.pop()
                op1=stack.pop()
                if tokens[i]=="*":
                    ans=op1*op2
                elif tokens[i]=="/":
                    if op1/op2<0 and op1%op2!=0:
                        ans=op1//op2 +1
                    else:
                        ans=(op1)//op2
                elif tokens[i]=="+":
                    ans=op1+op2
                else:
                    ans=op1-op2
                stack.append(ans)
        return stack[-1]


        