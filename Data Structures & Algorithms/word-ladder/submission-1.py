class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        q = deque()
        q.append((beginWord,1))
        vis = set()
        while q:
            w,d = q.popleft()
            if w==endWord:
                return d
            for i in range(len(w)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if j==w[i]:
                        continue
                    temp = w[:i] + j + w[i+1:]
                    if temp not in vis and temp in words:
                        vis.add(temp)
                        q.append((temp,d+1))
        return 0
        


        


        