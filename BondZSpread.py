import numpy as np
from scipy.optimize import root

def getCashflowZspread(zspread, zero_rates_regular, cashflows, maturities):
    cashflows_each_period = cashflows / (1 + zero_rates_regular + zspread) ** maturities
    res = np.sum(cashflows_each_period)
    return res

def calcZSpreadFromZeroes(zero_rates, face_value, cashflows, maturities):
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root.html
    # scipy.optimize.root(fun, x0, args=(), method='hybr', jac=None, tol=None, callback=None, options=None)[source]
    
    # Input Scaling:
    zero_rates = zero_rates / 100
    face_value = face_value / 100
    cashflows = cashflows / 100

    # Objective function for root optimizer
    objective_function = lambda x: getCashflowZspread(x, zero_rates, cashflows, maturities) - face_value
    x0 = [0.01]
    
    # Run root optimization
    root_solution = root(objective_function, x0)
    z_spread = root_solution.x[0]
    
    # Scale result back up
    z_spread *= 100 
    return z_spread

def main():
    # par_rates = np.array([1.00, 1.50, 1.80, 2.05, 2.20])
    zero_rates = np.array([1.0, 1.5038, 1.8085, 2.0652, 2.2199])
    coupon_payments = np.array([3.0, 3.0, 3.0, 3.0, 103.0])
    maturities = np.array([1, 2, 3, 4, 5])
    face_value = 100
    zspread = calcZSpreadFromZeroes(zero_rates, face_value, coupon_payments, maturities)
    return zspread

if __name__ == "__main__":
    res = main()
    print("Z Spread Calculation = ", res)
