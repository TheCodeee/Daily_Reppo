# ========= METHOD 1 : ==============(for loop)
import time

x = int(input())
y = 0

for i in range(x + 1):
    y = y + i

print(y)

m = time.process_time()
print(m)
