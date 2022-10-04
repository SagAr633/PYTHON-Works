lst=[
    [10,30],
    [23,27],
    [3,33],[4,44],
    [1,55]
]
# flat_list=[n for i in lst for n in i]
flat_list=[n for sub_list in lst for n in sub_list]
#print all number>25
gt_25=list(filter(lambda l:l>25,flat_list))
print(gt_25)
#print square of all numbers
sqr=list(map)