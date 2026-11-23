class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(str)}#{str}' for str in strs)

    def decode(self, s: str) -> List[str]:
        out=[]

        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            start=j+1
            end = start + length
            out.append(s[start:end])
            i=end
        return out