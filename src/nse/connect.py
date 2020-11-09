from nse import Nse

db = Nse()

data = db.live("HDFCBANK")   
print(data)

#Load OIL Brand Data.
data = db.load('HDFCBANK')
#Bar Grap Of Data
Hdata = db.history("HDFCBANK","05-10-2020",'15-10-2020')
print(Hdata)