current_price=int(input())

last_months_price=int(input())

monthly_mortgage= (current_price * 0.051) / 12

price_change=int(current_price - last_months_price)

print(f'This house is ${current_price}. The change is ${price_change} since last month.')

print(f'The estimated monthly mortgage is ${monthly_mortgage:.2f}.')

   