"""
Converting a list of dictionaries with nested sub-dictionaries to a dataframe 
"""

import os
import pandas as pd
import pickle


raw_data_file = os.path.join('docs_backups', '20200521_2203.pickle')
with open(raw_data_file, 'rb') as f:
    docs = pickle.load(f)['docs']

# If you don't care about renaming, you can simply use a list of the fields 
# instead (the keys below) and skip the 'rename' part later

fields = {
    '_id': 'id',
    '_source.leaderName': 'name',
    '_source.leaderEmail': 'email',
    '_source.phone': 'phone',
    '_source.bookingCode': 'bookingCode',
    '_source.bookingDate': 'bookingDate',
    '_source.reservationAmount': 'reservationAmount',
    '_source.totalAmount': 'totalAmount',
    '_source.failed': 'failed',
    '_source.totalPassengers': 'totalPassengers',
    '_source.totalVehicles': 'totalVehicles',
    '_source.metadata.locale': 'locale',
    '_source.metadata.affiliateId': 'affiliate'
}

df = pd.json_normalize(docs)[fields].rena
df.bookingDate = pd.to_datetime(df.bookingDate)

