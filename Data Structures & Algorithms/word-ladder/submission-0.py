class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # cat<->bat<->bag<->sag<->dag  dot
        wordset = set(wordList)
        dist = {i:math.inf for i in wordset}
        vis = {i:0 for i in wordset}
        dist[beginWord] = 0
        q = deque()
        q.append((beginWord,1))
        vis[beginWord] = 1
        while q:
            ele,d = q.popleft()
            if ele==endWord:
                return d
            for j in range(len(ele)):
                for l in range(26):
                    neighbour = ele[:j] + chr(97 + l) + ele[j+1:]
                    if neighbour in wordset and vis[neighbour]==0:
                        dist[neighbour] = min(dist[neighbour],d+1)
                        q.append((neighbour,dist[neighbour]))
                        vis[neighbour] = 1
        return 0


        


        