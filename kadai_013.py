def calculate_total(price, tax):

    total = price + price* tax/100

    print(f"{total}円")

calculate_total(1350, 10)
