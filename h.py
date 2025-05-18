import math


# 第一题
def calculate_area():
    print("请输入圆的半径")
    m = input()
    if m.isdigit() == True:
        trans_m = int(m)
        res = round(math.pi * (trans_m * trans_m), 2)
        return print("圆的面积是", res)
    print("请输入有效的数字！")


# 第二题
def calculate_fahrenheit():
    print("请输入摄氏温度")
    try:
        temperture_input = float(input())
        fahrenheit = temperture_input * 9 / 5 + 32
        print("华氏温度是", fahrenheit)
    except ValueError:
        print("请输入有效的数字！")


# 第三题
def shopping_list():
    arr = []
    arr_len = 0
    while arr_len <= 2:
        print(f"请输入商品{arr_len + 1}的名称")
        name = input()
        print(f"请输入商品{arr_len + 1}的价格")
        price = input()
        if price.isdigit() == False:
            price("请输入有效的数字!")
            return
        arr.append({"name": name, "price": price})
        arr_len = arr_len + 1

    print("购物清单:")
    total = 0
    for index in range(len(arr)):
        item = arr[index]
        name = item["name"]
        price = item["price"]
        total = total + int(price)
        print(f"{index + 1}.{name} - {price}元")
    print("总价", f"{total}元")
