from urllib.request import urlretrieve

'''
下载广论音频,每章节单数号则为音频 A 面,双数号则为音频 B 面
001A代表第一卷 A 面
002B代表第一卷 B 面
'''


class SpiderAudio():

    def __audio_list(self):
        audio_url_list = []
        for audio_num in range(1, 41):
            if audio_num % 2 == 0:
                audio_num = '00' + str(audio_num) + 'B' if audio_num < 10 else '0' + str(audio_num) + 'B'
                audio_url = 'http://www.theqi.com/buddhism/GL1/audio/' + audio_num + '.MP3'
                audio_info = {'audio_num': audio_num, 'audio_url': audio_url}
                audio_url_list.append(audio_info)
            else:
                audio_num = '00' + str(audio_num) + 'A' if audio_num < 10 else '0' + str(audio_num) + 'A'
                audio_url = 'http://www.theqi.com/buddhism/GL1/audio/' + audio_num + '.MP3'
                audio_info = {'audio_num': audio_num, 'audio_url': audio_url}
                audio_url_list.append(audio_info)

        return audio_url_list

    def __audio_download(self, audio_url_list):
        for audio_info in audio_url_list:
            # urlretrieve(audio_info.get('audio_url'),
            #             '/Users/superhaha/Downloads/菩提道次第广论/' + audio_info.get('audio_num') + '.mp3')
            print('下载广论语音文件:' + audio_info.get('audio_num'))
        print("下载完成")

    def go(self):
        audio_url_list = self.__audio_list()
        self.__audio_download(audio_url_list)


spider = SpiderAudio()
spider.go()
