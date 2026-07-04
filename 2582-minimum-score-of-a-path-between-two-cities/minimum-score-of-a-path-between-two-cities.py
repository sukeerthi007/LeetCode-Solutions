class Solution:

    from collections import deque, defaultdict
    
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        # Build adjacency list where each node points to (neighbor, road_distance)
        graph = defaultdict(list)
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))
            
        # Queue for BFS traversal starting from city 1
        queue = deque([1])
        
        # Keep track of visited nodes to avoid infinite loops
        visited = {1}
        
        # Initialize minimum score with a value larger than any maximum edge weight
        min_score = float('inf')
        
        while queue:
            node = queue.popleft()
            
            # Explore all roads connected to the current city
            for neighbor, distance in graph[node]:
                # Track the smallest road weight found anywhere in this component
                min_score = min(min_score, distance)
                
                # If neighbor hasn't been visited, add it to the queue
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score
