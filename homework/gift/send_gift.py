
"""
发礼物之后展示礼物
1、默认值have_gift 没有礼物
2、定义一个发礼物的方法
3、定义一个显摆礼物的方法
4、实现发完礼物之后，能展示礼物
"""
# have_gift = False
# def send_gift():
#     global have_gift
#     have_gift = True
#     print("发礼物啦")
#
# def show_gift():
#     if have_gift == True:
#         print("收到礼物啦，好开心")
#     else:
#         print("等等一会就轮到啦")
# print(__name__)
# # #python 执行入口
# # if __name__ == '__main__':  # 问题1
# #     send_gift()
#     show_gift()
from pythoncode.homework import gift


def send_gift():
    # global have_gift
    gift.have_gift = True
    print("发礼物啦")