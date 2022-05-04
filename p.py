#while loop比較適合用在不知道會執行幾次的事情上面

products = []#拿來放商品的清單

while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
    	break
    price = input('請輸入商品價格：')
    p = []#建立一個小清單
    p.append(name)#在清單內放入名稱
    p.append(price)#在清單內放入價格
    products.append(p)#把小清單放入大清單
print(products)