from pydub import AudioSegment
import matplotlib.pyplot as plt
from mutagen.easyid3 import EasyID3

class Main:

    def __init__(self, switch):

        self.switch = switch

    def main(self):

        if self.switch == 0:

            """https://qiita.com/itoru257/items/8af2902d8ce851ae74ea"""
            """https://qiita.com/nyancook/items/786cffd0b07bad8b4444"""
            self.sound = AudioSegment.from_file("MindlessFate - Sky Punch.mp3", "mp3")
            self.channel_count = self.sound.channels  # チャンネル数(1:mono, 2:stereo) https://algorithm.joho.info/programming/python/pydub-time-sampling-rate-channel/
            self.frame_per_second = self.sound.frame_rate  # FPS
            self.duration = self.sound.duration_seconds  # 再生時間
            self.samples = self.sound.get_array_of_samples()
            print(self.channel_count, self.frame_per_second, self.duration)

            plt.plot(self.samples)
            plt.show()

            self.sound.export("./result.mp3", format="mp3")  # 保存

        if self.switch == 1:

            self.tags_before = EasyID3('MindlessFate - Sky Punch.mp3')

            self.dict_keys = EasyID3.valid_keys.keys()  # 編集可能なタグのリスト出力
            self.dict_values_before = EasyID3.valid_keys.values()  # タグのリスト出力，編集前
            print(self.dict_keys)
            print(self.dict_values_before)

            self.tags_before['title'] = 'Sky Punch'
            self.tags_before.save()

            self.tags_after = EasyID3('MindlessFate - Sky Punch.mp3')
            self.dict_values_after = EasyID3.valid_keys.values()  # タグのリスト出力，編集後
            print(self.dict_values_after)



if __name__ == '__main__':

    main = Main(1)
    main.main()
    tags_before = main.tags_before
    tags_after = main.tags_after
