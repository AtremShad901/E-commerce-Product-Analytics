import pandas as pd 
from data_loader import load_table

def APRAU(user_mart:pd.DataFrame)->float:
    return user_mart['total_revenue'].mean()

def AVG_DAU(session_mart:pd.DataFrame)->float:
    df = session_mart.copy()
    df['event_datetime'] = pd.to_datetime(df['event_datetime']).dt.date
    return df.groupby('event_datetime')['user_id'].nunique().mean()

def AVG_WAU(session_mart:pd.DataFrame)->float:
    df = session_mart.copy()
    df['event_datetime'] = pd.to_datetime(df['event_datetime']).dt.to_period('W')
    return df.groupby('event_datetime')['user_id'].nunique().mean()

def AVG_MAU(session_mart:pd.DataFrame)->float:
    df = session_mart.copy()
    df['event_datetime'] = pd.to_datetime(df['event_datetime']).dt.to_period('M')
    return df.groupby('event_datetime')['user_id'].nunique().mean()

def stickiness(session_mart:pd.DataFrame)->float:
    return AVG_DAU(session_mart) / AVG_MAU(session_mart)

def revenue_per_session(users_mart:pd.DataFrame) -> float:
    df = users_mart.copy()
    total_revenue = df['total_revenue'].sum()
    total_session = df['total_session'].sum()
    return total_revenue/total_session

def session_conversion_rate(session_mart:pd.DataFrame ) -> float:
    df = session_mart.copy()
    return df['converted'].mean()

def AOV(revenue_mart:pd.DataFrame) -> float : 
    df = revenue_mart.copy()
    return df['avg_order_value'].mean()

def PARETO(user_mart:pd.DataFrame ,
            top_share :float = 0.2) -> float : 
    df = user_mart.copy()
    df = df[df['total_revenue']!=0].sort_values(by='total_revenue' , ascending=False)
    total_revenue = df['total_revenue'].sum()

    top_20_percent_users = int(len(df)*top_share)
    revenue_top20 = df.iloc[:top_20_percent_users]['total_revenue'].sum()
    return revenue_top20 / total_revenue

def funnel(staging_events:pd.DataFrame) ->pd.DataFrame: 
    df = staging_events.copy()
    funnel_counts = (
        df.groupby('event_type' , as_index=False)['user_id'] 
        .nunique()
        .sort_index()
        .rename(columns = { "user_id":"user_id_count"})
    )
    return funnel_counts

def retention(staging_events : pd.DataFrame , days :int = 7 , disp :int = 0 ) -> float : 
    df = staging_events.copy()
    df['event_datetime'] = pd.to_datetime(df['event_datetime'])
    df['date'] = df['event_datetime'].dt.date

    first_visit = df.groupby('user_id')['date'].min().reset_index()\
                .rename(columns={"date":"first_date"})
    
    df = df.merge(first_visit , on = 'user_id')
    df['diff'] = (pd.to_datetime(df['date']) - 
                pd.to_datetime(df['first_date'])
                ).dt.days  
    
    retained  = df[(df['diff'] >= days-disp)&(df['diff']<=days+disp)]['user_id'].nunique()

    total_users = first_visit['user_id'].nunique()
    
    return retained / total_users


if __name__ == "__main__":
    user_mart = load_table('user_mart')
    session_mart = load_table('sessions_mart')
    revenue_mart = load_table('revenue_mart')
    staging_events = load_table('staging_events')
    print(retention(staging_events , days = 30 ,disp = 3 ))