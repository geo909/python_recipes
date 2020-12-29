import os
import pandas as pd
import pickle

docs_pickle = '20200521_2203.pickle'

# This will be used both for parsing the correct fields as well as naming the columns
# Alternatively, you can use a simple list and skip the df.columns = .. part
columns = {
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

def raw_bookings_to_df(file_path, columns)
    """ file_path points to a pickle file that contains a list of dictionaries """

    with open(docs_pickle, 'rb') as f:
        docs = pickle.load(f)['docs']

    df = pd.json_normalize(docs)[columns].rename(columns=columns)
    return df

if __name__ == '__main__':

    df = file_to_df(docs_pickle)
    df.bookingDate = pd.to_datetime(df.bookingDate)
    df.to_pickle('df.pickle')
