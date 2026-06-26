class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        # Step 1: Convert to +1 and -1 values
        # target becomes 1, any other number becomes -1
        transformed = [1 if num == target else -1 for num in nums]
        
        # Step 2: Compute prefix sums
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + transformed[i]
            
        # Step 3: Coordinate compression for Fenwick Tree indices
        # Fenwick tree requires 1-based, positive indices
        unique_sums = sorted(list(set(prefix_sums)))
        ranks = {val: i + 1 for i, val in enumerate(unique_sums)}
        
        # Step 4: Implement a Fenwick Tree (Binary Indexed Tree)
        tree_size = len(unique_sums)
        bit = [0] * (tree_size + 1)
        
        def update(idx: int, delta: int):
            while idx <= tree_size:
                bit[idx] += delta
                idx += idx & (-idx)
                
        def query(idx: int) -> int:
            total = 0
            while idx > 0:
                total += bit[idx]
                idx -= idx & (-idx)
            return total
            
        # Step 5: Count valid subarrays
        total_subarrays = 0
        
        # Insert the initial prefix sum of 0 into the tree
        update(ranks[0], 1)
        
        for p_sum in prefix_sums[1:]:
            # Find how many previous prefix sums are strictly smaller than p_sum
            current_rank = ranks[p_sum]
            total_subarrays += query(current_rank - 1)
            
            # Add the current prefix sum to the Fenwick Tree
            update(current_rank, 1)
            
        return total_subarrays
