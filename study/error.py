# 相除异常
# def div(a, b):
#     if b != 0:
#         return a / b
#     else:
#         print("分母不能为空")
#         return 0


# 捕获异常 3/21
list1 = [1, 2, 3]


# def div(a, b):
#     return a / b
#
#
# try:
#     print(div(1, 1))
#     print(list1[3])
# except ZeroDivisionError as e:
#     print(e)
#     print("这里有个异常")
# except IndexError as e1:
#     print(e1)

# 捕获父类异常
# def div(a, b):
#     return a / b
#
#
# try:
#     print(div(1, 0))
#     print(list1[3])
# except Exception as e:
#     print(e)
#     print("这里有个异常")

# finally
def div(a, b):
    return a / b


try:
    print(div(1, 0))
    print(list1[3])
except Exception as e:
    print(e)
    print("这里有个异常")

