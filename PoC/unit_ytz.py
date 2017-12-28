import ytz
import poc_simpletest
import test

my_suite = poc_simpletest.TestSuite()
# score tests
my_suite.run_test(ytz.score((1, 1)), 2)
my_suite.run_test(ytz.score((1, 2)), 2)
my_suite.run_test(ytz.score((1, 2, 3)), 3)
my_suite.run_test(ytz.score((1, 1, 2, 2)), 4)
my_suite.run_test(ytz.score((1, 1, 2, 2, 2)), 6)
my_suite.run_test(ytz.score((1, 2, 4, 5, 5)), 10)
my_suite.run_test(ytz.score((1, 3, 3, 5, 6)), 6)
my_suite.run_test(ytz.score((3, 3, 3, 5, 6)), 9)
my_suite.run_test(ytz.score((1, 2, 3, 4, 5)), 5)
my_suite.run_test(ytz.score((5, 5, 5, 5, 5)), 25)

my_suite.run_test(ytz.gen_all_holds((1, 2, 3)), set(
    [(), (1, 2, 3), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3)]))
my_suite.run_test(ytz.gen_all_holds((1, 1, 1)),
                  set([(), (1,), (1, 1), (1, 1, 1)]))
my_suite.run_test(ytz.gen_all_holds((1, 1, 2)), set(
    [(), (1,), (2,), (1, 1), (1, 2), (1, 1, 2)]))

my_suite.report_results()
test.run_suite(ytz.gen_all_holds)

my_suite.run_test(ytz.expected_value((2,), 6, 1), 4.0)

my_suite.run_test(round(ytz.expected_value((1, 2, 3, 4, 5), 6, 1), 1), 6.7)

my_suite.run_test(ytz.expected_value(tuple([]), 6, 5), 3.5)
