from typing import List

from test_framework import generic_test

# [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_price = float('inf')
    max_profit = 0.0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            continue
        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
