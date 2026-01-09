test_cases = [
    # Test 1 - Basic operations
    [
        {'nums': [0, 0, 1, 2, 0], 'n': 5, 'start': 2, 'end': 4},
        ['deq', 'enq', 'enq', 'deq', 'deq', 'deq', 'isEmpty'],
        [None, 3, 4, None, None, None, None]
    ],
    
    # Test 2 - Fill, partially empty, fill more
    [
        {'nums': [1, 2, 3, 0, 0], 'n': 5, 'start': 0, 'end': 3},
        ['deq', 'deq', 'enq', 'enq', 'isEmpty', 'enq', 'deq', 'enq'],
        [None, None, 4, 5, None, 6, None, 7]
    ],
    
    # Test 3 - Empty queue operations
    [
        {'nums': [10, 20, 30, 40, 50], 'n': 5, 'start': 0, 'end': 5},
        ['deq', 'deq', 'deq', 'deq', 'deq', 'isEmpty', 'enq', 'isEmpty'],
        [None, None, None, None, None, None, 60, None]
    ],
    
    # Test 4 - Fill completely
    [
        {'nums': [0, 0, 0, 0, 0], 'n': 5, 'start': 0, 'end': 0},
        ['enq', 'enq', 'deq', 'enq', 'enq', 'deq', 'enq', 'enq', 'deq', 'isEmpty'],
        [1, 2, None, 3, 4, None, 5, 6, None, None]
    ],
    
    # Test 5 - Alternating pattern
    [
        {'nums': [100, 200, 0, 0, 0], 'n': 5, 'start': 0, 'end': 2},
        ['deq', 'enq', 'deq', 'enq', 'enq', 'deq', 'enq', 'isEmpty', 'enq'],
        [None, 300, None, 400, 500, None, 600, None, 700]
    ],
    
    # Test 6 - Complex mixed pattern
    [
        {'nums': [0]*8, 'n': 8, 'start': 0, 'end': 0},
        ['enq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [10, 20, None, 30, None, 40, None, 50, None, 60, None, 70, None]
    ],
    
    # Test 7 - Small queue wrap-around
    [
        {'nums': [9999, 0, 0, 0], 'n': 4, 'start': 0, 'end': 1},
        ['deq', 'enq', 'enq', 'isEmpty', 'enq', 'deq', 'deq', 'enq', 'isEmpty'],
        [None, 1, 2, None, 3, None, None, 4, None]
    ],
    
    # Test 8 - Rapid enqueue/dequeue
    [
        {'nums': [0]*3, 'n': 3, 'start': 0, 'end': 0},
        ['enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq'],
        [10, None, 20, None, None, 30, None, 40, None, None]
    ],
    
    # Test 9 - Empty then fill
    [
        {'nums': [5000, 6000, 7000, 0], 'n': 4, 'start': 0, 'end': 3},
        ['deq', 'deq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'enq', 'isEmpty'],
        [None, None, None, None, 8000, 9000, None, 10000, None]
    ],
    
    # Test 10 - Mixed with checking emptiness
    [
        {'nums': [0]*6, 'n': 6, 'start': 0, 'end': 0},
        ['enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'isEmpty'],
        [1, None, 2, None, 3, None, 4, None, None, 5, None, None]
    ],
    
    # Test 11 - Complex sequence
    [
        {'nums': [42, 0, 0, 0, 0], 'n': 5, 'start': 0, 'end': 1},
        ['deq', 'enq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'deq', 'enq', 'isEmpty'],
        [None, 1, 2, None, 3, None, 4, None, None, 5, None]
    ],
    
    # Test 12 - Alternating with checks
    [
        {'nums': [0]*7, 'n': 7, 'start': 0, 'end': 0},
        ['enq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [100, 200, None, None, 300, None, 400, None, None, 500, None, 600, None]
    ],
    
    # Test 13 - Random mixed
    [
        {'nums': [1234, 5678, 0, 0], 'n': 4, 'start': 0, 'end': 2},
        ['deq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [None, None, None, 999, 888, None, 777, None, None, 666]
    ],
    
    # Test 14 - Complex alternating
    [
        {'nums': [0]*9, 'n': 9, 'start': 0, 'end': 0},
        ['enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, None, 7]
    ],
    
    # Test 15 - Mixed with multiple checks
    [
        {'nums': [255, 511, 1023, 0, 0, 0], 'n': 6, 'start': 0, 'end': 3},
        ['deq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'enq', 'deq', 'enq', 'isEmpty', 'deq'],
        [None, None, 2047, None, None, 4095, 8191, None, 16383, None, None]
    ],
    
    # Test 16 - Pattern: enq, check, deq, enq
    [
        {'nums': [0]*10, 'n': 10, 'start': 0, 'end': 0},
        ['enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None]
    ],
    
    # Test 17 - Complex wrap-around
    [
        {'nums': [7777, 8888, 9999, 0, 0, 0, 0], 'n': 7, 'start': 0, 'end': 3},
        ['deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'enq', 'deq', 'enq', 'deq', 'isEmpty'],
        [None, 1111, None, 2222, None, None, 3333, 4444, None, 5555, None, None]
    ],
    
    # Test 18 - Medium size mixed
    [
        {'nums': [0]*12, 'n': 12, 'start': 0, 'end': 0},
        ['enq', 'enq', 'deq', 'isEmpty', 'enq', 'deq', 'enq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq'],
        [10, 20, None, None, 30, None, 40, 50, None, 60, None, None, 70, None, 80]
    ],
    
    # Test 19 - Complex pattern
    [
        {'nums': [1500, 2500, 3500, 4500, 0, 0], 'n': 6, 'start': 0, 'end': 4},
        ['deq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq'],
        [None, None, 5500, None, 6500, None, None, 7500, None, 8500, None, 9500]
    ],
    
    # Test 20 - Mixed with many isEmpty checks
    [
        {'nums': [0]*8, 'n': 8, 'start': 0, 'end': 0},
        ['enq', 'isEmpty', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq'],
        [1, None, 2, None, None, 3, None, 4, None, None, 5, None, 6, None, None]
    ],
    
    # Test 21 - Empty, fill, empty cycle
    [
        {'nums': [111, 222, 333, 444, 555, 0, 0, 0], 'n': 8, 'start': 0, 'end': 5},
        ['deq', 'deq', 'deq', 'deq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq'],
        [None, None, None, None, None, None, 666, 777, None, 888, None, 999, None, None]
    ],
    
    # Test 22 - Complex alternating with checks
    [
        {'nums': [0]*15, 'n': 15, 'start': 0, 'end': 0},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [1, None, None, 2, 3, None, 4, None, None, 5, None, 6, None, 7, None]
    ],
    
    # Test 23 - Random mixed operations
    [
        {'nums': [321, 654, 987, 0, 0, 0, 0, 0], 'n': 8, 'start': 0, 'end': 3},
        ['deq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'deq', 'enq', 'isEmpty'],
        [None, None, 123, None, 456, None, 789, 101, None, None, 202, None, 303, None]
    ],
    
    # Test 24 - Pattern: two enq, one deq
    [
        {'nums': [0]*10, 'n': 10, 'start': 0, 'end': 0},
        ['enq', 'enq', 'deq', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq'],
        [1, 2, None, 3, 4, None, None, 5, None, 6, None, 7, None, None]
    ],
    
    # Test 25 - Complex with wrap-around
    [
        {'nums': [999, 888, 777, 666, 555, 444, 0, 0, 0, 0], 'n': 10, 'start': 0, 'end': 6},
        ['deq', 'deq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'enq', 'deq', 'isEmpty'],
        [None, None, None, 333, None, 222, None, None, 111, None, 0, -1, None, None]
    ],
    
    # Test 26 - Small queue intensive
    [
        {'nums': [0]*3, 'n': 3, 'start': 0, 'end': 0},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'enq', 'deq', 'isEmpty', 'deq', 'enq', 'isEmpty'],
        [1, None, None, 2, 3, None, 4, None, None, None, 5, None]
    ],
    
    # Test 27 - Empty then operations
    [
        {'nums': [50, 60, 70, 80, 90], 'n': 5, 'start': 0, 'end': 5},
        ['deq', 'deq', 'deq', 'deq', 'deq', 'isEmpty', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq'],
        [None, None, None, None, None, None, 100, None, 110, None, 120, None, 130]
    ],
    
    # Test 28 - Alternating with isEmpty
    [
        {'nums': [0]*6, 'n': 6, 'start': 0, 'end': 0},
        ['enq', 'isEmpty', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [10, None, 20, None, 30, None, None, 40, None, 50, None, None, 60]
    ],
    
    # Test 29 - Medium complex pattern
    [
        {'nums': [0]*12, 'n': 12, 'start': 0, 'end': 0},
        ['enq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [1, 2, None, 3, None, None, 4, 5, None, None, 6, None, 7, None, 8, None]
    ],
    
    # Test 30 - Edge case: n=1
    [
        {'nums': [0], 'n': 1, 'start': 0, 'end': 0},
        ['enq', 'deq', 'isEmpty', 'enq', 'deq', 'isEmpty', 'enq', 'deq', 'isEmpty'],
        [1, None, None, 2, None, None, 3, None, None]
    ],
    
    # Test 31 - Pattern: fill, check, empty, check, fill
    [
        {'nums': [1000]*5 + [0]*5, 'n': 10, 'start': 0, 'end': 5},
        ['deq', 'deq', 'isEmpty', 'deq', 'deq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [None, None, None, None, None, None, None, 2000, 2001, None, 2002, None, 2003, None]
    ],
    
    # Test 32 - Complex random mix
    [
        {'nums': [0]*9, 'n': 9, 'start': 0, 'end': 0},
        ['enq', 'enq', 'deq', 'isEmpty', 'enq', 'deq', 'enq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [10, 20, None, None, 30, None, 40, 50, None, 60, None, None, 70, None, 80, None]
    ],
    
    # Test 33 - Mixed with frequent checks
    [
        {'nums': [0]*7, 'n': 7, 'start': 0, 'end': 0},
        ['enq', 'isEmpty', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty'],
        [1, None, 2, None, None, 3, None, None, 4, None, 5, None, None, 6, None]
    ],
    
    # Test 34 - Complex alternating pattern
    [
        {'nums': [42, 73, 19, 0, 0, 0], 'n': 6, 'start': 0, 'end': 3},
        ['deq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq'],
        [None, None, 100, None, 200, None, 300, None, 400, None, 500, None]
    ],
    
    # Test 35 - Mixed operations with checks
    [
        {'nums': [0]*8, 'n': 8, 'start': 0, 'end': 0},
        ['enq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'isEmpty', 'deq'],
        [1, 2, None, 3, None, None, 4, None, 5, None, 6, None, 7, None, None]
    ]
]

# Adding more tests to reach 75
for i in range(36, 76):
    n = (i % 20) + 5  # Vary n between 5 and 24
    start = i % n
    end = (i * 2) % n
    
    # Create mixed operations pattern
    operations = []
    args = []
    
    # Create a unique pattern for each test
    for j in range(min(20, n * 2)):  # Vary number of operations
        if j % 4 == 0:
            operations.append('enq')
            args.append(j * 100 + i)  # Unique value
        elif j % 4 == 1:
            operations.append('deq')
            args.append(None)
        elif j % 4 == 2:
            operations.append('isEmpty')
            args.append(None)
        else:
            operations.append('enq')
            args.append(j * 50 + i)  # Another unique value
    
    test_cases.append([
        {'nums': [0]*n, 'n': n, 'start': start, 'end': end},
        operations,
        args
    ])

f = open("ProgrammingQuestion/data/0005/in.txt", "w")
f.write(str(test_cases))
f.close()