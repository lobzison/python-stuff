import CookieClicker as cook
import poc_simpletest
import poc_clicker_provided as provided

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


my_test.buy_item("Test item", 100, 1)
my_suite.run_test(my_test.get_cookies(), 11)
my_suite.run_test(my_test.get_cps(), 2)
my_suite.run_test(my_test.get_history(), [(0.0, None, 0.0, 0.0),
                                          (111.0, 'Test item', 100, 111.0)])

my_test = cook.ClickerState()
res = cook.ClickerState()
res.current_cookies = 6965195661.0
res.total_cookies = 153308849166.0
res.current_time = 10000000000.0
res.current_cps = 16.1
my_suite.run_test(str(cook.simulate_clicker(provided.BuildInfo(),
                                            cook.SIM_TIME,
                                            cook.strategy_cursor_broken)),
                  str(res))


my_suite.report_results()
print(str(my_test))
