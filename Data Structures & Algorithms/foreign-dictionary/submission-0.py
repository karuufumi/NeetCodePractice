class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        vertices = set()
        for w in words:
            for c in w:
                vertices.add(c)

        adjList = dict()
        for v in vertices:
            adjList[v] = list()
        
        indegree = dict()
        for v in vertices:
            indegree[v] = 0

        for i in range(len(words) - 1):
            wordA = words[i]
            wordB = words[i + 1]
            j = 0
            a = wordA[j]
            b = wordB[j]
            while a == b:
                j += 1
                if j < len(wordA) and j == len(wordB):
                    return ""
                if j == len(wordA):
                    break
                a = wordA[j]
                b = wordB[j]
            if a == b:
                continue
            adjList[a].append(b)
            indegree[b] += 1

        queue = list()
        for c in vertices:
            if indegree[c] == 0:
                queue.append(c)
        
        result = ""
        while queue:
            c = queue.pop()
            result += c
            for n in adjList[c]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)

        return result if len(result) == len(vertices) else ""
