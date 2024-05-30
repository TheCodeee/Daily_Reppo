# =========== METHOD 2 =============(While loop)
import time

a = int(input())
b = 0
Run = True

while Run:
    b = b + a
    a -= 1
    if a == 0:
        Run = False

print(b)

n = time.process_time()
print(n)
