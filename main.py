# 第一题
def word_count(str):
    str_split = str.split(' ')
    mark_point_list = ['?', '!', '.', ',']
    word_obj = {}
    word_arr = []
    for i in str_split:
        str = ''
        for j in i:
            in_list = j in mark_point_list
            if in_list == False:
                str = str + j
        word_obj[str.lower()] = 0
        word_arr.append(str.lower())

    for i in word_arr:
        word_obj[i] = word_obj[i] + 1

    print(word_obj)
    return word_obj


word_count(str='Hello world! Hello Python.')


# 第二题

item_list = {}


def item_input(run=True):
    if run == False:
        return
    print('请输入操作类型', 'add添加商品', 'query查询商品列表', 'delete删除商品', 'q退出程序')
    action_type = input()
    while (True):
        if action_type == 'add':
            print('请输入商品名称')
            item_name = input()
            in_list = item_name in item_list
            if in_list == False:
                item_list[item_name] = 0
            print('请输入商品数量')
            item_count = input()
            item_list[item_name] = item_list[item_name] + int(item_count)
            break

        if action_type == 'delete':
            print('请输入要删除的商品名称')
            item_name = input()
            del item_list[item_name]
            break

        if action_type == 'query':
            print('当前商品列表', item_list)
            break

        if action_type == 'q':
            print('退出程序')
            item_input(run=False)
            return

    item_input()


def input_time(value):
    format = value.split('/')
    if (len(format) != 3):
        print('输入日期格式有误')
        return
    day = format[0]
    month = format[1]
    year = format[2]

    if day.isdigit() == False or int(day) >= 32:
        print('输入的日期有误')
        return

    if month.isdigit() == True and (int(month) == 2 and int(day) > 28):
        print('2 月不能超过 28 天')
        return

    if month.isdigit() == False or int(month) >= 13:
        print('输入的月份有误')
        return
    if year.isdigit() == False or int(year) < 1000 or int(year) > 9999:
        print('输入的年份有误')
        return


# input_time('25/12/2023')
