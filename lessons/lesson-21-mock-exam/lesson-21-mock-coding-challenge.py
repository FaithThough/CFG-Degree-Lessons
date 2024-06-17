def can_afford(coin_collection, item_price):
    total_value = 0
    for coin, count in coin_collection.items():
        total_value += coin * count

    if total_value >= item_price:
        change_required = total_value - item_price
        coins_to_return = {}

        for coin in sorted(coin_collection.keys(), reverse=True):
            if change_required >= coin:
                num_coins = change_required // coin
                num_coins = min(num_coins, coin_collection[coin])
                coins_to_return[coin] = num_coins
                change_required -= num_coins * coin

        return coins_to_return
    else:
        print(f"Can't afford this with the available petty change")
        return {}

coin_collection = {
    2.00: 2,
    1.00: 6,
    0.50: 10,
    0.20: 4,
    0.10: 6,
    0.05: 7,
    0.02: 4,
    0.01: 6
}

item_price = float(input('What is the price of the item? '))
coins_to_return = can_afford(coin_collection, item_price)

if coins_to_return:
    print(f"You can afford the item. Use the following coins:")
    for coin, count in coins_to_return.items():
        print(f"£{coin:.2f}: {count}")