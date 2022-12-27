def compoundinterest(p,r,t):
    amount = p * (pow((1+r/100),t))
    ci = amount - p
    return ci
print("The compound intrest is :",compoundinterest(1000,5,3))
