def apply_discounts(products, stocks):
    for e in stocks:
        stock = float(stocks[e].replace('%', ''))

        if e in products:
            products[e] = round(products[e] - products[e] * stock/100, 2)
    return products


products = {
        "Oranges (packaged)": 114.99, 
        "Candy (Rotfront)": 280.00,
        "Boiled sausage": 199.99,
        "Juice J7 (orange)": 119.99,
        "Trout (Seven Seas)": 399.99
        }
stocks = {
        "Boiled sausage": "33%",
        "Juice J7 (orange)": "12%",
        "Trout (Seven Seas)": "18%"
    }
    
new_products = apply_discounts(products, stocks)
    
    
print(new_products)