#while loop比較適合用在不知道會執行幾次的事情上面

products = []#拿來放商品的清單

while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
    	break
    price = input('請輸入商品價格：')
#    p = []#建立一個小清單
#    p.append(name)#在清單內放入名稱
#    p.append(price)#在清單內放入價格
#    products.append(p)#把小清單放入大清單

#    p = [name, price]#也可以把上面三行縮到清單裡面
#    products.append(p)#把小清單放入大清單

    products.append([name, price])

print(products)

for p in products:#把products加入p
    print(p)#把清單內容逐條print出來
    print(p[0], '的價格是', p[1])

# 可以透過products[0][0]來找到特定的資料#第一個[0]是大清單的第0格，第二個[0]是小清單中的第0格

with open('products.txt', 'w') as f: #開啟檔案，寫入模式，如果沒有這個檔案的話，會生成一個 as、這個檔案會被稱作f
	for p in products: #把這個檔案一個一個寫入
		f.write(p[0] + ',' + p[1] + '\n')#在open的這個檔案write

with open('products.csv', 'w') as f: #csv是比較常見的儲存格式
	for p in products: #把這個檔案一個一個寫入
		f.write(p[0] + ',' + p[1] + '\n')#在open的這個檔案write








