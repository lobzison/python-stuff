import zombies
import poc_simpletest

test_sute = poc_simpletest.TestSuite()

test_sute.run_test

test1 = zombies.Apocalypse(2, 2, [[1, 1]])


print test1
test1.clear()
print test1
test1.add_zombie(0, 0)
print test1.num_zombies()
test1.add_zombie(1, 0)
print test1.num_zombies()
test1.add_zombie(0, 1)
for zombie in test1.zombies():
    print zombie

for row, col in test1.zombies():
    print row, col

test2 = zombies.Apocalypse(7, 8)

test2.add_zombie(6, 3)

test2.add_zombie(1, 7)


test2.add_human(4, 7)

test2.move_humans(test2.compute_distance_field(zombies.ZOMBIE))
print test2

test3 = zombies.Apocalypse(20, 30)

print test3.compute_distance_field(zombies.HUMAN)

test4 = zombies.Apocalypse(3, 3, [], [(2, 2)], [(1, 1)])
print test4

obj = zombies.Apocalypse(3, 3, [(0, 0), (0, 1), (0, 2), (1, 0)], [(2, 1)], [(1, 1)])

print obj

dist = [[9, 9, 9],
        [9, 1, 2],
        [1, 0, 1]]

obj.move_zombies(dist)
obj.humans()
print obj

obj = zombies.Apocalypse(3, 3, [(0, 0), (0, 1), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)], [(0, 2)], [(1, 1)])
dist = [[9, 9, 0], [9, 9, 9], [9, 9, 9]]
print obj
obj.move_humans(dist)
print obj
obj.humans()
# expected location to be one of [(1, 1)] but received (0, 2)
print "---><----"
obj = zombies.Apocalypse(3, 3, [], [(1, 1)], [(1, 1)])
print obj
dist = [[2, 1, 2],
        [1, 0, 1],
        [2, 1, 2]]
obj.move_zombies(dist)
print obj
#[(1, 1)] but received (0, 1)



