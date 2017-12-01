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


for line in test2.compute_distance_field(zombies.ZOMBIE):
	print line