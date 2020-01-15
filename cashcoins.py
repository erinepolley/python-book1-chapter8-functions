# import math

dollarAmount = 8.69

def count_my_money(num):
    piggyBank = {
        "pennies": 0,
        "nickels": 0,
        "dimes": 0,
        "quarters": 0
    }
    orig_num = num * 100
    amount_in_quarters = orig_num - orig_num%25
    # print(amount_in_quarters)
    quarter_num = amount_in_quarters/25
    # print(quarter_num)
    piggyBank["quarters"] = quarter_num
    # print(piggyBank["quarters"])

    num_no_quarters = orig_num-amount_in_quarters
    amount_in_dimes = num_no_quarters - num_no_quarters%10
    # print(amount_in_dimes)
    dime_num = amount_in_dimes/10
    # print(dime_num)
    piggyBank["dimes"] = dime_num

    num_no_dimes = num_no_quarters - amount_in_dimes
    # print(num_no_dimes)
    amount_in_nickels = num_no_dimes - num_no_dimes%5
    nickel_num = amount_in_nickels/5
    piggyBank["nickels"] = nickel_num
    # print(piggyBank["nickels"])

    num_no_nickels = num_no_dimes - amount_in_nickels
    # print(num_no_nickels)
    amount_in_pennies = num_no_nickels - num_no_nickels%1
    piggyBank["pennies"] = amount_in_pennies
    # print(piggyBank["pennies"])

    # print(piggyBank.items())
    print(f'Your piggy bank has {piggyBank["quarters"]} quarters, {piggyBank["dimes"]} dimes, {piggyBank["nickels"]} nickels, and {piggyBank["pennies"]} pennies.')

count_my_money(8.69)




# print(8.69/25)
# print(2.1725*.1)
# print(.21725*.05)
# print(.0108625 * .01)

# print(8.69-2.1725)
# print(6.5175/25)

