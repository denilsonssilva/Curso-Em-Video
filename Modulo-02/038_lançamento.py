from time import sleep as sl

for i in range(10, 0, -1):
    print(i, end=' -> ', flush=True)
    sl(0.5)

    