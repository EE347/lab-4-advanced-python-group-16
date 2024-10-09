with open("task3.txt", 'r') as f:
    names = f.readlines()
    [print(name,end="") for name in names]
