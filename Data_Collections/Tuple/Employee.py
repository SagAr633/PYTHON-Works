employee=(
    ('anu',1,'dev',35000),
    ('amal',2,'tester',25000),
    ('arun',3,'dev',50000),
    ('akhil',4,'dev',52000)
)
for i in employee:
    if i[3]>=40000:
        print(i)
