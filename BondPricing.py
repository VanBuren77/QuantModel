import QuantLib as ql

# ================================
# Bond Modelling
# ================================
# Par = 100
# Coupon = 6%
# Payment Frequency = Semi-Annually
# Issue Date = January 15th, 2015
# Maturity Date = January 15, 2016
# ================================
# Spot Rates 
# ================================
# 6M =  0.005 
# 1Y = 0.007
# ================================

spot_rate_6m = 0.005
spot_rate_1y = 0.007

bond_payment_6m = 3 / (1 + spot_rate_6m) ** 0.5
bond_payment_1y = (100 + 3) / (1 + spot_rate_1y) ** 1

bond_price =  bond_payment_6m + bond_payment_1y

print(bond_price)

# ================================
# Bond Pricing Using Quant Lib
# ================================

# Build a Spot Curve Object:

todays_date = ql.Date(15, 1, 2015)
ql.Settings.instance().evaluationDate = todays_date

spot_dates = [ql.Date(15, 1, 2015), 
			  ql.Date(15, 7, 2015), 
			  ql.Date(15, 1, 2016)]

spot_rates = [0.0, 
			  0.005, 
			  0.007]

day_count = ql.Thirty360()

calendar = ql.UnitedStates()
interpolation = ql.Linear()

compounding = ql.Compounded
compounding_frequency = ql.Annual

spot_curve = ql.ZeroCurve(spot_dates,
						  spot_rates,
						  day_count,
						  calendar, 
						  interpolation,
						  compounding,
						  compounding_frequency)

spot_curve_handle = ql.YieldTermStructureHandle(spot_curve)


# Build a Bond Object:

issue_date = ql.Date(15, 1 , 2015)
maturity_date = ql.Date(15, 1, 2016)

tenor = ql.Period(ql.Semiannual)
calendar = ql.UnitedStates()

business_convention = ql.Unadjusted

date_generation = ql.DateGeneration.Backward
month_end = False

schedule = ql.Schedule(issue_date,
					   maturity_date, 
					   tenor,
					   calendar,
					   business_convention,
					   business_convention,
					   date_generation,
					   month_end)


day_count = ql.Thirty360()
coupon_rate = 0.06
coupons = [coupon_rate]

settlement_days = 0
face_value = 100

fixed_rate_bond = ql.FixedRateBond(settlement_days,
								   face_value,
								   schedule,
								   coupons,
								   day_count)

bond_engine = ql.DiscountingBondEngine(spot_curve_handle)
fixed_rate_bond.setPricingEngine(bond_engine)

print(fixed_rate_bond.NPV())










