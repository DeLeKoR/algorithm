class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {}

        for i in range(numCourses):
            graph[i] = []

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = set()
        path = set()

        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True

            path.add(course)

            for next_course in graph[course]:
                if dfs(next_course) == False:
                    return False

            path.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return False

        return True