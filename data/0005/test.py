def loadInput(id):
    with open("in.txt", "r", encoding="utf-8") as f:
        loadedList = eval(f.readline())
        return loadedList

print(loadInput("0005")[0])