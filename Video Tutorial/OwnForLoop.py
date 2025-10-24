def my_for_loop(item):

    iterator = iter(item)

    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break
    
L = [1,2,3]
my_for_loop(L)