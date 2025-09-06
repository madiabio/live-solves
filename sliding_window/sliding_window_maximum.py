class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonoically decreasing deque!
        output = []
        l = r = 0
        q = deque()

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # Remove all idxs in queue that are smaller than r from the end fo the queue.
                q.pop()
            
            q.append(r) # Add current element to the queue such thta its smaller than everything to the left of it.

            if l > q[0]: # If out of bounds, pop!
                q.popleft()
            if r+1 >= k: # If moving out of the window, add the window's max to the output & slide the window.
                output.append(nums[q[0]])
                l+=1
            r += 1 # r always slides.

        return output
