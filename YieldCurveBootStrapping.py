import QuantLib as ql

def print_curve(xlist, ylist, precision=3):
    """
    Method to print curve in a nice format
    """
    print ("----------------------")
    print ("Maturities\tCurve")
    print ("----------------------")
    for x,y in zip(xlist, ylist):
        print (x,"\t\t", round(y, precision))
    print ("----------------------")


# Deposit Rates:
depo_maturities = [ql.Period(6, ql.Months),
				   ql.Period(12, ql.Months)]

depo_rates = [5.25,
 			  5.5]


# Bond Rates: 
bond_maturities = [ql.Period(6*i, ql.Months) for i in range(3, 21)]

bond_rates = [5.75, 
			  6.0, 
			  6.25, 
			  6.5, 
			  6.75,
			  6.80, 
			  7.00, 
			  7.1, 
			  7.15,
              7.2, 
              7.3, 
              7.35, 
              7.4, 
              7.5, 
              7.6, 
              7.6, 
              7.7, 
              7.8]


print_curve(depo_maturities, depo_rates)
print_curve(bond_maturities, bond_rates)

calc_date = ql.Date(15, 1, 2015)
ql.Settings.instance().evaluationDate = calc_date

calendar = ql.UnitedStates()

business_convention = ql.Unadjusted
day_count = ql.Thirty360()

end_of_month = True

settlement_days = 0

face_amount = 100

coupon_frequency = ql.Period(ql.Semiannual)
settlement_days = 0

depo_helpers = [ql.DepositRateHelper(ql.QuoteHandle(ql.SimpleQuote(r/100.0)),
					 				 m,
					 				 settlement_days,
					 				 calendar,
									 business_convention,
									 end_of_month,
									 day_count)
				for r, m in zip(depo_rates, depo_maturities)]


