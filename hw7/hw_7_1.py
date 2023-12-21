loan = int(input('Enter the amount >>> '))
loan_term = int(input('Enter the term of loan in years - 1 or 5 >>> '))

term_month = loan_term * 12
term_total = loan_term * 12
pattern_title = "Month     Repayment    Percent    Loan left to pay"
pattern_row = "{:^7} {:^13.2f} {:^11.2f} {:^17.2f}"
print(pattern_title)

if loan_term == 1 or loan_term == 5:
    for term_month in range(1, term_month + 1):
        payment_month = (loan / term_total)
        if term_month <= 24:
            percent = 0.02
        else:
            percent = 0.04

        percent_month = loan * percent
        loan = loan - payment_month
        term_total = term_total - 1
        print(pattern_row.format(term_month, payment_month, percent_month, loan))
