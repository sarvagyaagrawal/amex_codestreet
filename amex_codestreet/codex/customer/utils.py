
def calc_total_savings(balance, month_save,time=6):
    return balance + month_save*time

def calc_debt(total_debt,amt, rate, time=6):
    ''' time in months'''
    tot=amt
    for i in range(time):
        tot+= (tot * (rate/100))
    return tot + total_debt

def calc_minimum_amt(mini_amt2, mini_amt1):
    return mini_amt2 + mini_amt1

def income_future_calc(income,time=6):
    return income*time

def debt_to_inc_ratio_calc(total_debt, income):
    return total_debt/income

def return_income(income):
    return income/1000
def return_debt(total_debt):
    return total_debt/1000

def spending_to_saving(spend,save):
    return spend/save

    