Add your answers to the Algorithms exercises here.

Exercise I
a).  O(n^3)

b). ?

c). O(n)

Exercise II
Step #1 -Ok, I would start by dropping an egg from the middle floor btw top & bottom floor math.floor(n/2)
Step #2 - Next, if the egg doesn't break, check the floor 1/2 between the current floor and the top.
Step#3 - If it breaks at this point, Repeat step #2, but, check the floor halfway between the current floor and the ground.
Step #4 - You can stop when two floors that are consecutive, the egg breaks dropped from one and doesn't break when dropped from the other. `f` = the floor from where the egg drop last.
**don't know if this would work or it makes sense.
