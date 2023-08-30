class Solution:
    def reverseOnlyLetters(self,S):
        if not S:
            return S
        str_=""
        start=0
        end=len(S)-1
        while(start<(len(S))):
            if end>=0 and S[start].isalpha() and S[end].isalpha():
                str_+=S[end]
                end-=1
                start +=1
            elif S[start].isalpha():
                end-=1
            elif not S[start].isalpha():
              str_+=S[start]
              start+=1
            else:
              end -=1
              start +=1
        return str_
obj=Solution()