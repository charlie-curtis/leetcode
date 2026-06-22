class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:

        n = len(edges)+1
        d = defaultdict(list)
        for u,v,w in edges:
            d[u].append((v,w))
            d[v].append((u,w))


        def getBest(options, allowed):
            score = 0
            chosen = 0
            for x,y in options:
                if y > x and chosen < allowed:
                    score+=y
                    chosen+=1
                else:
                    score+=x
            #print("returning a score of ", score, "for options", options)
            return score


        def dfs(node, parent):

            options = []
            parent_weight = 0
            for u,w in d[node]:
                if u == parent:
                    parent_weight = w
                    continue
                options.append(dfs(u, node))

            options.sort(key = lambda x: x[0]-x[1])
            score = getBest(options, k-1)
            score_if_keep_parent_edge = score + parent_weight
            score_if_del_parent_edge = getBest(options, k)

            return [score_if_del_parent_edge, score_if_keep_parent_edge]

        return max(dfs(0, -1))
