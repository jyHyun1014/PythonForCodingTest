# 7219 타격왕 정우성
# 이진탐색

x, y = map(int, input().split())
m = 1000000000
rate = int((y / x) * 100) / 100
new = int(((y + m) / (x + m)) * 100) / 100

if x == y or rate >= new:
  print(-1)
else:
  result = m
  start = 1
  end = m
  while start <= end:
    mid = (start + end) // 2
    new_rate = int(((y + mid) / (x + mid)) * 100) / 100
    if new_rate > rate:
      result = min(mid, result)
      end = mid - 1
    elif new_rate == rate:
      start = mid + 1
  print(result)