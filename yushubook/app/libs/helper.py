"""
Created by 张 on 2019/7/31 
"""
__author__ = '张'



def is_isbn_or_key(word):
    """
    判断搜索字段是 isbn  还是关键字搜索
    :param word: 搜索的关键字
    :return:
    """
    isbn_or_key = 'key'

    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'

    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key
