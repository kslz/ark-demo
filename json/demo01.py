import json


def main():
    historyTransactions = [
        {
            'time': '20170101070311',  # 交易时间
            'amount': '3088',  # 交易金额
            'productid': '45454455555',  # 货号
            'productname': 'iphone7'  # 货名
        },
        {
            'time': '20170101050311',  # 交易时间
            'amount': '18',  # 交易金额
            'productid': '453455772955',  # 货号
            'productname': '奥妙洗衣液'  # 货名
        }
    ]

    # dumps 方法将数据对象序列化为 json格式的字符串
    jsonstr = json.dumps(historyTransactions,ensure_ascii=False,indent=4)
    # print(jsonstr)
    w_file('.\data\info1.json',jsonstr,'w')
    text = r_file('.\data\info1.json')
    print(f'text={text}')
    text =json.loads(text)
    print(f'text={text}')


def r_file(path):
    with open(path, 'r') as f:
        return f.read()


def w_file(path, text, mode):
    """
    用于向文件中写入

    :param path: 文件路径
    :param text: 要写入的数据
    :param mode: 写入模式 a为追加 w为覆写

    """
    with open(path, mode) as f:
        f.write(text)


if __name__ == '__main__':
    main()
