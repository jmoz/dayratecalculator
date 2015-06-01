import sys

try:
    rate_pd = int(sys.argv[1])
except (IndexError, ValueError):
    raise RuntimeError("script must be run with day rate integer as parameter e.g. python calculator.py 400")

rate_pw = rate_pd * 5
rate_total = rate_pw
vat = 1.2

for i in range(1, 53):
    print "week {} subtotal {} inc vat {}".format(i, rate_total, int(rate_total * vat))
    rate_total += rate_pw
