def max_profit(prices):
    """
    Calculate the maximum profit that can be made from buying and selling 
    a stock at different days based on a list of stock prices.

    This function computes the maximum profit using a dynamic programming approach
    where it keeps track of the current maximum profit (`cur_max`) and the highest 
    profit encountered so far (`max_so_far`). It assumes that you can only make one 
    transaction (buy once and sell once).

    Parameters:
    prices (list): A list of integers representing the stock prices on different days.

    Returns:
    int: The maximum profit that can be achieved from the given stock prices. 
         Returns 0 if no profit is possible (i.e., prices are in descending order).

    Example:
    >>> max_profit([7, 1, 5, 3, 6, 4])
    5
    """
    cur_max, max_so_far = 0, 0
    for i in range(1, len(prices)):
        cur_max = max(0, cur_max + prices[i] - prices[i - 1])
        max_so_far = max(max_so_far, cur_max)

    return max_so_far


def buy_sell_stock(prices):
    """
    Find the maximum profit and the corresponding buy and sell prices 
    for a given list of stock prices. The function assumes that you can 
    only make one buy and one sell operation.

    This function calculates the profit between consecutive days, 
    identifies the maximum profit, and returns the buy price (the price 
    at which the stock should be bought) and sell price (the price at which 
    the stock should be sold to maximize profit).

    Parameters:
    prices (list): A list of integers representing the stock prices on different days.

    Returns:
    tuple: A tuple containing two values:
           - The maximum profit (int).
           - The price at which to buy the stock (int), and 
             the price at which to sell the stock (int).

    Example:
    >>> buy_sell_stock([7, 1, 5, 3, 6, 4])
    (4, 1, 5)
    """
    res = []
    for i in range(1, len(prices)):
        res.append(([prices[i] - prices[i - 1]], prices.index(prices[i])))

    max_profit = max(res)
    return max_profit[0][0], prices[max_profit[1] - 1], prices[max_profit[1]]
