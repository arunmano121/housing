Calculates the monthly commitment given mortgage parameters, and graphically
depict results for a variety of interest rates.

A variety of home prices and interest rates (based on user input) are
considered and the resulting monthly commitment is plotted using a series of
lines depicting the different home prices for various interest rates.

This program should aid the user to determine what kinds of home prices they
could afford at different interest rates given their cap on monthly cash
outflow and down payment.
    
The parameters that are involved in calculating the monthly parameters are
home value, down payment, loan term, interest rate, monthly HOA, maintenance,
property tax and home insurance (which are roughly based on the property tax
rates.

Input parameters
----------------

* Home value (lower bound, upper bound, steps): purchase price of home. You
can specify in a variety of formats like 1000000 or 1,000,000 or 1M or $1M
or 1000K, etc. The resulting simulation considers prices between lower and
upper bound in steps of user specified value. 
* Down payment: Maximum down payment that could be paid to bank. You can
specify in a variety of number formats like 200000 or 200,000 or 200K or
$0.2M, etc. or using percentage like 20%. Often times, there is a upper limit
to this amount. 
* Loan term: specify number of years of the loan period - typically 30 years,
or 15 years, etc.
* HOA/Mello-Roos: Monthly HOA and Mello-Roos. Typically, varies between $0 for
older properties to as much as $1000 for newer properties and communities.
* Maintenance: Monthly maintenance cost - varies between property. Typically,
around $200.
* Property tax percentage: Property tax rate determines the monthly property
tax and the approximate home insurance rates. In the San Diego area, the
rates are around 1.25% annual. 
* Annual interest rate: Specify the annual interest rate for your mortagage.
Varies between 2%-15%. The range is split between lower and upper bound in
steps of 0.25% and the monthly outflow is calculated for each of the interest
rates.
* Monthly budget: This is the maximum amount that you can set aside towards
housing payments each month. This will be depicted using a dash-dot line. 
