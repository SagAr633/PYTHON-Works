# def eligibility(func):
#     def wrapper(a,b):
#         if b>=18:
#             return func(a,b)
#         else:
#             raise Exception('Not eligible')
#     return wrapper
# @eligibility
# def vac(name,age):
#     return 'You are eligible for vaccination'
# print(vac('anu',16))



def exam(fn):
    def wrapper(a,b):
        if a>=50:
            return fn(a,b)
        else:
            raise Exception('You are failed')
    return wrapper
@exam
def score(mark,total_mark):
    return 'your are pass'
print(score(66,100))

