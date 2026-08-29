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

    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        freq=defaultdict(int)
        for ch in s:
            freq[ch]+=1
        odd=0
        middle=""
        for ch in freq:
            if freq[ch]%2!=0:
                odd+=1
                middle=ch
        if odd>1:
            return ""
        char_map_s=defaultdict(int)
        for ch in freq:
            char_map_s[ch]=freq[ch]//2
        s_arr=list(freq.keys())
        s_arr.sort()
        i=0
        ans=""
        target_half=target[:len(s)//2]
        while i<len(s)//2:
            if char_map_s.get(target_half[i],0)>0:
                    ans+=target_half[i]
                    char_map_s[target_half[i]]-=1
                    if char_map_s[target_half[i]]==0:
                        del char_map_s[target_half[i]]
                    i+=1
            else:
                just_greater=self.lowerBound(s_arr,target_half[i])
                while just_greater < len(s_arr) and char_map_s.get(s_arr[just_greater],0) == 0:
                    just_greater += 1
                if just_greater<len(s_arr):
                    char=s_arr[just_greater]
                    ans+=char
                    char_map_s[char]-=1
                    if char_map_s.get(char,0)==0:
                        del char_map_s[char]
                    for char in s_arr:
                        while char_map_s.get(char,0)>0:
                            ans+=char
                            char_map_s[char]-=1
                    return ans + middle + ans[::-1]
                else:
                    break 
        if len(ans)==len(target_half):
            cand=ans+middle+ans[::-1]
            if cand>target:
                return cand
        lst=list(ans)
        while lst:
            ch=lst.pop()
            char_map_s[ch]+=1
            just_greater=self.lowerBound(s_arr,ch)
            while just_greater < len(s_arr) and char_map_s.get(s_arr[just_greater],0) == 0:
                just_greater += 1
            if just_greater<len(s_arr):
                char=s_arr[just_greater]
                lst.append(char)
                char_map_s[char]-=1
                if char_map_s.get(char,0)==0:
                    del char_map_s[char]
                for char in s_arr:
                    while char_map_s.get(char,0)>0:
                        lst.append(char)
                        char_map_s[char]-=1
                left= ''.join(lst)
                return left + middle + left[::-1]
        return ""

        
        