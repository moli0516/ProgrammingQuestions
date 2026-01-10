import random
test_cases = [
    # Test 1: Basic operations
    [
        {'nums': [0, 0, 1, 2, 0], 'n': 5, 'start': 2, 'end': 3},
        ['deq', 'enq', 'enq', 'deq', 'deq', 'deq', 'isEmpty'],
        [None, 3, 4, None, None, None, None]
    ],
    
    # Test 2: Mixed operations with wrap-around
    [
        {'nums': [1, 2, 3, 0, 0], 'n': 5, 'start': 0, 'end': 2},
        ['deq', 'deq', 'enq', 'enq', 'isEmpty', 'enq', 'deq', 'enq'],
        [None, None, 4, 5, None, 6, None, 7]
    ],
    
    # Test 3: Empty queue then operations
    [
        {'nums': [0, 0, 0, 0, 0], 'n': 5, 'start': 0, 'end': 0},
        ['enq', 'enq', 'deq', 'enq', 'enq', 'deq', 'enq', 'enq', 'deq', 'isEmpty'],
        [1, 2, None, 3, 4, None, 5, 6, None, None]
    ],
    
    # Test 4: Complex mixed pattern
    [
        {'nums': [100, 200, 0, 0, 0], 'n': 5, 'start': 0, 'end': 1},
        ['deq', 'enq', 'deq', 'enq', 'enq', 'deq', 'enq', 'isEmpty', 'enq'],
        [None, 300, None, 400, 500, None, 600, None, 700]
    ],
    
    # Test 5: Small queue intensive
    [
        {'nums': [0, 0, 0, 0], 'n': 4, 'start': 0, 'end': 0},
        ['enq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'deq', 'enq', 'isEmpty'],
        [1, 2, None, 3, None, 4, None, None, 5, None]
    ],
    
    # Test 6: Alternating pattern
    [
        {'nums': [0, 0, 0, 0, 0, 0], 'n': 6, 'start': 0, 'end': 0},
        ['enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [10, None, 20, None, 30, None, 40, None, 50, None, 60, None]
    ],
    
    # Test 7: Edge case n=1
    [
        {'nums': [0], 'n': 1, 'start': 0, 'end': 0},
        ['enq', 'deq', 'isEmpty', 'enq', 'deq', 'isEmpty', 'enq', 'deq', 'isEmpty'],
        [1, None, None, 2, None, None, 3, None, None]
    ],
    
    # Test 8: Fill and empty cycle
    [
        {'nums': [0, 0, 0, 0, 0], 'n': 5, 'start': 0, 'end': 0},
        ['enq', 'enq', 'enq', 'deq', 'deq', 'enq', 'enq', 'deq', 'deq', 'enq', 'isEmpty'],
        [1, 2, 3, None, None, 4, 5, None, None, 6, None]
    ],
    
    # Test 9: Random mixed operations
    [
        {'nums': [0, 0, 0, 0, 0, 0, 0], 'n': 7, 'start': 0, 'end': 0},
        ['enq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [100, 200, None, None, 300, None, 400, None, None, 500, None, 600, None]
    ],
    
    # Test 10: Complex sequence with checks
    [
        {'nums': [0, 0, 0, 0, 0, 0, 0, 0], 'n': 8, 'start': 0, 'end': 0},
        ['enq', 'isEmpty', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq'],
        [1, None, 2, None, None, 3, None, 4, None, None, 5, None, 6, None, None]
    ],
    
    # Test 11: Medium size mixed
    [
        {'nums': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'n': 10, 'start': 0, 'end': 0},
        ['enq', 'enq', 'deq', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq'],
        [1, 2, None, 3, 4, None, None, 5, None, 6, None, 7, None, None]
    ],
    
    # Test 12: Stress test with many operations
    [
        {'nums': [0]*15, 'n': 15, 'start': 0, 'end': 0},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [1, None, None, 2, 3, None, 4, None, None, 5, None, 6, None, 7, None]
    ],
    
    # Test 13: Pattern: two enq, one deq
    [
        {'nums': [0]*12, 'n': 12, 'start': 0, 'end': 0},
        ['enq', 'enq', 'deq', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq'],
        [1, 2, None, 3, 4, None, None, 5, None, 6, None, 7, None, None]
    ],
    
    # Test 14: Random mixed values
    [
        {'nums': [42, 73, 19, 0, 0, 0], 'n': 6, 'start': 0, 'end': 2},
        ['deq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq'],
        [None, None, 100, None, 200, None, 300, None, 400, None, 500, None]
    ],
    
    # Test 15: Complex wrap-around
    [
        {'nums': [0, 0, 0, 0, 0], 'n': 5, 'start': 3, 'end': 3},
        ['enq', 'enq', 'enq', 'enq', 'deq', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [1, 2, 3, 4, None, None, 5, None, 6, None]
    ],
    
    # Test 16
    [
        {'nums': [0]*8, 'n': 8, 'start': 4, 'end': 4},
        ['enq', 'enq', 'deq', 'enq', 'deq', 'enq', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [10, 20, None, 30, None, 40, 50, None, 60, None, 70, None]
    ],
    
    # Test 17
    [
        {'nums': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'n': 9, 'start': 5, 'end': 5},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq'],
        [1, None, None, 2, 3, None, None, 4, 5, None, None, 6]
    ],
    
    # Test 18
    [
        {'nums': [0]*11, 'n': 11, 'start': 7, 'end': 7},
        ['enq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [100, 200, None, 300, None, None, 400, 500, None, 600, None, 700, None]
    ],
    
    # Test 19
    [
        {'nums': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'n': 12, 'start': 0, 'end': 0},
        ['enq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [1, 2, None, 3, None, None, 4, 5, None, None, 6, None, 7, None, 8, None]
    ],
    
    # Test 20
    [
        {'nums': [0]*13, 'n': 13, 'start': 8, 'end': 8},
        ['enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, None, 7]
    ],
    
    # Test 21
    [
        {'nums': [0]*14, 'n': 14, 'start': 10, 'end': 10},
        ['enq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [10, 20, None, None, 30, None, 40, None, None, 50, None, 60, None, 70, None]
    ],
    
    # Test 22
    [
        {'nums': [0]*16, 'n': 16, 'start': 12, 'end': 12},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq'],
        [1, None, None, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8]
    ],
    
    # Test 23
    [
        {'nums': [0]*17, 'n': 17, 'start': 5, 'end': 5},
        ['enq', 'enq', 'deq', 'enq', 'enq', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [1, 2, None, 3, 4, None, 5, None, 6, None, 7, None, 8, None]
    ],
    
    # Test 24
    [
        {'nums': [0]*18, 'n': 18, 'start': 9, 'end': 9},
        ['enq', 'isEmpty', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty'],
        [1, None, 2, None, None, 3, None, None, 4, None, 5, None, None, 6, None]
    ],
    
    # Test 25
    [
        {'nums': [0]*19, 'n': 19, 'start': 14, 'end': 14},
        ['enq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq'],
        [1, 2, None, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, None]
    ],
    
    # Test 26
    [
        {'nums': [0]*20, 'n': 20, 'start': 15, 'end': 15},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq'],
        [1, None, None, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None]
    ],
    
    # Test 27
    [
        {'nums': [0]*21, 'n': 21, 'start': 18, 'end': 18},
        ['enq', 'enq', 'deq', 'isEmpty', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [10, 20, None, None, 30, None, 40, None, None, 50, None, 60, None, None, 70, None, 80, None]
    ],
    
    # Test 28
    [
        {'nums': [0]*22, 'n': 22, 'start': 10, 'end': 10},
        ['enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, None, 7, None, 8, None]
    ],
    
    # Test 29
    [
        {'nums': [0]*23, 'n': 23, 'start': 17, 'end': 17},
        ['enq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [100, 200, None, None, 300, None, 400, None, None, 500, None, 600, None, None, 700, None, 800, None]
    ],
    
    # Test 30
    [
        {'nums': [0]*24, 'n': 24, 'start': 12, 'end': 12},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq'],
        [1, None, None, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10]
    ],
    
    # Test 31
    [
        {'nums': [0]*25, 'n': 25, 'start': 20, 'end': 20},
        ['enq', 'enq', 'deq', 'enq', 'enq', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [1, 2, None, 3, 4, None, 5, None, 6, None, 7, None, 8, None]
    ],
    
    # Test 32
    [
        {'nums': [0]*26, 'n': 26, 'start': 15, 'end': 15},
        ['enq', 'isEmpty', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty'],
        [1, None, 2, None, None, 3, None, None, 4, None, 5, None, None, 6, None, None, 7, None]
    ],
    
    # Test 33
    [
        {'nums': [0]*27, 'n': 27, 'start': 22, 'end': 22},
        ['enq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq'],
        [1, 2, None, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, None, 9, None]
    ],
    
    # Test 34
    [
        {'nums': [0]*28, 'n': 28, 'start': 18, 'end': 18},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq'],
        [10, None, None, 20, 30, None, None, 40, 50, None, None, 60, 70, None, None, 80, 90, None, None, 100]
    ],
    
    # Test 35
    [
        {'nums': [0]*29, 'n': 29, 'start': 25, 'end': 25},
        ['enq', 'enq', 'deq', 'isEmpty', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [1, 2, None, None, 3, None, 4, None, None, 5, None, 6, None, None, 7, None, 8, None, None, 9]
    ],
    
    # Test 36
    [
        {'nums': [0]*30, 'n': 30, 'start': 20, 'end': 20},
        ['enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq'],
        [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, None, 7, None, 8, None, None, 9, None]
    ],
    
    # Test 37
    [
        {'nums': [0]*31, 'n': 31, 'start': 27, 'end': 27},
        ['enq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [10, 20, None, None, 30, None, 40, None, None, 50, None, 60, None, None, 70, None, 80, None, None, 90]
    ],
    
    # Test 38
    [
        {'nums': [0]*32, 'n': 32, 'start': 24, 'end': 24},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq'],
        [1, None, None, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10]
    ],
    
    # Test 39
    [
        {'nums': [0]*33, 'n': 33, 'start': 29, 'end': 29},
        ['enq', 'enq', 'deq', 'enq', 'enq', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty'],
        [1, 2, None, 3, 4, None, 5, None, 6, None, 7, None, 8, None, None, 9, None, 10, None]
    ],
    
    # Test 40
    [
        {'nums': [0]*34, 'n': 34, 'start': 25, 'end': 25},
        ['enq', 'isEmpty', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [1, None, 2, None, None, 3, None, None, 4, None, 5, None, None, 6, None, None, 7, None, None, 8]
    ],
    
    # Test 41
    [
        {'nums': [0]*35, 'n': 35, 'start': 30, 'end': 30},
        ['enq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq'],
        [1, 2, None, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, None, 9, None, 10]
    ],
    
    # Test 42
    [
        {'nums': [0]*36, 'n': 36, 'start': 28, 'end': 28},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq'],
        [10, None, None, 20, 30, None, None, 40, 50, None, None, 60, 70, None, None, 80, 90, None, None, 100]
    ],
    
    # Test 43
    [
        {'nums': [0]*37, 'n': 37, 'start': 33, 'end': 33},
        ['enq', 'enq', 'deq', 'isEmpty', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [1, 2, None, None, 3, None, 4, None, None, 5, None, 6, None, None, 7, None, 8, None, None, 9]
    ],
    
    # Test 44
    [
        {'nums': [0]*38, 'n': 38, 'start': 30, 'end': 30},
        ['enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq'],
        [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, None, 7, None, 8, None, None, 9, None]
    ],
    
    # Test 45
    [
        {'nums': [0]*39, 'n': 39, 'start': 35, 'end': 35},
        ['enq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [10, 20, None, None, 30, None, 40, None, None, 50, None, 60, None, None, 70, None, 80, None, None, 90]
    ],
    
    # Test 46
    [
        {'nums': [0]*40, 'n': 40, 'start': 32, 'end': 32},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq'],
        [1, None, None, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10]
    ],
    
    # Test 47
    [
        {'nums': [0]*41, 'n': 41, 'start': 37, 'end': 37},
        ['enq', 'enq', 'deq', 'enq', 'enq', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq'],
        [1, 2, None, 3, 4, None, 5, None, 6, None, 7, None, 8, None, None, 9, None, 10, None, None]
    ],
    
    # Test 48
    [
        {'nums': [0]*42, 'n': 42, 'start': 38, 'end': 38},
        ['enq', 'isEmpty', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [1, None, 2, None, None, 3, None, None, 4, None, 5, None, None, 6, None, None, 7, None, None, 8]
    ],
    
    # Test 49
    [
        {'nums': [0]*43, 'n': 43, 'start': 40, 'end': 40},
        ['enq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq'],
        [1, 2, None, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, None, 9, None, 10]
    ],
    
    # Test 50
    [
        {'nums': [0]*44, 'n': 44, 'start': 36, 'end': 36},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq'],
        [10, None, None, 20, 30, None, None, 40, 50, None, None, 60, 70, None, None, 80, 90, None, None, 100]
    ],
    
    # Test 51
    [
        {'nums': [0]*45, 'n': 45, 'start': 42, 'end': 42},
        ['enq', 'enq', 'deq', 'isEmpty', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [1, 2, None, None, 3, None, 4, None, None, 5, None, 6, None, None, 7, None, 8, None, None, 9]
    ],
    
    # Test 52
    [
        {'nums': [0]*46, 'n': 46, 'start': 40, 'end': 40},
        ['enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq'],
        [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, None, 7, None, 8, None, None, 9, None]
    ],
    
    # Test 53
    [
        {'nums': [0]*47, 'n': 47, 'start': 44, 'end': 44},
        ['enq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [10, 20, None, None, 30, None, 40, None, None, 50, None, 60, None, None, 70, None, 80, None, None, 90]
    ],
    
    # Test 54
    [
        {'nums': [0]*48, 'n': 48, 'start': 42, 'end': 42},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq'],
        [1, None, None, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10]
    ],
    
    # Test 55
    [
        {'nums': [0]*49, 'n': 49, 'start': 46, 'end': 46},
        ['enq', 'enq', 'deq', 'enq', 'enq', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq'],
        [1, 2, None, 3, 4, None, 5, None, 6, None, 7, None, 8, None, None, 9, None, 10, None, None]
    ],
    
    # Test 56
    [
        {'nums': [0]*50, 'n': 50, 'start': 45, 'end': 45},
        ['enq', 'isEmpty', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [1, None, 2, None, None, 3, None, None, 4, None, 5, None, None, 6, None, None, 7, None, None, 8]
    ],
    
    # Test 57
    [
        {'nums': [0]*51, 'n': 51, 'start': 48, 'end': 48},
        ['enq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq'],
        [1, 2, None, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, None, 9, None, 10]
    ],
    
    # Test 58
    [
        {'nums': [0]*52, 'n': 52, 'start': 46, 'end': 46},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq'],
        [10, None, None, 20, 30, None, None, 40, 50, None, None, 60, 70, None, None, 80, 90, None, None, 100]
    ],
    
    # Test 59
    [
        {'nums': [0]*53, 'n': 53, 'start': 50, 'end': 50},
        ['enq', 'enq', 'deq', 'isEmpty', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [1, 2, None, None, 3, None, 4, None, None, 5, None, 6, None, None, 7, None, 8, None, None, 9]
    ],
    
    # Test 60
    [
        {'nums': [0]*54, 'n': 54, 'start': 48, 'end': 48},
        ['enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq'],
        [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, None, 7, None, 8, None, None, 9, None]
    ],
    
    # Test 61
    [
        {'nums': [0]*55, 'n': 55, 'start': 52, 'end': 52},
        ['enq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [10, 20, None, None, 30, None, 40, None, None, 50, None, 60, None, None, 70, None, 80, None, None, 90]
    ],
    
    # Test 62
    [
        {'nums': [0]*56, 'n': 56, 'start': 50, 'end': 50},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq'],
        [1, None, None, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10]
    ],
    
    # Test 63
    [
        {'nums': [0]*57, 'n': 57, 'start': 54, 'end': 54},
        ['enq', 'enq', 'deq', 'enq', 'enq', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq'],
        [1, 2, None, 3, 4, None, 5, None, 6, None, 7, None, 8, None, None, 9, None, 10, None, None]
    ],
    
    # Test 64
    [
        {'nums': [0]*58, 'n': 58, 'start': 52, 'end': 52},
        ['enq', 'isEmpty', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [1, None, 2, None, None, 3, None, None, 4, None, 5, None, None, 6, None, None, 7, None, None, 8]
    ],
    
    # Test 65
    [
        {'nums': [0]*59, 'n': 59, 'start': 56, 'end': 56},
        ['enq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq'],
        [1, 2, None, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, None, 9, None, 10]
    ],
    
    # Test 66
    [
        {'nums': [0]*60, 'n': 60, 'start': 54, 'end': 54},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq'],
        [10, None, None, 20, 30, None, None, 40, 50, None, None, 60, 70, None, None, 80, 90, None, None, 100]
    ],
    
    # Test 67
    [
        {'nums': [0]*61, 'n': 61, 'start': 58, 'end': 58},
        ['enq', 'enq', 'deq', 'isEmpty', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [1, 2, None, None, 3, None, 4, None, None, 5, None, 6, None, None, 7, None, 8, None, None, 9]
    ],
    
    # Test 68
    [
        {'nums': [0]*62, 'n': 62, 'start': 56, 'end': 56},
        ['enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq'],
        [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, None, 7, None, 8, None, None, 9, None]
    ],
    
    # Test 69
    [
        {'nums': [0]*63, 'n': 63, 'start': 60, 'end': 60},
        ['enq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [10, 20, None, None, 30, None, 40, None, None, 50, None, 60, None, None, 70, None, 80, None, None, 90]
    ],
    
    # Test 70
    [
        {'nums': [0]*64, 'n': 64, 'start': 58, 'end': 58},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq'],
        [1, None, None, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10]
    ],
    
    # Test 71
    [
        {'nums': [0]*65, 'n': 65, 'start': 62, 'end': 62},
        ['enq', 'enq', 'deq', 'enq', 'enq', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq'],
        [1, 2, None, 3, 4, None, 5, None, 6, None, 7, None, 8, None, None, 9, None, 10, None, None]
    ],
    
    # Test 72
    [
        {'nums': [0]*66, 'n': 66, 'start': 60, 'end': 60},
        ['enq', 'isEmpty', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [1, None, 2, None, None, 3, None, None, 4, None, 5, None, None, 6, None, None, 7, None, None, 8]
    ],
    
    # Test 73
    [
        {'nums': [0]*67, 'n': 67, 'start': 64, 'end': 64},
        ['enq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'enq', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq'],
        [1, 2, None, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, None, 9, None, 10]
    ],
    
    # Test 74
    [
        {'nums': [0]*68, 'n': 68, 'start': 62, 'end': 62},
        ['enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq', 'enq', 'deq', 'isEmpty', 'enq'],
        [10, None, None, 20, 30, None, None, 40, 50, None, None, 60, 70, None, None, 80, 90, None, None, 100]
    ],
    
    # Test 75
    [
        {'nums': [0]*69, 'n': 69, 'start': 66, 'end': 66},
        ['enq', 'enq', 'deq', 'isEmpty', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq', 'deq', 'enq', 'isEmpty', 'deq', 'enq'],
        [1, 2, None, None, 3, None, 4, None, None, 5, None, 6, None, None, 7, None, 8, None, None, 9]
    ]
]

# Adding more tests to reach 75
for i in range(100, 200):
    n = i * 5  # Vary n between 5 and 24
    start = random.randint(0, n - 1)
    end = random.randint(0, n - 1)
    nums = [0] * n
    if end == start:
        end -= 1
    if start > end:
        for i in range(start, n):
            nums[i] = random.randint(1, 10000)
        for i in range(0, end):
            nums[i] = random.randint(1, 10000)
    else:
        for i in range(start, end):
            nums[i] = random.randint(1, 10000)
    
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
        {'nums': nums, 'n': n, 'start': start, 'end': end},
        operations,
        args
    ])

f = open("ProgrammingQuestion/data/0005/in.txt", "w")
f.write(str(test_cases))
f.close()