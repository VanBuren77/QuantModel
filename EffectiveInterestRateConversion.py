import QuantLib as ql

# Semi Annual / Annual Interst Rate Calculator

annual_rate = 0.05
day_count = ql.ActualActual()
compound_type = ql.Compounded
frequency = ql.Annual
interest_rate = ql.InterestRate(annual_rate, day_count, compound_type, frequency)

new_frequency = ql.Semiannual
semi_annual_rate = interest_rate.equivalentRate(compound_type, new_frequency, 1)

print("Annual Rate: " + str(interest_rate.rate()))
print("Semi Annual Rate: " +str(semi_annual_rate.rate()))

years = 2.0

annual_compound_rate = (1.0 + annual_rate) ** (years)
semi_annual_compound_rate = (1.0 + semi_annual_rate.rate() / 2.0 ) ** (years * 2.0)

print("")
print("Semi-Annual Compound Rate : "  + str(semi_annual_compound_rate))
print("Semi-Annual Compound Rate : "  + str(semi_annual_rate.compoundFactor(years)))
print("")
print("Annual Compound Rate : " + str(annual_compound_rate))
print("Annual Compound Rate : " + str(interest_rate.compoundFactor(years)))
print("")
print("Annual Discount Factor : " + str(interest_rate.discountFactor(years)))
print("Semi-Annual Discount Factor : " + str(interest_rate.discountFactor(years)))
print("")