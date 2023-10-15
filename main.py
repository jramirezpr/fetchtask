import numpy as np
import pandas as pd
import tensorflow as tf

from typing import Union

from fastapi import FastAPI

app = FastAPI()
new_model = tf.keras.models.load_model("multimodelfile2")
df_daily = pd.read_csv("data/data_daily.csv")
df_daily["# Date"] = pd.to_datetime(df_daily["# Date"])
df_daily2 = df_daily.set_index("# Date")
df_daily_sorted = df_daily2.sort_index().copy()
df_daily_sorted["num_days_since_jan12021"]=((df_daily_sorted.index.to_series() - pd.to_datetime("2021-01-01"))).dt.days
mn = df_daily_sorted.mean()
dfstd =df_daily_sorted.std()

@app.get("/")
def read_root():
    return {"response": "home","link":"prediction/yyyy-mm-dd/receipts_for_that_day"}


@app.get("/prediction/{last_available_date}/{receipts_for_that_day}/{starting_prediction_day}")
def prediction(last_available_date:  str, receipts_for_that_day:int,starting_prediction_day:str):
    num_days=(pd.to_datetime(last_available_date) - pd.to_datetime("2021-01-01")).days 
    num_predictions = (pd.to_datetime(starting_prediction_day) - pd.to_datetime(last_available_date)).days+29
    pred_input=(np.array([receipts_for_that_day,num_days]) - mn)/dfstd
    pred_list =[]
    while num_predictions>0:
        iresults = new_model(tf.constant([[pred_input]]))
        iresults = iresults[0,:,:].numpy().tolist()
        num_predictions-=len(iresults)
        pred_input = iresults[-1]
        pred_list+=iresults
    df_out=pd.DataFrame(pred_list,columns=["receipt","numdays"]) 
    dfout2=df_out["receipt"]*dfstd["Receipt_Count"] + mn["Receipt_Count"]

    dfout2=dfout2.reset_index()
    dfout2["Date"]= starting_prediction_day
    print(dfout2)
    dfout2["Date1"]=pd.to_datetime(dfout2["Date"])+pd.to_timedelta(dfout2["index"], unit="D")
    dfout2["datep"]= dfout2["Date1"].dt.strftime('%Y-%m-%d')
    print(dfout2)
    return dfout2[["datep","receipt"]].to_json(orient="table") 



