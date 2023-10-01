prompt_1 = "Please enter the board size\n"
prompt_2 = "Please enter how many squares you want to place\n"
prompt_3 = "Please enter the coordinates of a square you want to place\n"
prompt_4 = "Please enter a target square coordinate, or enter exit to exit\n"
prompt_5 = "Congratulations, you won!"
prompt_6 = "Thanks for playing."
error_message_1 = "Improper board size"
error_message_2 = "Improper amount of squares"
error_message_3 = "Incorrect input format for square coordinates"
error_message_4 = "Improper square coordinates"
error_message_5 = "Sign already placed to square"

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
# taking coordinates function
def take_coo(message):
    co_list = []
    while True:
        coordinates = input(message)
        coordinates = coordinates.replace(" ", "")
        if not ((coordinates[0].isnumeric()) and (coordinates[1].isnumeric())):
            print(error_message_3)
            continue
        elif (len(coordinates) > 3) and (coordinates[2] == ".") and (coordinates[3].isnumeric()):
            print(error_message_3)
            continue
        elif not ((int(coordinates[0]) and int(coordinates[1]))>0 and (int(coordinates[0]) and int(coordinates[1])) < (board_size + 1)):
            print(error_message_4)
            continue
        else:
            co_list.append(int(coordinates[0]))
            co_list.append(int(coordinates[1]))
            break
    return co_list
#end of taking coo func

def target_coo(message):
    target_list = []
    while True:
        coordinates = input(message)
        exitornot = coordinates.lower()
        if exitornot == "exit":
            return "exit"
            break
        else:
            coordinates = coordinates.replace(" ", "")
            if not ((coordinates[0].isnumeric()) and (coordinates[1].isnumeric())):
                print(error_message_3)
                continue
            elif (len(coordinates) > 3) and (coordinates[2] == ".") and (coordinates[3].isnumeric()):
                print(error_message_3)
                continue
            elif not ((int(coordinates[0]) and int(coordinates[1]))>0 and (int(coordinates[0]) and int(coordinates[1])) < (board_size + 1)):
                print(error_message_4)
                continue
            else:
                target_list.append(int(coordinates[0]))
                target_list.append(int(coordinates[1]))
                break
    return target_list

# function of printing lists
def print_funcs(lists):
    for i in lists:
        for j in i:
            print(j, end="")
        print()
ex = True
while ex:
    # block of taking board size
    x = True
    while x:
        board_size = int(input(prompt_1))
        if board_size < 5 or board_size > 9:
            print(error_message_1)
            continue
        else:
            break
        # end of the block


    # block of taking number of square
    x = True
    while x:
        num_of_square = int(input(prompt_2))
        if num_of_square < 1 or num_of_square > board_size ** 2:
            print(error_message_2)
            continue
        else:
            break
    # end of the block

    # creating initial board
    board = []
    for i in range(board_size+1):
        board.append([])
    board[0].append(" ")
    for i in range(board_size):
        board[0].append(" ")
        board[0].append(i+1)
    for i in range(board_size):
        board[i+1].append(i+1)
        for j in range(board_size):
            board[i+1].append(" ")
            board[i+1].append("-")
    clearboard = []
    for i in range(board_size+1):
        clearboard.append([])
    clearboard[0].append(" ")
    for i in range(board_size):
        clearboard[0].append(" ")
        clearboard[0].append(i+1)
    for i in range(board_size):
        clearboard[i+1].append(i+1)
        for j in range(board_size):
            clearboard[i+1].append(" ")
            clearboard[i+1].append("-")
    # end of the block

    # + squares coordinates
    used_squares = []
    y = 0
    while y != num_of_square:
        j, k = take_coo(prompt_3)
        if [j, k] not in used_squares:
            used_squares.append([j, k])
            board[j][2 * k] = "+"
            print_funcs(board)
            y += 1
        else:
            print(error_message_5)
            continue
    # end of the block

    # change available coo

    z = True
    while z:
        a = target_coo(prompt_4)
        if not a == "exit":
            target1 = []
            target2 = []
            target3 = []
            target4 = []
            target5 = []
            l, m = a
            target1.append(l - 1)
            target1.append(m - 1)
            target2.append(l - 1)
            target2.append(m + 1)
            target3.append(l + 1)
            target3.append(m-1)
            target4.append(l + 1)
            target4.append(m + 1)
            target5.append(l)
            target5.append(m)

            if  (target1[0] > 0) and (target1[1] > 0) and (target1[0] < board_size+1) and (target1[1] < board_size+1):
                if board[target1[0]][(target1[1]*2)] == "+":
                    board[target1[0]][(target1[1] * 2)] = "-"
                else:
                    board[target1[0]][(target1[1] * 2)] = "+"
            else: pass
            if  (target2[0] > 0) and (target2[1] > 0) and (target2[0] < board_size+1) and (target2[1] < board_size+1):
                if board[target2[0]][(target2[1]*2)] == "+":
                    board[target2[0]][(target2[1] * 2)] = "-"
                else:
                    board[target2[0]][(target2[1] * 2)] = "+"
            else: pass
            if  (target3[0] > 0) and (target3[1] > 0) and (target3[0] < board_size+1) and (target3[1] < board_size+1):
                if board[target3[0]][(target3[1]*2)] == "+":
                    board[target3[0]][(target3[1] * 2)] = "-"
                else:
                    board[target3[0]][(target3[1] * 2)] = "+"
            else: pass
            if  (target4[0] > 0) and (target4[1] > 0) and (target4[0] < board_size+1) and (target4[1] < board_size+1):
                if board[target4[0]][(target4[1]*2)] == "+":
                    board[target4[0]][(target4[1] * 2)] = "-"
                else:
                    board[target4[0]][(target4[1] * 2)] = "+"
            else: pass
            if  (target5[0] > 0) and (target5[1] > 0) and (target5[0] < board_size+1) and (target5[1] < board_size+1):
                if board[target5[0]][(target5[1]*2)] == "+":
                    board[target5[0]][(target5[1] * 2)] = "-"
                else:
                    board[target5[0]][(target5[1] * 2)] = "+"
            else: pass
            print_funcs(board)
            if board == clearboard:
                print(prompt_5)
                print(prompt_6)
                finish = True
                break
        else:
            print(prompt_6)
            finish = True
            break
    if finish:
        break

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
