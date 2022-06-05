#!/usr/bin/env python3

__authors__ = 'Arun Manohar'
__license__ = '3-clause BSD'
__maintainer__ = 'Arun Manohar'
__email__ = 'arunmano121@outlook.com'

# plotting tools
import matplotlib.pyplot as plt
# numpy for array tasks
import numpy as np


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
    try:
        payment = (out_prin * (int_rate / (12 * 100)) /
                   (1 - (1 + int_rate / (12 * 100))**(-months)))
    except ZeroDivisionError:
        # if interest rate is 0%
        payment = out_prin/months

    # interest component
    interest = (int_rate/(12 * 100))*out_prin

    # principal component
    principal = payment - interest

    return [payment, interest, principal]


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
    Calculates the monthly payments given mortgage parameters, and
    graphically depict results for a variety of interest rates.

    A variety of home prices and interest rates are considered and the
    resulting monthly commitment is plotted using a series a lines depicting
    the different home prices for various interest rates.

    This program should aid the user to determine what kinds of home prices
    they could afford at different interest rates given their cap on monthly
    cash outflow and down payment.
    '''

    # home value lower bound
    home_val_lb = get_valid_input('Home price lower range: ')

    # home value upper bound
    home_val_ub = get_valid_input('Home price upper range: ')

    # home price steps - like 25k, 50k, etc.
    steps = get_valid_input('Home price steps: ')

    # home value is in range between lower bound and upper bound
    # in steps of user specified value.
    home_val = np.array(range(int(home_val_lb), int(home_val_ub) + 1,
                              int(steps)))
    # reshape to help with numpy broadcasting
    home_val = home_val.reshape(len(home_val), 1)

    # downpayment - typically less than 30% of home value or amount
    # enter maximum down payment possible
    down_pay = get_valid_input('Enter max possible down payment: ')

    # loan amount is home value minus down payment
    loan_amt = home_val - down_pay

    # loan term
    loan_term = int(input('Loan term (years): '))

    # Monthly HOA and Mello-Roos
    hoa = int(input('Monthly HOA and Mello-Roos ($): '))

    # Monthly maintenance
    maint = int(input('Monthly maintenance ($): '))

    # max monthly cash available
    mon_budget = int(input('Monthly max budget ($): '))

    # monthly property tax - typically around 1.25% in San Diego, CA area
    prop_tax_pct = float(input('Enter property tax percentage (%): '))

    # interest rate - simulate between desired interest rate range in
    # steps of 0.25%
    msg = 'Enter interest rate range seperated by (-): '
    int_rate = np.array(input(msg).strip('% ').split('-'))
    # adding delta of 0.01 to upper bound so that it is included
    int_rate = np.arange(float(int_rate[0]), float(int_rate[-1])+0.01, 0.25)
    # reshape to help with numpy broadcasting
    int_rate = int_rate.reshape(1, len(int_rate))

    # calculate the schedule of payments
    [payment, interest, principal] = \
        calc_mon_pay(loan_amt, loan_term*12, int_rate)

    # monthly property tax
    prop_tax = prop_tax_pct / (12*100) * home_val

    # monthly home insurance
    home_ins = prop_tax_pct / (12*100) * home_val / 10

    # total monthly commitment is sum of payment to bank, hoa, home ins and
    # prop tax, maintenance
    mon_commit = payment + hoa + home_ins + prop_tax + maint

    # plots the results including the range of interest rates on x-axis
    # monthly commitment on the y-axis for the different home prices.
    # the max budget line is also shown using dash-dot horizontal line

    fig, ax = plt.subplots(nrows=1, ncols=1)

    # descriptive title for the figure
    fig.suptitle(('Home value range: \\$%0.2fM - \\$%0.2fM, '
                  'Down payment: \\$%dK, '
                  '\nLoan Term: %d years, Monthly HOA/Mello-Roos: \\$%d, '
                  'Monthly Maint.: \\$%d')
                 % (home_val_lb/1e6, home_val_ub/1e6, down_pay/1e3,
                    loan_term, hoa, maint))

    # plot line series
    # iterate through the different home values
    for i in range(len(home_val)):
        ax.plot(np.squeeze(int_rate), mon_commit[i, :],
                label='%0.3f' % (home_val[i]/1e6))
    # add horizontal line showing the max budget
    ax.axhline(mon_budget, linestyle='-.', linewidth=2, label='Max. budget')
    ax.set_xlim([np.squeeze(int_rate)[0], np.squeeze(int_rate)[-1]])
    ax.set_xlabel('Interest Rate [%]')
    ax.set_ylabel('Monthly Commitment ($)')
    ax.set_title('Monthly Commitment vs Interest Rate')
    # plot legend box outside of the main figure area
    ax.legend(title='Home price [\\$M]', bbox_to_anchor=(1.05, 1),
              loc='upper left', borderaxespad=0.)
    plt.grid()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
