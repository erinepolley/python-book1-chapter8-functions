def calc_dollars():
    piggyBank = {
        "quarters": 9845,
        "nickels": 2985,
        "dimes": 65465,
        "pennies": 654,
    }
    dollar_amount = piggyBank["quarters"]/4 + piggyBank["nickels"]/20 + piggyBank["dimes"]/10 + piggyBank["pennies"]
    
    print(f'You have {dollar_amount} in your piggy bank.')

calc_dollars()

