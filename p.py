#while loop比較適合用在不知道會執行幾次的事情上面
#讀取檔案
products = []#拿來放商品的清單

with open('products.csv','r',encoding='utf-8') as p:#把檔案以utf-8格式開啟並讀取
    for line in p:#一個line是一行
        if '商品,價格' in line:#如果在line裡面有商品跟價格的話
            continue#那會直接跳過本次迴圈
            #在本例中，他會直接掉到下個迴圈
#        s = line.strip().split(',')#先利用strip去掉\n，再利用split，來用,去做切割
#        name = s[0]# 把小清單的第一個加入name
#        price = s[1]# 把小清單的第二項加入price
        name, price = line.strip().split(',')#分別使用name跟price把它存進去，上三行的簡寫
        products.append([name, price])#把這兩個小清單給加入products裡面

print(products)

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

# print(products)

for p in products:#把products加入p
#    print(p)#把清單內容逐條print出來
    print(p[0], '的價格是', p[1])

# 可以透過products[0][0]來找到特定的資料#第一個[0]是大清單的第0格，第二個[0]是小清單中的第0格

#with open('products.txt', 'w') as f: #開啟檔案，寫入模式，如果沒有這個檔案的話，會生成一個 as、這個檔案會被稱作f
#	for p in products: #把這個檔案一個一個寫入
#		f.write(p[0] + ',' + p[1] + '\n')#在open的這個檔案write

with open('products.csv', 'w', encoding='utf-8') as f: #在寫入檔案時加入encoding='utf-8'來解決中文字會變成亂碼的問題
	f.write('商品,價格\n')#加上這行來讓表格有一個欄位名稱
	for p in products: #把這個檔案一個一個寫入
		f.write(p[0] + ',' + p[1] + '\n')#csv的區隔是,

#在python中，如果是with下的話，他會自動把檔案關閉
#其他的程式語言還會需要把檔案close掉







