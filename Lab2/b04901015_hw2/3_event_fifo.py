n_item = 0
INIT_EVENT = 5
CLOCK_EVENT = 7
WRITE_EVENT = 11

def Clk(n):
    yield INIT_EVENT
    for i in range(n):
        # TODO
        #pass
        TriggerEvent(CLOCK_EVENT)
        yield CLOCK_EVENT

def Producer(n):
    global n_item
    yield INIT_EVENT
    for i in range(n):
        yield CLOCK_EVENT
        yield CLOCK_EVENT
        yield CLOCK_EVENT
        n_item += 1
        print("Put an item")
        TriggerEvent(WRITE_EVENT)

def GetItem():
    # TODO
    #pass
    global n_item
    while True:
        yield CLOCK_EVENT       
        if n_item == 0:
            yield WRITE_EVENT
            print("Get an item")
        n_item -= 1

def Consumer(n):
    n_get = 0
    yield INIT_EVENT
    while n_get < n:
        yield from GetItem()
        n_get += 1

from collections import deque
event_pending_on_list = [list() for _ in range(100)]
event_pending = deque()
event_pending.append(INIT_EVENT)

def TriggerEvent(idx):
    # TODO
    #pass
    event_pending.append(idx)

def WaitOnNextEvent(t):
    try:
        waiting_on = next(t)
        event_pending_on_list[waiting_on].append(t)
    except StopIteration:
        pass

def main_loop(threads):
    for t in threads:
        WaitOnNextEvent(t)
    # while what?
    while event_pending:
        # TODO
        trigger = event_pending.popleft()
        print("handling {}".format(trigger))
        handling, event_pending_on_list[trigger] = event_pending_on_list[trigger], list()
        for t in handling:
            WaitOnNextEvent(t)

main_loop([Clk(100), Producer(10), Consumer(10)])
