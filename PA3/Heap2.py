import traceback

class Heap(list):
    #Initialize a Heap.  Takes two inputs: array is the the list of
    #  Task objects, not necessarily all in max-heap format, and
    #  heap_size is the number of elements that are actually within
    #  the "heap" part of the array (usually 0 to start)
    def __init__(self,array,heap_size):
        self.heap_size = heap_size
        super().__init__(array)
    #Overloading the [] operator.  There is a point in the
    #  max_heap_insert code in the textbook where the psuedocode increases
    #  the heap_size by 1 and inserts an element there without checking
    #  whether the underlying array has room.  We avoid that problem
    #  by allowing indexing one past the end of the array to be interpreted
    #  as simply appending.
    def __setitem__(self,key,value):
        if key == len(self):
            self.append(value)
        else:
            super().__setitem__(key,value)
    #String representation of Heap objects.  We display the actual heap
    #  part of the array as surrounded by angle brackets; anything in
    #  the array but not in the heap is added after the ~~~End of Heap~~~
    #  marker.
    def __repr__(self):
        return "[<"+str(self[:self.heap_size])[1:-1]+\
               ">\n~~~End of Heap~~~"+str(self[self.heap_size:])[1:]
    #Heap equality: we only care that the elements that are in the heap
    #  section of the array match: those outside don't count.
    def __eq__(self,other):
        return (self[:self.heap_size] == other[:other.heap_size])




#Task class
#Each task has two instance variables:
#   self.description is a string describing what the task is
#   self.priority is a number representing the importance of the
#      task (higher values are more important)
class Task:
    def __init__(self,description,priority):
        self.description = description
        self.priority = priority
    def __repr__(self):
        return "\n"+str(self.priority) + ": " + self.description
    def __eq__(self,other):
        return type(self) == type(other) and \
               self.description == other.description and \
               self.priority == self.priority



#Test cases:

t1 = Task("'Accidentally' run into love interest",76)
t2 = Task("Brood over inner darkness",61)
t3 = Task("Lunch with Powerdude and Megagal",61)
t4 = Task("Pick up Laundry",89)
t5 = Task("Go to boring normal job as alter-ego",65)
t6 = Task("Comic relief with useless sidekick",1)
t7 = Task("Help clean up collateral damage",84)
t8 = Task("Receive key to city",33)
t9 = Task("Prevent bank robbery",96)
t10 = Task("Training montage",46)

t11 = Task("Take a nap",20)
t12 = Task("Defeat King Explosion Murder", 20)
t13 = Task("Walk Ultradog the Annhilator", 20)
t14 = Task("Escape elaborate deathtrap", 97)
t15 = Task("Respond to fanmail",16)

#Duplicate objects, in case originals corrupted by student code
d1 = Task("'Accidentally' run into love interest",76)
d2 = Task("Brood over inner darkness",61)
d3 = Task("Lunch with Powerdude and Megagal",61)
d4 = Task("Pick up Laundry",89)
d5 = Task("Go to boring normal job as alter-ego",65)
d6 = Task("Comic relief with useless sidekick",1)
d7 = Task("Help clean up collateral damage",84)
d8 = Task("Receive key to city",33)
d9 = Task("Prevent bank robbery",96)
d10 = Task("Training montage",46)

d11 = Task("Take a nap",20)
d12 = Task("Defeat King Explosion Murder", 20)
d13 = Task("Walk Ultradog the Annhilator", 20)
d14 = Task("Escape elaborate deathtrap", 97)
d15 = Task("Respond to fanmail",16)

count = 0

A = [t1,t2,t3,t4,t5]
B = Heap(A, 1)

print(B.heap_size)
