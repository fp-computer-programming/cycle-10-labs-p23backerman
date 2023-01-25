
#gives function add_foods
def add_foods(x):
    #sets the lists to equal nothing but forced into list format
    sixth_letter = []
    short_foods = []
    not_foods = [] 
    #it will check the 6th letter of each value in the list and will add that letter to the end of the sixt_letter list
    for index in x:  
        try:  
            c = index[5]
            sixth_letter.append(c)
            #if it gives an index error, that means the value is too short and does not have a sixth letter. so it adds that string to the end of the list "short_foods"
        except IndexError: 
            short_foods.append(index)
            #if it gives a Type error, it is not a string and will add it the list "not_foods"
        except TypeError:
            not_foods.append(index)


    #prints each list with the name of the list followed by a colon and the list
    print(("sixth_letter : {0}, not_foods : {1}, short_foods {2}").format(sixth_letter, not_foods, short_foods))


print (add_foods(['potatoes', 'salsa', 'cherries', 'banana', 'apple']))
print (add_foods(['naan', 'celery', 'buckwheat', 7, 'clementine']))
print (add_foods(['Cheeseburger', True, 'chicken', 'rice', 'radish']))
