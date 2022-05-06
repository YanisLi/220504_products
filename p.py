#while loop比較適合用在不知道會執行幾次的事情上面
#理想的function應該「只做一件事」
#所以refactor（重構程式）的核心概念，就是把程式碼不斷地改寫
#寫成越來越小的function
#讓function盡量只做一件事
#程式最好有main() function為程式的接入點

import os #operation system，載入系統

def read_file(filename):
    #讀取檔案
    #要來檢查檔案在不在電腦裡面
    products = []#拿來放商品的清單
    with open(filename, 'r', encoding='utf-8') as p:#把檔案以utf-8格式開啟並讀取
            for line in p:#一個line是一行
                if '商品,價格' in line:
                    continue
                name, price = line.strip().split(',')#分別使用name跟price把它存進去，上三行的簡寫
                products.append([name, price])#把這兩個小清單給加入products裡面
    #把清單內容給導入出來
    return products
def user_input(products):
    while True:
        name = input('請輸入商品名稱：')
        if name == 'q':
            print('結束新增')
            break
        price = input('請輸入商品價格：')
    #    p = []#建立一個小清單
    #    p.append(name)#在清單內放入名稱
    #    p.append(price)#在清單內放入價格
    #    products.append(p)#把小清單放入大清單

    #    p = [name, price]#也可以把上面三行縮到清單裡面
    #    products.append(p)#把小清單放入大清單

        products.append([name, price])
    return products
def print_products(products):
    count = 1
    for p in products:#把products加入p.
    #    print(p)#把清單內容逐條print出來
        print(count ,'->',p[0], '的價格是', p[1])
        count = count + 1
    # 可以透過products[0][0]來找到特定的資料#第一個[0]是大清單的第0格，第二個[0]是小清單中的第0格
    #with open('products.txt', 'w') as f: #開啟檔案，寫入模式，如果沒有這個檔案的話，會生成一個 as、這個檔案會被稱作f
    #	for p in products: #把這個檔案一個一個寫入
    #		f.write(p[0] + ',' + p[1] + '\n')#在open的這個檔案write
    if count == 1:
        print('無紀錄可供輸出')
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f: #在寫入檔案時加入encoding='utf-8'來解決中文字會變成亂碼的問題
    	f.write('商品,價格\n')#加上這行來讓表格有一個欄位名稱
    	for p in products: #把這個檔案一個一個寫入
    		f.write(p[0] + ',' + p[1] + '\n')
        #csv的區隔是,
        #在python中，如果是with下的話，他會自動把檔案關閉
        #其他的程式語言還會需要把檔案close掉

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):#確認這個檔案存不存在，現在為相對路徑，如不在這個資料夾中，則需要絕對路徑
            print('已找到檔案！')
            products = read_file(filename)
    else:
            print('找不到檔案Ｑ')

    products = user_input(products)

    ask_if_print = input('是否要輸出總表？ y/n    :')
    if ask_if_print == 'y':
        print_products(products)

    write_file(filename, products)

main()
