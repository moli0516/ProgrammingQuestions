class CircularQueue:
    def __init__(self, nums, n, start, end):
        self.nums = nums
        self.n = n
        self.start = start
        self.end = end

    def enq(self, k: int) -> None:
        if self.nums[self.end] != 0:
            return None
        self.nums[self.end] = k
        self.end = (self.end + 1) % self.n
        return None

    def deq(self) -> int:
        if self.nums[self.start] == 0:
            return -1
        val = self.nums[self.start]
        self.nums[self.start] = 0
        self.start = (self.start + 1) % self.n
        return val

    def isEmpty(self) -> bool:
        return self.start == self.end
    
def generateOutput():
    outputs = []
    inputs = eval(open('ProgrammingQuestion/data/0005/in.txt', 'r').read())
    for i in range(len(inputs)):
        obj = CircularQueue(**inputs[i][0])
        result = []
        for cmd, arg in zip(inputs[i][1], inputs[i][2]):
            if arg is not None:
                res = getattr(obj, cmd)(arg)
            else:
                res = getattr(obj, cmd)()
            result.append(res)
        outputs.append([result, obj.__dict__])
    return outputs

if __name__ == "__main__":
    output = generateOutput()
    with open('ProgrammingQuestion/data/0005/out.txt', 'w') as f:
        f.write(repr(output))