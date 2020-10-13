from nse import Nse

db = Nse()

data = db.live("HDFCBANK")   
print(data)

#Load OIL Brand Data.
data = db.load('HDFCBANK')
#Bar Grap Of Data
Hdata = db.history("HDFCBANK","05-03-2020",'07-03-2020')
print(Hdata)