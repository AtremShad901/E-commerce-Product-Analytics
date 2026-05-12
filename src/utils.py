import pandas as pd 

def rfm_seg(df : pd.DataFrame , snapshot_date)->pd.DataFrame:
    purchases = df[df['event_type'] == 'purchase'].copy()
    purchases['event_datetime'] = pd.to_datetime(purchases['event_datetime'])

    rfm = (
    purchases
    .groupby('user_id')
    .agg({
        'event_datetime': lambda x: (snapshot_date - x.max()).days,
        'user_id': 'count',
        'price': 'sum'
    })
)

    rfm.columns = ['Recency', 'Frequency', 'Monetary']
    rfm.reset_index(inplace=True)

    rfm['R_score'] = pd.qcut(rfm['Recency'], 4, labels=[4,3,2,1])
    rfm['F_score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, labels=[1,2,3,4])
    rfm['M_score'] = pd.qcut(rfm['Monetary'], 4, labels=[1,2,3,4])

    rfm['RFM_score'] = (
    rfm['R_score'].astype(str) +
    rfm['F_score'].astype(str) +
    rfm['M_score'].astype(str)
    )
    def segment(row):
        if row['RFM_score'] == '444':
            return 'VIP'
        elif row['F_score'] >= 3 and row['M_score'] >= 3:
            return 'Loyal'
        elif row['R_score'] == 4:
            return 'New'
        elif row['R_score'] == 1:
            return 'At Risk'
        else:
            return 'Regular'

    rfm['Segment'] = rfm.apply(segment, axis=1)
    
    return rfm 