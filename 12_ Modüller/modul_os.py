import os

env = os.environ
i = 0
for key,value in env.items():
    i += 1
    print(f"{i}.{key} -> {value}")