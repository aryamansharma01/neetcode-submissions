class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for i in words:
            for j in i:
                if j not in adj:
                    adj[j] = []
        n = len(words)
        ind = {i:0 for i in adj}
        for i in range(n - 1):
            w1 = words[i]
            w2 = words[i + 1]
            j = 0
            while j < len(w1) and j < len(w2):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].append(w2[j])
                        ind[w2[j]] += 1
                    break
                j += 1
            if j == len(w2) and len(w1) > len(w2):
                return ""
        q = deque()
        for i in ind:
            if ind[i]==0:
                q.append(i)
        res = ""
        while q:
            ele = q.popleft()
            res+=ele
            for child in adj[ele]:
                ind[child]-=1
                if ind[child]==0:
                    q.append(child)
        if len(res)!=len(adj):
            return ""
        return res
            
        
        

