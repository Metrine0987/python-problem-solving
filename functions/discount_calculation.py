def calculate_discount(price):
    if price >= 1000:
        return price * 0.20
    elif price >= 500:
        return price * 0.10


    return price


final_price = 1200 - calculate_discount(1200)


print(final_price)
