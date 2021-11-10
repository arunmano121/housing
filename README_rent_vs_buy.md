This program compares the scenario of buying vs renting given certain
parameters.

The parameters that are involved in calculating the monthly parameters are
home value, down payment, loan term, interest rate, monthly HOA, maintenance,
property tax and home insurance (which are roughly based on the property tax
rates (1.25%)).

Other parameters involved in modeling are rent appreciation, property
appreciation, investment returns, tax bracket, number of years, etc.

Once the parameters are input, the program calculates the monthly schedule
comparing renting and buying and outputs to terminal, and also writes to
excel sheet, and plots the monthly variation to show net worth between renting
and buying.

Input parameters
----------------

* Home value: purchase price of home. You can specify in a variety of formats
   like 1000000 or 1,000,000 or 1M or $1M or 1000K, etc.
* Down payment: down payment that is paid to bank. You can specify in a
   variety of number formats like 200000 or 200,000 or 200K or $0.2M, etc. or
   using percentage like 20%.
* Loan term: specify number of years of the loan period - typically 30 years,
   or 15 years, etc.
* HOA/Mello-Roos: Monthly HOA and Mello-Roos. Typically, varies between $0 for
   older properties to as much as $1000 for newer properties and communities.
* Maintenance: Monthly maintenance cost - varies between property. Typically,
   around $200.
* Tax bracket: Since mortgage insurance and property tax are tax deductible,
   enter your approximate tax bracket in percentage - typically varies between
   10% - 40%.
* Rent: Cost to rent a similar home in dollars.
* Years to model: Specify in years the number of years to consider for the
   model - example: enter 5 if you would like to model for 5 years.
* Annual interest rate: Specify the annual interest rate for your mortagage.
   Varies between 2%-15%. If you are on a variable rate, specify 5 entries
   corresponding to the different years. For example, either enter 3, if you
   are on a fixed 3% rate, or enter 3,5,6,4,5 if you are on a ARM.
* Annual Home Appreciation: Specify the rate at which the annual home prices
   are increasing. If you believe that the rate is fixed, enter a single float
   to indicate that the prices are increasing annually at the same level. If
   the rate if variable every year, enter 2,5,-10,-5,1 to indicate that over
   the next five years the prices are anticipatated to change by 2%, 5%, -10%,
   -5%, 1% each year.
* Annual Rent Appreciation: Specify the rate at which the annual rent is
   increasing. If you believe that the rate is fixed, enter a single float
   to indicate that the rent is increasing annually at the same level. If
   the rate if variable every year, enter 2,5,-10,-5,1 to indicate that over
   the next five years the rents are anticipatated to change by 2%, 5%, -10%,
   -5%, 1% each year.
* Investment Returns: When renting, it is assumed that you invest the down
   payment. Specify the rate at which the investments are anticipated to grow
   each year. If you believe that the rate is fixed, enter a single float
   to indicate that the investments are growing annually at the same level. If
   the rate if variable every year, enter 2,5,-10,-5,1 to indicate that over
   the next five years the investments are anticipatated to change by 2%, 5%,
   -10%, -5%, 1% each year.


Assumptions
-----------

* Property Tax rate is assumed to be 1.25%, and this affects monthly property
  tax, home insurance and tax break calculations. If necessary, change this to
  a value that reflects your situation.
* The down payment amount that was set aside for the buying scenario is
  assumed to be fully invested for the renting scenario. 
