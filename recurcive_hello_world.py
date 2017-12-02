def triangular_summ(num):
    if num == 1:
        return 1
    else:
        return num + triangular_summ(num - 1)


print triangular_summ(10)
print triangular_summ(20)
print triangular_summ(4)


def number_of_threes(num):
    if len(str(num)) == 1:
        if num == 3:
            return 1
        else:
            return 0
    else:
        if str(num)[0] == "3":
            return number_of_threes(int(str(num)[1:])) + 1
        else:
            return number_of_threes(int(str(num)[1:]))


def number_of_threes2(num):
    if num == 0:
        return 0
    else:
        last_digit = num % 10
        rest_or_digits = num // 10
        if last_digit == 3:
            return number_of_threes2(rest_or_digits) + 1
        else:
            return number_of_threes2(rest_or_digits)


print number_of_threes(31233123145643635635)
print number_of_threes2(31233123145643635635)


def is_member(my_list, elem):
    if my_list == []:
        return False
    else:
        return my_list[0] == elem or is_member(my_list[1:], elem)


print is_member(['c', 'a', 't'], 'a')
print "Computed:", is_member([], 1), "Expected: False"
print "Computed:", is_member([1], 1), "Expected: True"
print "Computed:", is_member(['c', 'a', 't'], 't'), "Expected: True"
print "Computed:", is_member(['c', 'a', 't'], 'd'), "Expected: False"


def remove_x(my_string):
    if my_string == "":
        return ""
    else:
        if my_string[0] == 'x':
            return remove_x(my_string[1:])
        else:
            return my_string[0] + remove_x(my_string[1:])


print remove_x('catxxxdog')
print "Computed:", "\"" + remove_x("") + "\"", "Expected: \"\""
print "Computed:", "\"" + remove_x("cat") + "\"", "Expected: \"cat\""
print "Computed:", "\"" + remove_x("xxx") + "\"", "Expected: \"\""
print "Computed:", "\"" + remove_x("dxoxg") + "\"", "Expected: \"dog\""\



def insert_x(my_string):
    if len(my_string) <= 1:
        return my_string
    else:
        return my_string[0] + 'x' + insert_x(my_string[1:])


print "Computed:", "\"" + insert_x("") + "\"", "Expected: \"\""
print "Computed:", "\"" + insert_x("c") + "\"", "Expected: \"c\""
print "Computed:", "\"" + insert_x("pig") + "\"", "Expected: \"pxixg\""
print "Computed:", "\"" + insert_x("catdog") + "\"", "Expected: \"cxaxtxdxoxg\""


def list_reverse(my_list):
    if len(my_list) <= 1:
        return my_list
    else:
        return [my_list[-1]] + list_reverse(my_list[:-1])


print list_reverse([1, 2, 3, 4, 5])
print "Computed:", list_reverse([]), "Expected: []"
print "Computed:", list_reverse([1]), "Expected: [1]"
print "Computed:", list_reverse([1, 2, 3]), "Expected: [3, 2, 1]"
print "Computed:", list_reverse([2, 3, 1]), "Expected: [1, 3, 2]"
