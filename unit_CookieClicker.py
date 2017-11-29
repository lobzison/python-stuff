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

print 'LOOK HERE'
print cook.simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 50.0]}, 1.15),
                            16.0,
                            cook.strategy_cursor_broken)


my_suite.report_results()
print(str(my_test))


#[-11.1 pts]
# simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 50.0]}, 1.15), 16.0, < function strategy_cursor_broken at 0xfb40a2b0 >)
# expected obj: Time: 16.0 Current Cookies: 13.9125 CPS: 151.0 Total Cookies: 66.0 History(length: 4): [(0.0, None, 0.0, 0.0), (15.0, 'Cursor', 15.0, 15.0), ..., (16.0, 'Cursor', 19.837499999999999, 66.0)]
# but received(printed using your __str__ method)
# Current time: 16.000000 Current cookies: 34.000000 Total cookies: 66.000000, , , Current CPS: 101.000000


#[-2.2 pts]
# simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 0.10000000000000001],
#                                     'Portal': [1666666.0, 6666.0],
#                                     'Shipment': [40000.0, 100.0],
#                                     'Grandma': [100.0, 0.5],
#                                     'Farm': [500.0, 4.0],
#                                    'Time Machine': [123456789.0, 98765.0],
#                                     'Alchemy Lab': [200000.0, 400.0],
#                                     'Factory': [3000.0, 10.0],
#                                     'Antimatter Condenser': [3999999999.0, 999999.0],
#                                     'Mine': [10000.0, 40.0]}, 1.15), 10000000000.0,
#                                      <function strategy_expensive at 0xf9ed9730>)
# expected obj:
# Time: 10000000000.0 Current Cookies: 2414.64612076 CPS: 133980795.7 Total Cookies: 6.83676443443e+17
# History (length: 981): [(0.0, None, 0.0, 0.0), (3999999999.0, 'Antimatter Condenser', 3999999999.0, 3999999999.0), ..., (10000000000.0, 'Cursor', 9293.7698900500291, 6.836764434425321e+17)]
# but received (printed using your __str__ method)
# time: 10000000000.0 Current cookies: 93886686.000000 Current CPS: 133980751.000000 Total cookies: 683676443442532096.000000, ,

print '---->>LOOK HERE<<------'
print cook.simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 0.10000000000000001],
                                                'Portal': [1666666.0, 6666.0],
                                                'Shipment': [40000.0, 100.0],
                                                'Grandma': [100.0, 0.5],
                                                'Farm': [500.0, 4.0],
                                                'Time Machine': [123456789.0, 98765.0],
                                                'Alchemy Lab': [200000.0, 400.0],
                                                'Factory': [3000.0, 10.0],
                                                'Antimatter Condenser': [3999999999.0, 999999.0],
                                                'Mine': [10000.0, 40.0]}, 1.15),
                            10000000000.0,
                            cook.strategy_expensive)
