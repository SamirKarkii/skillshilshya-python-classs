# everything you can loop over is an iterable .
"""
If you can do this:
for x in something:
    ....
then something is iteraable .
"""

# common iterables in python 
# string = "hello"
# lists = [1,2,3]
# Tuples = (1,2,3)
# Dictionaries = {'a':1, 'b':2}
# sets = {1,34}
# files =open(file.txt)
# anything that implements _iter_() or _getitem_() properly

"String = a sequence of characters (and yes, it's an iterable )"

#A string is basically a list of charactrtd that's read-only.
"that means we can loop over "
# for ch in "python":
#     print(ch)

#but you can't modify a character directly :
# s = "python"
# s[0] = "a"
"why? Because strings are immutable . Python does this for performance + memory optimization"
#if you want to "modify" a string , you actually but a new one:

# s = "python"
# s = "P" + s[1:]


# Iterable vs Iterator (pro -level distinction)

#Iterable
"A container that can give you an iterator ."
#Examples: A playlist of a song .
"""
"hello"
[1,2,3]
(4,5,60
"""

#Iterator:
"An object that produces one item at a time , and remembers where it left off"
# example: A music player that's currently playing through the playlist.

#You get iterator  by doing:
# it = iter("abc")
# print(next(it)) #a 
# print(next(it)) #b
# print(next(it)) #c
# print(next(it)) #stopsIteration  
#That 'stop' iteration is what singnals the end of loop internally.


#how a for - loop actually works(internals like a pro )  

# for ch in "abc":
#     print(ch)

#is secreately doing :

iterator = iter("abc")
while True:
    try:
        ch = next(iterator)
    except StopIteration:
        break
    print(ch)

