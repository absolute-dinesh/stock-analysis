from nse import Nse

db = Nse()
#Load OIL Brand Data.
data = db.load('OIL')
#Bar Grap Of Data
db.bar(data)