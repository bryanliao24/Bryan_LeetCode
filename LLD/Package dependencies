You have a package repository in which there are dependencies between packages for building like package A has to be built before package B. If you are given dependencies between the packages and package name x, we have find the build order for x.
Ex: A → {B,C}
B → {E}
C → {D,E,F}
D → {}
F → {}
G → {C}

For package A, build order is E B F D C A (may not unique)

# --------- Minimal Exceptions ----------
class PackageNotFoundError(Exception):
    pass

class DependencyCycleError(ValueError):
    pass


# --------- Repository (graph) ----------
class PackageRepository:
    def __init__(self):
        # name -> ordered unique list of deps
        self.graph = {}

    def _ensure(self, name):
        if name not in self.graph:
            self.graph[name] = []

    def add_package(self, name, deps):
        self._ensure(name)
        out = []
        seen = set()
        for d in deps:
            self._ensure(d)
            if d not in seen:
                seen.add(d)
                out.append(d)
        self.graph[name] = out

    def has_package(self, name):
        return name in self.graph

    def deps_of(self, name):
        if name not in self.graph:
            raise PackageNotFoundError("Package not found: " + str(name))
        # 返回副本，避免外部修改内部列表
        return list(self.graph[name])


# --------- Planner (DFS post-order) ----------
class BuildPlanner:
    def __init__(self, repo):
        self.repo = repo

    def build_order(self, root):
        if not self.repo.has_package(root):
            raise PackageNotFoundError("Package not found: " + str(root))

        visiting = set()  # 当前递归路径上的点（栈）
        visited  = set()  # 已完成
        order = []        # 退出时追加：依赖在前，被依赖在后

        def dfs(u):
            if u in visiting:
                # 这里为简洁仅报节点；若要完整环路径，可在面试口述如何用父指针还原
                raise DependencyCycleError("Cycle involving: " + str(u))
            if u in visited:
                return
            visiting.add(u)
            for v in self.repo.deps_of(u):
                dfs(v)
            visiting.remove(u)
            visited.add(u)
            order.append(u)

        dfs(root)
        return order  # root 必在最后


# --------- Quick demo ----------
def demo():
    repo = PackageRepository()
    repo.add_package('A', ['B', 'C'])
    repo.add_package('B', ['E'])
    repo.add_package('C', ['D', 'E', 'F'])
    repo.add_package('D', [])
    repo.add_package('E', [])
    repo.add_package('F', [])
    repo.add_package('G', ['C'])

    planner = BuildPlanner(repo)

    print("Build A:", planner.build_order('A'))  # e.g. ['E','B','D','F','C','A']
    print("Build G:", planner.build_order('G'))  # e.g. ['E','D','F','C','G']

if __name__ == "__main__":
    demo()
