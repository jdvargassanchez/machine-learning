from unittest import result
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

def getdataset():
    df = pd.read_csv("credit_card_dataset.csv")
    df = df.dropna()
    data = df.to_dict(orient="records")

    return data

def ApplyClusteringKmeans():
    data =getdataset()
    x = [[
        person["BALANCE"],
        person["PURCHASES"],
        person["CREDIT_LIMIT"]
    ] for person in data]

    scaler=StandardScaler()
    Xscaled=scaler.fit_transform(x)

    model=KMeans(n_clusters=3,random_state=42,n_init=10)
    labels=model.fit_predict(Xscaled)
    result=[]


    for i,person in enumerate(data):
        row=person.copy()
        row["cluster"]=int (labels[i])
        result.append(row)

    summaryClusters={}
    for label in labels:
        label=int(label)
        summaryClusters[label] = summaryClusters.get(label,0) + 1 

    centers=model.cluster_centers_.tolist()

    return{
        "result":result,
        "summaryClusters":summaryClusters,
        "centers":centers
    }
    