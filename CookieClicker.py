"""
Cookie Clicker Simulator
"""
import math
import matplotlib.pyplot as plt

# Used to increase the timeout, if necessary

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0


class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._current_time = 0.0
        self._current_cps = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]

    def __str__(self):
        """
        Return human readable state
        """
        res = ('Total cookies: %f, Current cookies: %f,'
               'Current time: %f, Current CPS: %f') % (
            round(self._total_cookies), round(self._current_cookies),
            round(self._current_time), self._current_cps)
        return res

    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)

        Should return a float
        """
        return self._current_cookies

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self._history)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        cookies_left = cookies - self._current_cookies
        if cookies_left < 0:
            cookies_left = 0
        time = cookies_left / self._current_cps
        return math.ceil(time)

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0.0:
            self._current_time += time
            cookies_amount = time * self._current_cps
            self._current_cookies += cookies_amount
            self._total_cookies += cookies_amount

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost <= self._current_cookies:
            self._current_cookies -= cost
            self._current_cps += additional_cps
            self._history.append((self._current_time, item_name,
                                 cost, self._total_cookies))
        else:
            return


def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    game = ClickerState()
    info = build_info.clone()
    while game.get_time() < duration:
        time_left = duration - game.get_time()
        strtg = strategy(game.get_cookies(), game.get_cps(),
                         game.get_history(), time_left, info)
        if strtg is None:
            break
        time_to_w8 = game.time_until(info.get_cost(strtg))
        if game.get_time() + time_to_w8 > duration:
            break
        game.wait(time_to_w8)
        game.buy_item(strtg, info.get_cost(strtg), info.get_cps(strtg))
        info.update_item(strtg)

    time = duration - game.get_time()
    game.wait(time)
    strtg = strategy(game.get_cookies(), game.get_cps(),
                     game.get_history(), time_left, info)
    # while strtg is not None No fucking idea why this is infinte loop
    for _ in range(1000):
        strtg = strategy(game.get_cookies(), game.get_cps(),
                         game.get_history(), time_left, info)
        if strtg is None:
            break
        game.buy_item(strtg, info.get_cost(strtg), info.get_cps(strtg))
        info.update_item(strtg)

    # i = 0
    # while strtg is not None:
    # #for i in range(150):
    #     strtg = strategy(game.get_cookies(), game.get_cps(),
    #                      game.get_history(), 0, info)
    #     print strtg
    #     if strtg is None:
    #         print "END"
    #         break
    #     game.buy_item(strtg, info.get_cost(strtg), info.get_cps(strtg))            
    #     info.update_item(strtg)
    #     i += 1
    #     if i > 1000:
    #         print "BAD END"
    #         break

    #for item in info.build_items():
    #    print item, info.get_cost(item), info.get_cps(item)
    #for item in game.get_history():
    #    print item
    return game


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"


def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None


def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    cookies_next = cps * time_left
    total_cookies = cookies + cookies_next
    items = [[build_info.get_cost(item), item]
             for item in build_info.build_items()
             if build_info.get_cost(item) <= total_cookies]
    if items == []:
        cheapest_item = None
    else:
        cheapest_item = min(items)[1]
    return cheapest_item


def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    cookies_next = cps * time_left
    total_cookies = cookies + cookies_next
    items = [[build_info.get_cost(item), item]
             for item in build_info.build_items()
             if build_info.get_cost(item) <= total_cookies]
    #print cookies_next, total_cookies, items
    if items == []:
        expencive_item = None
        #print expencive_item
        #print('no more items')
    else:
        expencive_item = max(items)[1]
    return expencive_item


def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    cookies_next = cps * time_left
    total_cookies = cookies + cookies_next
    items = [[build_info.get_cps(item) / build_info.get_cost(item), item]
             for item in build_info.build_items()
             if build_info.get_cost(item) <= total_cookies]
    if items == []:
        expencive_item = None
    else:
        expencive_item = max(items)[1]
    return expencive_item


def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)


def run():
    """
    Run the simulator.
    """
    run_strategy("Cursor", SIM_TIME, strategy_best)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)


run()
