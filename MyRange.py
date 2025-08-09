class my_range:

    def __init__(self,start,end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return my_range_helper(self)

class my_range_helper:

    def __init__(self,iterable_obj):
        self.iterator = iterable_obj

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterator.start>self.iterator.end:
            raise StopIteration

        current = self.iterator.start
        self.iterator.start+=1

        return current

for i in my_range(1,10):
    print(i)