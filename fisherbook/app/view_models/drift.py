"""
Created by 张 on 2019/7/14
"""
from app.libs.enums import PendingStatus

__author__ = '张'


class DriftCollection:
    def __init__(self, drifts, current_user_id):
        self.data = []
        self.__parse(drifts, current_user_id)

    def __parse(self, drifts, current_user_id):
        for drift in drifts:
            temp = DriftViewModel(drift, current_user_id)
            self.data.append(temp.data)




class DriftViewModel:
    def __init__(self, drift, current_user_id):
        self.data = []
        self.data = self.__parse(drift, current_user_id)

    @staticmethod
    def request_or_gifter(drift, current_user_id):
        if drift.requester_id == current_user_id:
            you_are = 'requester'
        else:
            you_are = 'gifter'
        return you_are

    def __parse(self, drift, current_user_id):
        you_are = self.request_or_gifter(drift, current_user_id)
        pending_status = PendingStatus.pending(drift.pending, you_are)

        r = {
            'you_are': you_are,
            'drift_id': drift.id,
            'book_title': drift.book_title,
            'book_author': drift.book_author,
            'book_img': drift.book_img,
            'date': drift.create_datetime.strftime('%m/%d/%Y'),
            'operator': drift.gifter_name if you_are == 'requester' else drift.requester_name,
            'message': drift.message,
            'address': drift.address,
            'status_str': pending_status,
            'recipient_name': drift.recipient_name,
            'mobile': drift.mobile,
            'status': drift.pending
        }

        return r
