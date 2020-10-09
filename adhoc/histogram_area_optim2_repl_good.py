histogram = [6, 2, 5, 4, 5, 1, 6]
histogram = [1, 1, 2, 1, 1]
l = 1
r = 3

print("start")

stack = list() 
max_area = 0
index = l
while index <= r:
    print("s0", stack)
    if (not stack) or (histogram[stack[-1]] <= histogram[index]):
        stack.append(index)
        index += 1
        print("s1", stack)
    else:
        top_of_stack = stack.pop()
        area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index -l))
        max_area = max(max_area, area)
        print("s2", stack, max_area)

while stack:
    print("s3", stack)
    top_of_stack = stack.pop()
    print("t", top_of_stack, index)
    area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index -l))
    max_area = max(max_area, area)
    print("s4", stack, max_area)

print("finish", max_area)

