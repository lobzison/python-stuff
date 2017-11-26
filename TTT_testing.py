import user43_ph1PvFBktU_10 as mycode
import poc_simpletest
import poc_ttt_provided as provided


def count_cells(grid):
    cnt = 0
    summ = 0
    for row in grid:
        for cell in row:
            summ += cell
            cnt += 1
    return (summ, cnt)


testsute = poc_simpletest.TestSuite()

a = provided.TTTBoard(3)
b = provided.TTTBoard(4)
c = provided.TTTBoard(5)

c.move(1, 1, provided.PLAYERX)
c.move(3, 3, provided.PLAYERO)

a_g = mycode.mc_make_scores_grid(a)
b_g = mycode.mc_make_scores_grid(b)
c_g = mycode.mc_make_scores_grid(c)

mycode.mc_trial(a, provided.PLAYERX)
mycode.mc_trial(b, provided.PLAYERO)
mycode.mc_trial(c, provided.PLAYERX)

testsute.run_test(a.get_empty_squares(), [])
testsute.run_test(b.get_empty_squares(), [])
testsute.run_test(c.get_empty_squares(), [])
testsute.run_test(count_cells(a_g), (0, 3 ** 2))
testsute.run_test(count_cells(b_g), (0, 4 ** 2))
testsute.run_test(count_cells(c_g), (0, 5 ** 2))

a.move(0, 0, provided.PLAYERX)
a.move(1, 0, provided.PLAYERX)
a.move(0, 1, provided.PLAYERO)
a.move(0, 2, provided.PLAYERX)
a.move(1, 1, provided.PLAYERX)
a.move(1, 2, provided.PLAYERO)
a.move(2, 0, provided.PLAYERO)
#a.move(1, 1, provided.PLAYERX)

a = provided.TTTBoard(3)
b = mc_make_scores_grid(a)

a.move(0, 0, provided.PLAYERX)
a.move(1, 0, provided.PLAYERX)
a.move(0, 1, provided.PLAYERO)
a.move(0, 2, provided.PLAYERX)
a.move(1, 1, provided.PLAYERX)
a.move(1, 2, provided.PLAYERO)
a.move(2, 0, provided.PLAYERO)
#a.move(1, 1, provided.PLAYERX)

# FIX STRANGE ISSUE WITH NO WINS

for i in range(50):
    c = a.clone()
    mc_trial(c, provided.PLAYERO)
    mc_update_scores(b, c, provided.PLAYERO)
    if c.check_win() == provided.PLAYERO:
        print('WIN')
    print(c)
    for n in b:
        print(n)


testsute.report_results()
