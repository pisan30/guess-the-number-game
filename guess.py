import random

# 判定ロジック定義
def main():
    # ランダムな数を定義　1−100
    correct_number = random.randint(1, 100)
    # print("正解は" + str(correct_number))

    guessing_count = 0
    while True:

        # ユーザ入力を受け付け
        try:
            guess_number = int(input("1から100の間で数値を入力してください："))
        except ValueError:
            print("数字を入力してください")
            continue

        # バリデーション
        if not 0 <= guess_number <= 100:
            print("1から100の範囲外です。")
            continue

        # 回答回数をカウント
        guessing_count += 1

        if correct_number == guess_number:
            print("正解です！　" + str(guessing_count) + "　回目で正解しました！")
            break
        else:
            print("不正解です")
            if correct_number > guess_number:
                print("正解は　" + str(guess_number) + " より大きいです")
            else:
                print("正解は　" + str(guess_number) + " より小さいです")
    
    return


if __name__ == "__main__":
    main()