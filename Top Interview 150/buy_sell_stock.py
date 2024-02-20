class Solution:
    def buy_sell_stock(self,prices):
        print(f"Prices are : {prices}")
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit , price - min_price)

            print(f"Current Price: {price} Min Price : {min_price} , Max Profit : {max_profit}")

        return max_profit

obj = Solution()
prices = [7,6,4,3,1]
print(f"Profit will be {obj.buy_sell_stock(prices)}")