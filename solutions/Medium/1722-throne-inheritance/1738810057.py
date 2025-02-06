class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = kingName
        self.adj = defaultdict(list)
        self.dead = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        self.adj[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:

        out = []
        def dfs(node):

            found = False
            out.append(node)
            for u in self.adj[node]:
                dfs(u)

        dfs(self.root)
        return [x for x in out if x not in self.dead]
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()