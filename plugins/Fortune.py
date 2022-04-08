import random


class Fortune:
    # ---------------------------------------------------
    # 占い
    # ---------------------------------------------------
    #
    def get_fortune_message(self):
        list = ([f"今日の運勢は～？", f"（ｼﾞｬｶｼﾞｬｶｼﾞｬｶ…）"])
        # 抽選
        fortune_id = random.choice(["大吉", "吉", "中吉", "小吉", "凶"])

        if fortune_id == "大吉":
            list.append(f"大吉！")
            list.append(f"今日はいい一日だ！")

        elif fortune_id == "吉":
            list.append(f"吉！")
            list.append(f"何かいいことあるかもね！")

        elif fortune_id == "中吉":
            list.append(f"中吉！")
            list.append(f"今日も一日頑張ろ～！")

        elif fortune_id == "小吉":
            list.append(f"小吉！")
            list.append(f"ちょっといいことあるかもよ！")

        elif fortune_id == "末吉":
            list.append(f"末吉！")
            list.append(f"ささやかな幸せがありますように！")

        elif fortune_id == "凶":
            list.append(f"凶！")
            list.append(f"今日は今日の風が吹く！")
            list.append(f"…なんつってね！")

        return list
