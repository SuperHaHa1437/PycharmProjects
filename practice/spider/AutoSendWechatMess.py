import itchat

def after_login():
    user_info = itchat.search_friends(nickName='Wolverine')
    print(user_info)
    if len(user_info) > 0:
        # 拿到用户名
        user_name = user_info[0]['UserName']
        # 登陆账户发送
        # 发送文字信息
        itchat.send_msg('张小铀你好啊！', user_name)


# 接收到对方消息登陆账户回复
@itchat.msg_register(itchat.content.SHARING)
@itchat.msg_register(itchat.content.TEXT)
@itchat.msg_register(itchat.content.SYSTEM)
def reply_msg(msg):
    print(msg['Content'])
    itchat.send_msg(msg['Content'], msg['FromUserName'])


if __name__ == '__main__':
    itchat.auto_login(loginCallback=after_login, hotReload=True)
    itchat.run()
