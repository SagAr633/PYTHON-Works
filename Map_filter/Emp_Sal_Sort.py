employees=[
    [10001,"ram","qa",25000,2],
    [10002, "ravi", "ba", 24000, 2],
    [10006, "arjun", "devop", 25000, 2],
    [10003, "jeevan", "qa", 27000, 3],
    [10004, "jhon", "sales", 28000, 3],
    [10005, "tinu", "mrkt", 25000, 1]
]
#sort by salary
employees.sort(key=lambda em:em[3])
print(employees)

#sort by employee's experience
employees.sort(reverse=True,key=lambda e:e[-1])
print(employees)

#highest paid employee
employees.sort(reverse=True,key=lambda emp:emp[-2])
print(employees[0])
highest_paid=max(employees,key=lambda e:e[-2])
print(highest_paid)

#lowest_paid employee
lowest_paid=min(employees,key=lambda e:e[-2])
print(lowest_paid)

#find total sum of salaries of all employees
salaries=list(map(lambda e:e[-2],employees))
total=sum(salaries)
print(total)
total_sum=sum(list(map(lambda e:e[-2],employees)))
print(total_sum)
#list comprahension
sal=[i[-2] for i in employees]
ts=sum(sal)
print(ts)