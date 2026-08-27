class Solution(object):
    def lowerBound(self,arr,char):
        low=0
        high=len(arr)-1
        ans=len(arr)
        while low<=high:
            mid=(low+high)//2
            if ord(arr[mid])<=ord(char):
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        char_map_s=defaultdict(int)
        s_set=set()
        for ch in s:
            char_map_s[ch]+=1
            s_set.add(ch)
        s_arr=list(s_set)
        s_arr.sort()
        ans=""
        i=0
        while i<len(s):
            if target[i] in char_map_s:
                    ans+=target[i]
                    char_map_s[target[i]]-=1
                    if char_map_s[target[i]]==0:
                        del char_map_s[target[i]]
                    i+=1
            else:
                just_greater=self.lowerBound(s_arr,target[i])
                while just_greater < len(s_arr) and char_map_s[s_arr[just_greater]] == 0:
                    just_greater += 1
                if just_greater<len(s_arr):
                    char=s_arr[just_greater]
                    ans+=char
                    char_map_s[char]-=1
                    if char_map_s[char]==0:
                        del char_map_s[char]
                    for char in s_arr:
                        while char_map_s[char]>0:
                            ans+=char
                            char_map_s[char]-=1
                    return ans
                else:
                    break 
        lst=list(ans)
        while lst:
            ch=lst.pop()
            char_map_s[ch]+=1
            just_greater=self.lowerBound(s_arr,ch)
            while just_greater < len(s_arr) and char_map_s[s_arr[just_greater]] == 0:
                just_greater += 1
            if just_greater<len(s_arr):
                char=s_arr[just_greater]
                lst.append(char)
                char_map_s[char]-=1
                if char_map_s[char]==0:
                    del char_map_s[char]
                for char in s_arr:
                    while char_map_s[char]>0:
                        lst.append(char)
                        char_map_s[char]-=1
                return ''.join(lst)
        return ""




            

        