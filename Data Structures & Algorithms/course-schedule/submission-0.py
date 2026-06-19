class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqMap = defaultdict(list)
        for a, b in prerequisites:
            preqMap[a].append(b)
        
        taken = set()
        for course in range(numCourses):
            if course not in preqMap:
                taken.add(course)
        
        seen = set()

        def dfs(course):
            if course in seen:
                return False
            if course in taken:
                return True
            
            seen.add(course)
            for pre in preqMap[course]:
                if not dfs(pre):
                    return False
            seen.remove(course)
            taken.add(course)
            return True

        for course in preqMap:
            if not dfs(course):
                return False
        return True