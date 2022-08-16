This program calculates the schedule of payments given mortgage parameters.
It outputs the monthly schedule of payments to an excel file, and also
graphically represents the composition of payments. 

This program does not account for any tax breaks and property appreciation or
depreciation. It also assumes fixed mortgage interest rates for the life of
loan. 

Input parameters
----------------
* Loan type: regular fixed rate loan or interest only loan.
* Home value: purchase price of home. You can specify in a variety of formats
  like 1000000 or 1,000,000 or 1M or $1M or 1000K, etc.
* Down payment: down payment that is paid to bank. You can specify in a
  variety of number formats like 200000 or 200,000 or 200K or $0.2M, etc. or
  using percentage like 20%.
* Loan term: specify number of years of the loan period - typically 30 years,
  or 15 years, etc.
* Loan type: Regular or Interest only - both options are allowed and the
  schedule of payments and amortization table are accordingly calculated.
* HOA/Mello-Roos: Monthly HOA and Mello-Roos. Typically, varies between $0 for
  older properties to as much as $1000 for newer properties and communities.
* Maintenance: Monthly maintenance charges. Typically, varies between $350 to
  $1000 for older properties, to as little as $0 for newer properties.
* Annual interest rate: Specify the annual interest rate for your mortagage.
  Varies between 2%-15%. 
* Property tax percentage: Property tax rate determines the monthly property
  tax and the approximate home insurance rates. In the San Diego area, the
  rates are around 1.25% annual. 
* Write amortization (flag): Boolean flag to check if detailed monthly payment
  schedule will be written to excel file.
* Visualize payments (flag): Boolean flag to check if payment breakdown will
  graphically be represented.
