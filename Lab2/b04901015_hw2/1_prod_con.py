n_item = 0

def Producer(n):
    global n_item
    for i in range(n):
        #assert 0
        yield
        yield
        yield
        print("Put an item")
        n_item += 1

def Consumer(n):
    global n_item
    n_get = 0
    while n_get < n:
        #assert 0
        yield
        yield
        if n_item > 0:
            print("Get an item")
            n_item -= 1
            n_get += 1

def main_loop(threads):
    from itertools import zip_longest
    for dummy in zip_longest(*threads):
        print("=== clk ===")

main_loop([Producer(10), Consumer(10)])
#main_loop([Consumer(10), Producer(10)])
