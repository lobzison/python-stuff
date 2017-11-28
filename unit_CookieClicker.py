import CookieClicker as cook
import poc_simpletest

my_suite = poc_simpletest.TestSuite()
my_test = cook.ClickerState()
my_suite.run_test(my_test.time_until(100), 100)
my_suite.run_test(my_test.time_until(1), 1)
my_suite.run_test(my_test.time_until(-1), 0)

my_test.wait(-10)
my_suite.run_test(my_test.get_cookies(), 0)
my_test.wait(1)
my_suite.run_test(my_test.get_cookies(), 1)
my_test.wait(10)
my_suite.run_test(my_test.get_cookies(), 11)
my_test.wait(100)
my_suite.run_test(my_test.get_cookies(), 111)


my_suite.report_results()
print(str(my_test))
