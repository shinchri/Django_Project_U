# unpacking list
date, name, price = ['December 23, 2015', 'Bread Gloves', 8.51]

def drop_first_and_last(grades):
    first, *middle, last = grades
    ave = sum(middle)/ len(middle)
    print(ave)

drop_first_and_last([65, 76, 97, 56, 21])