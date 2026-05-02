from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def GetData():
    return [
{"property_id": "House_1", "square_meters": 120, "price_thousands": 210, "age": 12},
{"property_id": "House_2", "square_meters": 145, "price_thousands": 260, "age": 9},
{"property_id": "House_3", "square_meters": 160, "price_thousands": 310, "age": 14},
{"property_id": "House_4", "square_meters": 115, "price_thousands": 195, "age": 10},
{"property_id": "House_5", "square_meters": 175, "price_thousands": 340, "age": 11},
{"property_id": "House_6", "square_meters": 130, "price_thousands": 225, "age": 15},
{"property_id": "House_7", "square_meters": 150, "price_thousands": 280, "age": 8},
{"property_id": "House_8", "square_meters": 165, "price_thousands": 320, "age": 13},
{"property_id": "House_9", "square_meters": 105, "price_thousands": 185, "age": 9},
{"property_id": "House_10", "square_meters": 140, "price_thousands": 250, "age": 11},
{"property_id": "House_11", "square_meters": 155, "price_thousands": 290, "age": 12},
{"property_id": "House_12", "square_meters": 125, "price_thousands": 215, "age": 10},
{"property_id": "House_13", "square_meters": 170, "price_thousands": 330, "age": 14},
{"property_id": "House_14", "square_meters": 135, "price_thousands": 240, "age": 8},
{"property_id": "House_15", "square_meters": 148, "price_thousands": 275, "age": 15},
{"property_id": "House_16", "square_meters": 162, "price_thousands": 305, "age": 11},
{"property_id": "House_17", "square_meters": 118, "price_thousands": 200, "age": 13},
{"property_id": "House_18", "square_meters": 152, "price_thousands": 285, "age": 9},
{"property_id": "House_19", "square_meters": 178, "price_thousands": 345, "age": 12},
{"property_id": "House_20", "square_meters": 122, "price_thousands": 210, "age": 10}
]


def ApplyClusteringManualApp():
    data = GetData()

    x = [[property["square_meters"], property["price_thousands"], property["age"]] for property in data]
    
    scaler = StandardScaler()
    Xscaled = scaler.fit_transform(x)
    
    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    labels = model.fit_predict(Xscaled)
    
    result = []
    for i, property in enumerate(data):
        row = property.copy()
        row["Cluster"] = int(labels[i])
        result.append(row)
        
    clusterSummary = {}
    for label in labels:
        label = int(label)
        clusterSummary[label] = clusterSummary.get(label, 0) + 1
        
    centers = model.cluster_centers_.tolist()

    return {
        "result": result,
        "clusterSummary": clusterSummary,
        "centers": centers
    }