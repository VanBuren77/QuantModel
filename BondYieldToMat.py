import math


def calc_pv(face, annual_cashflow, num_periods, rate):

    running_pv = 0

    for period in range(num_periods):
        # increment running present value by the annual cashflow divided by (1 + r) ^ n, where n = period, r = rate
        running_pv += annual_cashflow / math.pow((1 + rate), period)

    # Last Cashflow
    running_pv += face / math.pow((1 + rate), num_periods)

    return running_pv


def main(price, rate, face, maturity, semi):

    rate_pct = rate / 100 # get rate as a pct
    cashflow = face * rate_pct # annual or semi-annual cashflow
    factor = 1

    if semi:
        factor = 2

    ytm = rate_pct # init yield to mat at rate pct
    
    converged = False

    while not converged:
        # if discount bond 
        if price < face:
            ytm += 0.00001
        # if premium or priced at par
        else:
            ytm -= 0.00001

        pv = calc_pv(face, cashflow / factor, maturity * factor, ytm / factor)

        # If discounted bond
        if price < face:
            # converge to price from top down
            converged = pv < price

        # If premium / par bond
        else:
            # converge to price from bottom up
            converged = pv > price # we have not converged if the 
    
    print("Found YTM at:", round(ytm * 100, 5) , "%")

if __name__ == "__main__":
    price = 100         # priced at par
    price = 104.5       # priced at premium
    price = 98.3        # priced at discount
    rate = 2.5          # 2.5% coupon rate
    face = 100          # original face value of bond
    maturity = 30       # number of years remaning until maturity 
    semi = False        # semi-annual bond or not

    main(price, rate, face, maturity, semi)
