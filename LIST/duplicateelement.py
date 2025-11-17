a=[70,10,50,30,60,40]
profit=0
for i in range(0,len(a)-1):
    buy_price=a[i] 
    for j in range(i+1,len(a)):
        sell_price=a[j]
        if sell_price-buy_price>profit:
            profit=sell_price-buy_price
print(profit)