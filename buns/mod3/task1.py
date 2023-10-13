a, b, c = map(int, input().split())
middle_elem = a + b + c - max(a, b, c) - min(a, b, c)
print(middle_elem)