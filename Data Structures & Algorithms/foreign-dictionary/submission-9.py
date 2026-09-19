class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        ind = [0]*26
        for i in words:
            for j in range(len(i)):
                adj[i[j]] = []
        i = 0
        while i+1<len(words):
            w1 = words[i]
            w2 = words[i+1]
            j = 0
            while j<len(w1) and j<len(w2):
                if w1[j]!=w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].append(w2[j])
                        ind[ord(w2[j])-ord('a')]+=1
                    break
                j+=1
            if len(w1)>len(w2) and j==len(w2):
                return ""  
            i = i+1
        q = deque()
        for i in adj:
            if ind[ord(i)-ord('a')]==0:
                q.append(i)
        res = ""
        while q:
            ele = q.popleft()
            res+=ele
            if ele in adj: 
                for i in adj[ele]:
                    ind[ord(i)-ord('a')]-=1
                    if ind[ord(i)-ord('a')]==0:
                        q.append(i)
        if len(res)!=len(adj):
            return ""
        return res

                