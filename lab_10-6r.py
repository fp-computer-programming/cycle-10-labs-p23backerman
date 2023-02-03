#function add nums is given with a list requiored
def add_nums(list):
    #asks the user for a number
    print("Give a number")
    pause = []
    a = input()
    #if there is no value error, it will add the user input to every value in the list
    try:
        inp = int(a)
        for b in list:
            b += inp
            pause.append(b)
        print(pause)
        return ("passed list: {0}; user input: {1}".format(list, inp))
        #if there is a value error, it will print the following and ask to do it again
    except ValueError:
        print("Not a number, please try again")
    
    
#test cases
print(add_nums([1, 7, 9, 12]))
print(add_nums([1, 2, 5, 7, 9]))
print(add_nums([1, 43, 54, 54]))