import pandas as pd



"""Merges datasets A and B via a left join.
Drops entries with NaN in SUBSCR_NO column."""



dataA = pd.read_csv("/home/kaleblob/PI_Exchange/piexchange/H_ODS_SUBSCR_INFO.csv")
dataB = pd.read_csv("/home/kaleblob/PI_Exchange/piexchange/H_ODS_SUBSCR_INFO.csv")

# if NaNs are included, then they're treated as duplicate entries
# which results in a massive table with m*n rows.
dataA = dataA.dropna(subset=['SUBSCR_NO'])
dataB = dataB.dropna(subset=['SUBSCR_NO'])
dataMerge = pd.merge(dataA,dataB,how='left',left_on='SUBSCR_NO',right_on='SUBSCR_NO')
dataMerge.to_csv('merged.csv')