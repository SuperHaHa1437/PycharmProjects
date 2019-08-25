"""
Created by 张 on 2019/8/25 
"""
__author__ = '张'


# 在 view_model 中处理这两个列表的原始数据，加工成需要的数据。
# 由于 gifts,wishs 两个的加工逻辑一样，只是数据库表不一样，所以可以写一个统一的类 trade 来处理
class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        """
        处理赠送or索要清单的数据集合
        :param goods: 数据集合
        """
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self, single):
        """
        处理单个数据
        :param single:单个赠送or索要清单的数据
        :return:
        """
        if single.create_datetime:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'

        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )
