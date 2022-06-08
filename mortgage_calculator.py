#!/usr/bin/env python3

__authors__ = 'Arun Manohar'
__license__ = '3-clause BSD'
__maintainer__ = 'Arun Manohar'
__email__ = 'arunmano121@outlook.com'

# modules necessary to write out excel files
import xlsxwriter
# plotting tools
import matplotlib.pyplot as plt


def visualize_payments(home_val, years, int_rate, mon_hoa, mon_maint,
                       month_h, int_h, prin_h, tot_int, tot_home_ins,
                       tot_prop_tax, tot_hoa, tot_maint):
    '''
    Plot principal vs interest over life of loan, and proportion of
    amounts over the life of loan.

    Parameters
    ----------
    home_val: float
        value of the home
    years: int
        number of years in the loan
    int_rate: float
        fixed interest rate
    mon_hoa: float
        monthly HOA and Mello-Roos fees
    mon_maint: float
        monthly maintenance fees
    month_h: list of int
        list containing month of payment in numbers 1, 2, 3... etc.
    int_h: list of float
        list containing the interest paid every month
    prin_h: list of float
        list containing the principal paid every month
    tot_int: float
        total interest paid over life of loan
    tot_home_ins: float
        total home insurance over life of loan
    tot_prop_tax: float
        total property tax over life of loan
    tot_hoa: float
        total HOA and Mello-Roos over life of loan
    tot_maint: float
        total maintenance over life of loan

    Returns
    -------
    None
    '''

    fig, ax = plt.subplots(nrows=1, ncols=2)
    fig.suptitle(('Home Value: \\$%0.2fM, Loan Term: %d years, Int Rate: '
                  '%0.2f%%, Monthly HOA/Mello-Roos: \\$%d, Monthly Maint.:'
                  ' \\$%d')
                 % (home_val/1e6, years, int_rate, mon_hoa, mon_maint))

    # plot stacked bar chart
    ax[0].bar(month_h, int_h, color='r')
    ax[0].bar(month_h, prin_h, bottom=int_h, color='b')
    ax[0].set_xlabel('Month')
    ax[0].set_ylabel('Principal and Interest ($)')
    ax[0].legend(['Interest', 'Principal'])
    ax[0].set_title('Principal and Interest over life of loan')

    # pie chart to show the total proportion of amount over life of loan
    labels = ['Interest', 'Home Insurance', 'Home Value', 'HOA',
              'Property Tax', 'Maintenance']
    items = [tot_int, tot_home_ins, home_val, tot_hoa, tot_prop_tax,
             tot_maint]
    explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
    ax[1].pie(items, explode=explode, labels=labels, autopct='%1.1f%%',
              shadow=True, startangle=90)
    ax[1].set_title('Proportion of different components')
    ax[1].axis('equal')

    plt.tight_layout()
    plt.show()
    return


def write_excel(title, month, interest, principal, out_prin,
                mon_hoa, mon_home_ins, mon_prop_tax, mon_bank_pay,
                mon_maint, mon_pay, home_val, down_pay, loan_amt,
                tot_int, tot_prop_tax, tot_home_ins, tot_hoa, tot_maint,
                tot_pay, int_loan_rat, int_7yr, int_7yr_tot_rat,
                out_prin_7yr):
    '''
    write out payment schedule into excel sheet

    Parameters
    ----------
    title: str
        name of the excel file
    month: int
        numeric month
    interest: float
        interest component of the monthly payment
    principal: float
        principal component of the monthly payment
    out_prin: float
        outstanding principal component owed to bank
    mon_hoa: float
        monthly HOA and Mello-Roos fees
    mon_home_ins: float
        monthly home insurance
    mon_prop_tax: float
        monthly property tax
    mon_bank_pay: float
        total monthly payment to bank including principal and interest
    mon_maint: float
        total monthly maintenance
    mon_pay: float
        total monthly commitment
    home_val: float
        value of home
    down_pay: float
        downpayment at time of purchase
    loan_amt: float
        outstanding loan amount
    tot_int: float
        total interest paid over life of loan
    tot_prop_tax: float
        total property tax over life of loan
    tot_home_ins: float
        total home insurance over life of loan
    tot_hoa: float
        total HOA and Mello-Roos over life of loan
    tot_maint: float
        total maintenance over life of loan
    tot_pay: float
        total payment over life of loan
    int_loan_rat: float
        interest to loan amount ratio
    int_7yr: float
        interest paid over the first 7 years of loan
    int_7yr_tot_rat: float
        ratio of interest paid over 7 years to life time
    out_prin_7yr: float
        outstanding principal remaining after 7 years

    Returns
    -------
    None
    '''

    # file name to write out
    workbook = xlsxwriter.Workbook(title)
    worksheet = workbook.add_worksheet()

    # setting up necessary formats
    fmt = workbook.add_format({'bold': True})
    money = workbook.add_format({'num_format': '[$$]#,##0.00'})
    pct = workbook.add_format({'num_format': '0.00%'})

    # write out headers using format
    worksheet.write(0, 0, 'Month', fmt)
    worksheet.write(0, 1, 'Interest', fmt)
    worksheet.write(0, 2, 'Principal', fmt)
    worksheet.write(0, 3, 'HOA', fmt)
    worksheet.write(0, 4, 'Home Ins.', fmt)
    worksheet.write(0, 5, 'Prop. Tax', fmt)
    worksheet.write(0, 6, 'Maintenance', fmt)
    worksheet.write(0, 7, 'Mon. Bank Payment', fmt)
    worksheet.write(0, 8, 'Mon. Commitment', fmt)
    worksheet.write(0, 9, 'Out. Principal', fmt)

    # write out individual lines of data
    for i in range(len(month)):
        worksheet.write(i + 2, 0, month[i])
        worksheet.write(i + 2, 1, interest[i], money)
        worksheet.write(i + 2, 2, principal[i], money)
        worksheet.write(i + 2, 3, mon_hoa, money)
        worksheet.write(i + 2, 4, mon_home_ins, money)
        worksheet.write(i + 2, 5, mon_prop_tax, money)
        worksheet.write(i + 2, 6, mon_maint, money)
        worksheet.write(i + 2, 7, mon_bank_pay, money)
        worksheet.write(i + 2, 8, mon_pay, money)
        worksheet.write(i + 2, 9, out_prin[i], money)

    worksheet.write('L1', 'Home Value', fmt)
    worksheet.write('L2', 'Down Payment', fmt)
    worksheet.write('L3', 'Loan Amt.', fmt)
    worksheet.write('L4', 'Tot. Interest', fmt)
    worksheet.write('L5', 'Tot. Prop. Tax', fmt)
    worksheet.write('L6', 'Tot. Home Ins.', fmt)
    worksheet.write('L7', 'Tot. HOA', fmt)
    worksheet.write('L8', 'Tot. Maintenance', fmt)
    worksheet.write('L9', 'Tot. Payment', fmt)
    worksheet.write('L10', 'Int-Loan Ratio', fmt)
    worksheet.write('L11', '7yr Interest', fmt)
    worksheet.write('L12', 'Int 7yr-Total Ratio', fmt)
    worksheet.write('L13', 'Out. Prin. 7yr', fmt)

    worksheet.write('M1', home_val, money)
    worksheet.write('M2', down_pay, money)
    worksheet.write('M3', loan_amt, money)
    worksheet.write('M4', tot_int, money)
    worksheet.write('M5', tot_prop_tax, money)
    worksheet.write('M6', tot_home_ins, money)
    worksheet.write('M7', tot_hoa, money)
    worksheet.write('M8', tot_maint, money)
    worksheet.write('M9', tot_pay, money)
    worksheet.write('M10', int_loan_rat/100, pct)
    worksheet.write('M11', int_7yr, money)
    worksheet.write('M12', int_7yr_tot_rat/100, pct)
    worksheet.write('M13', out_prin_7yr, money)

    # finished writing - close the workbook
    workbook.close()

    return


def calc_mon_pay(out_prin, months, int_rate):
    '''
    calculate monthly payment including interest and principal

    Parameters
    ----------
    out_prin: float
        outstanding principal amount owed to bank
    months: int
        number of remaining months in loan
    int_rate: float
        fixed interest rate

    Returns
    -------
    [payment, interest, principal]: list
        list containing total monthly payment to bank, interest component in
        the monthly payment, principal component in the monthly payment
    '''

    # monthly payment not including home ins and property tax and HOA
    # this only includes the loan amount based payment that is due to bank
    payment = (out_prin * (int_rate / (12 * 100)) /
               (1 - (1 + int_rate / (12 * 100))**(-months)))

    # interest component
    interest = (int_rate/(12 * 100))*out_prin

    # principal component
    principal = payment - interest

    return [payment, interest, principal]


def calc_schedule(loan_amt, years, int_rate, loan_type):
    '''
    Calculate schedule of payments month over month

    Parameters
    ----------
    loan_amt: float
        outstanding loan amount
    years: int
        number of years in the loan
    int_rate: float
        fixed interest rate at start of the loan
    loan_type: str
        Indicator to specify if the loan is a regular loan or interest only

    Returns
    -------
    [pay_h, int_h, prin_h, month_h, out_prin_h]: list
        list containing monthly total payment to bank, monthly interest
        component to bank, monthly principal component to bank, month of
        payment in numbers 1, 2, 3... etc, outstanding principal after
        current monthly payment
    '''

    pay_h = []
    int_h = []
    prin_h = []
    month_h = []
    out_prin_h = []

    # at the very start, the outstanding principal is the loan amount
    out_prin = loan_amt

    # iterate through the life of loan
    for months in range(1, years*12 + 1):
        [payment, interest, principal] = \
            calc_mon_pay(out_prin,
                         years*12 - months + 1, int_rate)

        # interest only loan - so set back principal to 0
        if loan_type == 'I':
            principal = 0
            payment = interest

        # outstanding principal reduces every month
        out_prin = out_prin - principal
        # print(months, payment, interest, principal)

        # append the monthly breakdown into the arrays
        pay_h.append(payment)
        int_h.append(interest)
        prin_h.append(principal)
        month_h.append(months)
        out_prin_h.append(out_prin)

        # when the loan is paid off - stop looping, this is relevant when
        # there is additional monthly payments
        if out_prin <= 0:
            break

    return [pay_h, int_h, prin_h, month_h, out_prin_h]


def get_valid_input(msg):
    '''
    gets valid inputs for the home prices or down payments in a variety of
    formats - the user could enter like 1M or 1000000 or 1000K or $1M, etc.

    Parameters
    ----------
    msg: str
        message to be printed on the screen

    Returns
    -------
    None
    '''

    while True:
        try:
            # get input
            inp = input(msg)
            mod = float(inp.strip(' kK$%Mm,'))

            # check to see if value is in 1000's
            if 'k' in inp or 'K' in inp:
                val = mod * 1000

            # check to see if value is in 1000000's
            elif 'm' in inp or 'M' in inp:
                val = mod * 1000000

            # else value is as listed
            else:
                val = mod
            break

        except Exception as e:
            print(e)
            print('Enter as 100000 or $10,000 or $100K or 100K')

    return val


def main():
    '''
    Calculates the schedule of payments given mortgage parameters.

    The parameters that are involved in calculating the monthly parameters
    are home value, down payment, loan term, interest rate, monthly HOA,
    property tax and home insurance which are roughly based on the property
    tax rates (1.25%). The monthly schedule of payments are output to an
    excel file.
    '''

    # home value
    home_val = get_valid_input('Home value: ')

    # downpayment - typically less than 30% of home value or amount
    # enter maximum down payment possible
    down_pay = get_valid_input('Down payment: ')

    # regular loan or interest only loan
    loan_type = str(input('Reg. loan (R) or Int. only (I): '))

    # loan term in years
    years = int(input('Loan term (years): '))

    # interest rate
    int_rate = float(input('Interest rate (%): '))

    # loan amount is home value minus down payment
    loan_amt = home_val - down_pay

    # Monthly HOA and Mello-Roos
    mon_hoa = int(input('Monthly HOA and Mello-Roos ($): '))

    # Monthly maintenance
    mon_maint = int(input('Monthly maintenance ($): '))

    # monthly property tax - typically around 1.25% in San Diego, CA area
    prop_tax_pct = float(input('Property tax percentage (%): '))
    # monthly property tax
    mon_prop_tax = home_val * prop_tax_pct / 100 / 12
    # typical monthly home insurance
    mon_home_ins = home_val * prop_tax_pct / 100 / 10 / 12

    # write out amortization schedule
    write_amort_flag = input('Write amortization schedule (y/n): ')

    # visualize amortization schedule
    visualize_amort_flag = input('Visualize amortization schedule (y/n): ')

    # calculate the schedule of payments
    print('-'*60)
    print('calculating schedule of payments month over month...')
    print('-'*60)
    [pay_h, int_h, prin_h, month_h, out_prin_h] = \
        calc_schedule(loan_amt, years, int_rate, loan_type)

    if loan_type == 'R':
        print('Regular Loan')
    else:
        print('Interest Only Loan')

    # loan amount
    print('Loan amount: $%0.2f' % (loan_amt))

    if loan_type == 'R':
        # bank monthly payment is sum of principal and interest
        mon_bank_pay = pay_h[0]
        print('Monthly payment to bank (Principal + Interest): $%0.2f'
              % (mon_bank_pay))
    else:
        # bank monthly payment is interest only
        mon_bank_pay = pay_h[0]
        print('Monthly payment to bank (Interest): $%0.2f'
              % (mon_bank_pay))

    # total monthly commitment is sum of bank payment, hoa,
    # home ins, prop tax and maintenance
    mon_pay = mon_bank_pay + \
        mon_hoa + mon_home_ins + mon_prop_tax + mon_maint
    print('Total monthly commitment: $%0.2f' % (mon_pay))

    # total interest over the life of loan
    tot_int = sum(int_h)
    print('\nTotal interest payment over %d months: $%0.2f' %
          (years*12, tot_int))

    # total property tax over the life of loan
    tot_prop_tax = mon_prop_tax*12*years
    print('Total taxes over the %d months: $%0.2f' %
          (years*12, tot_prop_tax))

    # total home insurance over the life of loan
    tot_home_ins = mon_home_ins*12*years
    print('Total home insurance over the %d months: $%0.2f' %
          (years*12, tot_home_ins))

    # total HOA over the life of loan
    tot_hoa = mon_hoa*12*years
    print('Total HOA/Mello-Roos over the %d months: $%0.2f' %
          (years*12, tot_hoa))

    # total maintenance over the life of loan
    tot_maint = mon_maint*12*years
    print('Total maintenance over the %d months: $%0.2f' %
          (years*12, tot_maint))

    # total payment over the life of loan
    tot_pay = down_pay + years*12*mon_pay
    print('Total payment over the %d months: $%0.2f' %
          (years*12, tot_pay))

    # ratio of interest to money borrowed from bank
    int_loan_rat = tot_int/loan_amt*100
    print('\nInterest-Loan Ratio: %0.2f%%' % (int_loan_rat))

    # interest that is paid over the first 7 years
    int_7yr = sum(int_h[0:7*12])
    print('\nInterest paid over the first 7 years: $%0.2f' % (int_7yr))

    # Proportion of interest that is paid over the first 7 years
    int_7yr_tot_rat = int_7yr / tot_int * 100
    print('Proportion of total interest paid in first 7 years: %0.2f%%' %
          (int_7yr_tot_rat))

    # Outstanding principal after first 7 years
    out_prin_7yr = out_prin_h[7*12-1]
    print('Outstanding principal after 7 years: $%0.2f' % (out_prin_7yr))

    # Principal paid in 7 years
    print('Principal paid in 7 years: $%0.2f' % (loan_amt - out_prin_7yr))

    # interest that is paid over the first 10 years
    int_10yr = sum(int_h[0:10*12])
    print('\nInterest paid over the first 10 years: $%0.2f' % (int_10yr))

    # Proportion of interest that is paid over the first 10 years
    int_10yr_tot_rat = int_10yr / tot_int * 100
    print('Proportion of total interest paid in first 10 years: %0.2f%%' %
          (int_10yr_tot_rat))

    # Outstanding principal after first 10 years
    out_prin_10yr = out_prin_h[10*12-1]
    print('Outstanding principal after 10 years: $%0.2f' % (out_prin_10yr))

    # Principal paid in 10 years
    print('Principal paid in 10 years: $%0.2f' % (loan_amt - out_prin_10yr))

    if write_amort_flag.upper() == 'Y':
        # write the breakdown into excel file
        print('-'*60)
        print('writing out payment schedule into excel sheet...')
        print('-'*60)

        # title for the excel file
        title = 'monthly_schedule.xlsx'

        # todo: condense necessary items to be written into excel using dict
        write_excel(title, month_h, int_h, prin_h, out_prin_h,
                    mon_hoa, mon_home_ins, mon_prop_tax, mon_bank_pay,
                    mon_maint, mon_pay, home_val, down_pay, loan_amt,
                    tot_int, tot_prop_tax, tot_home_ins, tot_hoa, tot_maint,
                    tot_pay, int_loan_rat, int_7yr, int_7yr_tot_rat,
                    out_prin_7yr)

    if visualize_amort_flag.upper() == 'Y':
        # plot principal vs interest over life of loan, and proportion of
        # amounts over the life of loan
        visualize_payments(home_val, years, int_rate, mon_hoa, mon_maint,
                           month_h, int_h, prin_h, tot_int, tot_home_ins,
                           tot_prop_tax, tot_hoa, tot_maint)


if __name__ == '__main__':
    main()
