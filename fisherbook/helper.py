"""
Created by 张 on 2019/3/19 
"""
__author__ = '张'

'''
判断搜索字段是 isbn  还是关键字搜索
'''
def is_isbn_or_key(word):
    isbn_or_key = 'key'

    # 判断isbn13
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'

    # 判断 isbn10
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key