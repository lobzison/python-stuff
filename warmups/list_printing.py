def list_printing():
    """Doing some modification on nested lists and printing them"""
    my_list = [[0 for i in range(5)] for j in range(5)]
    my_list2 = [[0 for i in range(5)] for j in range(5)]
    
    for i in range(5):
        for j in range(5):
            if j == 1 and i > 0 and i < 4:
                my_list[i][j] = 1
                
    for i in range(5):
        for j in range(5):
            if (j == 3 or j == 1) and i > 0 and i < 4:
                my_list2[i][j] = 1
                
    for k in range(5):
        print(str(my_list[k]) + ' | ' + str(my_list2[k]))
	
    print('-'*33)
             
    for i in range(5):
        for j in range(5):
            if i == 3 and j > 1:
                my_list[i][j] = 1
                
    for k in range(5):
        print(str(my_list2[k]) + ' | ' + str(my_list[k]))
        
list_printing()
