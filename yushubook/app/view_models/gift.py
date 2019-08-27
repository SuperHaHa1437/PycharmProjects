"""
Created by 张 on 2019/8/27 
"""
from app.view_models.book import BookViewModel

__author__ = '张'


# 对原始数据进行加工
class MyGifts:
    def __init__(self, gift_of_mine, wish_count_list):
        self.gifts = []

        self.__gifts_of_mine = gift_of_mine
        self.__wish_count_list = wish_count_list
        self.gifts = self.__parse()

    def __parse(self):
        """
        1.从gift_of_mine中获取到所有的gift模型
        2.遍历 gift,即每一个可赠送的书籍
        3.遍历 wish_count_list,匹配gift.isbn 与wish_count_list的 isbn
        4.匹配成功即将相关数据赋给字典r
        :return:
        """
        temp_gifts = []
        for gift in self.__gifts_of_mine:
            my_gift = self.__matching(gift)
            temp_gifts.append(my_gift)
        return temp_gifts

    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        r = {
            'wishes_count': count,
            # 拿到书籍详细信息再通过BookViewModel加工
            'book': BookViewModel(gift.book),
            'id': gift.id
        }
        return r
