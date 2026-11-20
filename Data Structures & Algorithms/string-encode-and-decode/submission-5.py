class Solution:

    def encode(self, strs: List[str]) -> str:
        out="".join(f'{len(s)}#{s}' for s in strs)
        return out

    def decode(self, s: str) -> List[str]:
        out=[]
        i = 0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            start = j+1
            end = start+length
            t = s[start:end]
            out.append(t)
            i=end

        return out
