def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        area = width * current_height
        if area > max_area:
            max_area = area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))