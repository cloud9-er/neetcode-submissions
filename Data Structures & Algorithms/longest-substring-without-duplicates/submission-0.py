class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current=0
        left=0
        st=set()
        for right in range(len(s)):
            while s[right] in  st:
                st.remove(s[left])
                left+=1
            st.add(s[right])
            streak=(right -left)+1
            current=max(streak,current)
        return current
