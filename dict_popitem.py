fruit = {"apple":7,"orange":5,"peach":6}
while fruit :
    ans = input("フルーツを取り出しますか？（y/n）:")
    if ans == "y":
        key,value = fruit.popitem()
        print(f"{key}は{value}個")
    elif ans == "n":
        print("終了しました。")
        break
else :
    print("もう空っぽです。")