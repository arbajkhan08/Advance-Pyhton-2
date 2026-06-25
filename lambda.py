
# # # map example 
# l= [ 1,2,3,4,5,]

# # square = lambda x : x*x
# # sqList = map(square, l)
# # print(list(sqList))


# # filter  Example
# def even(n):
#     if (n%2 == 0):
#         return True
#     return False


# onlyEven = filter(even, l)
# print(list(onlyEven))



name = input("enter yourt name")
marks = int(input("enter your marks"))
phone = int(input("enter your phopne:"))

s = " the name of the student is {}, his marks are{}, and phone number is{}".format(name,marks,phone)


print(s)