employees=[
    [10001,"ram","qa",25000,2],
    [10002, "ravi", "ba", 24000, 2],
    [10006, "arjun", "devop", 25000, 2],
    [10003, "jeevan", "qa", 27000, 3],
    [10004, "jhon", "sales", 28000, 3],
    [10005, "tinu", "mrkt", 25000, 1]
]
upcase=map(lambda name:name[1].upper(),employees)
print(list(upcase))

salary=map(lambda sal:sal[3]>25000,employees)
print(list(salary))

#salary higher than 25k with filter function

sal=filter(lambda s:s[3]>25000,employees)
print(list(sal))

#print employee details whose salary in range of 23k to 26k

# salrange=filter(lambda sr:sr[3]>=23000 and sr[3]<=26000,employees)
salrange=filter(lambda sr:sr[3] in range(23000,26001),employees)
print(list(salrange))

