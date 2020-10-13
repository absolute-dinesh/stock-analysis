from nsetools import Nse

nse = Nse()

q = nse.get_quote('infy')

from pprint import pprint

pprint(q)