from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np


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
    {"property_id": "House_20", "square_meters": 122, "price_thousands": 210, "age": 10},
    {"property_id": "House_21", "square_meters": 142, "price_thousands": 255, "age": 14},
    {"property_id": "House_22", "square_meters": 168, "price_thousands": 325, "age": 8},
    {"property_id": "House_23", "square_meters": 132, "price_thousands": 230, "age": 11},
    {"property_id": "House_24", "square_meters": 158, "price_thousands": 295, "age": 15},
    {"property_id": "House_25", "square_meters": 128, "price_thousands": 220, "age": 12},
    {"property_id": "House_26", "square_meters": 172, "price_thousands": 335, "age": 9},
    {"property_id": "House_27", "square_meters": 146, "price_thousands": 265, "age": 13},
    {"property_id": "House_28", "square_meters": 112, "price_thousands": 190, "age": 10},
    {"property_id": "House_29", "square_meters": 164, "price_thousands": 315, "age": 14},
    {"property_id": "House_30", "square_meters": 138, "price_thousands": 245, "age": 11},
    {"property_id": "House_31", "square_meters": 156, "price_thousands": 285, "age": 8},
    {"property_id": "House_32", "square_meters": 126, "price_thousands": 215, "age": 15},
    {"property_id": "House_33", "square_meters": 174, "price_thousands": 340, "age": 12},
    {"property_id": "House_34", "square_meters": 144, "price_thousands": 260, "age": 9},
    {"property_id": "House_35", "square_meters": 65, "price_thousands": 95, "age": 2},
    {"property_id": "House_36", "square_meters": 85, "price_thousands": 140, "age": 4},
    {"property_id": "House_37", "square_meters": 55, "price_thousands": 85, "age": 1},
    {"property_id": "House_38", "square_meters": 75, "price_thousands": 120, "age": 3},
    {"property_id": "House_39", "square_meters": 88, "price_thousands": 145, "age": 5},
    {"property_id": "House_40", "square_meters": 60, "price_thousands": 90, "age": 2},
    {"property_id": "House_41", "square_meters": 80, "price_thousands": 130, "age": 4},
    {"property_id": "House_42", "square_meters": 70, "price_thousands": 110, "age": 1},
    {"property_id": "House_43", "square_meters": 52, "price_thousands": 82, "age": 3},
    {"property_id": "House_44", "square_meters": 82, "price_thousands": 135, "age": 5},
    {"property_id": "House_45", "square_meters": 68, "price_thousands": 105, "age": 2},
    {"property_id": "House_46", "square_meters": 78, "price_thousands": 125, "age": 4},
    {"property_id": "House_47", "square_meters": 58, "price_thousands": 88, "age": 1},
    {"property_id": "House_48", "square_meters": 86, "price_thousands": 142, "age": 3},
    {"property_id": "House_49", "square_meters": 62, "price_thousands": 92, "age": 5},
    {"property_id": "House_50", "square_meters": 72, "price_thousands": 115, "age": 2},
    {"property_id": "House_51", "square_meters": 84, "price_thousands": 138, "age": 4},
    {"property_id": "House_52", "square_meters": 54, "price_thousands": 84, "age": 1},
    {"property_id": "House_53", "square_meters": 76, "price_thousands": 122, "age": 3},
    {"property_id": "House_54", "square_meters": 66, "price_thousands": 100, "age": 5},
    {"property_id": "House_55", "square_meters": 89, "price_thousands": 148, "age": 2},
    {"property_id": "House_56", "square_meters": 64, "price_thousands": 96, "age": 4},
    {"property_id": "House_57", "square_meters": 74, "price_thousands": 118, "age": 1},
    {"property_id": "House_58", "square_meters": 56, "price_thousands": 86, "age": 3},
    {"property_id": "House_59", "square_meters": 81, "price_thousands": 132, "age": 5},
    {"property_id": "House_60", "square_meters": 61, "price_thousands": 91, "age": 2},
    {"property_id": "House_61", "square_meters": 79, "price_thousands": 128, "age": 4},
    {"property_id": "House_62", "square_meters": 69, "price_thousands": 108, "age": 1},
    {"property_id": "House_63", "square_meters": 51, "price_thousands": 81, "age": 3},
    {"property_id": "House_64", "square_meters": 83, "price_thousands": 136, "age": 5},
    {"property_id": "House_65", "square_meters": 63, "price_thousands": 94, "age": 2},
    {"property_id": "House_66", "square_meters": 73, "price_thousands": 112, "age": 4},
    {"property_id": "House_67", "square_meters": 57, "price_thousands": 87, "age": 1},
    {"property_id": "House_68", "square_meters": 250, "price_thousands": 480, "age": 20},
    {"property_id": "House_69", "square_meters": 310, "price_thousands": 590, "age": 25},
    {"property_id": "House_70", "square_meters": 220, "price_thousands": 420, "age": 18},
    {"property_id": "House_71", "square_meters": 280, "price_thousands": 530, "age": 22},
    {"property_id": "House_72", "square_meters": 340, "price_thousands": 640, "age": 28},
    {"property_id": "House_73", "square_meters": 210, "price_thousands": 405, "age": 16},
    {"property_id": "House_74", "square_meters": 260, "price_thousands": 500, "age": 21},
    {"property_id": "House_75", "square_meters": 320, "price_thousands": 610, "age": 26},
    {"property_id": "House_76", "square_meters": 230, "price_thousands": 440, "age": 19},
    {"property_id": "House_77", "square_meters": 290, "price_thousands": 550, "age": 23},
    {"property_id": "House_78", "square_meters": 330, "price_thousands": 625, "age": 29},
    {"property_id": "House_79", "square_meters": 240, "price_thousands": 460, "age": 17},
    {"property_id": "House_80", "square_meters": 270, "price_thousands": 520, "age": 24},
    {"property_id": "House_81", "square_meters": 300, "price_thousands": 575, "age": 27},
    {"property_id": "House_82", "square_meters": 215, "price_thousands": 415, "age": 15},
    {"property_id": "House_83", "square_meters": 255, "price_thousands": 490, "age": 20},
    {"property_id": "House_84", "square_meters": 315, "price_thousands": 600, "age": 25},
    {"property_id": "House_85", "square_meters": 225, "price_thousands": 430, "age": 18},
    {"property_id": "House_86", "square_meters": 285, "price_thousands": 540, "age": 22},
    {"property_id": "House_87", "square_meters": 345, "price_thousands": 645, "age": 28},
    {"property_id": "House_88", "square_meters": 205, "price_thousands": 400, "age": 16},
    {"property_id": "House_89", "square_meters": 265, "price_thousands": 510, "age": 21},
    {"property_id": "House_90", "square_meters": 325, "price_thousands": 620, "age": 26},
    {"property_id": "House_91", "square_meters": 235, "price_thousands": 450, "age": 19},
    {"property_id": "House_92", "square_meters": 295, "price_thousands": 560, "age": 23},
    {"property_id": "House_93", "square_meters": 335, "price_thousands": 635, "age": 29},
    {"property_id": "House_94", "square_meters": 245, "price_thousands": 470, "age": 17},
    {"property_id": "House_95", "square_meters": 275, "price_thousands": 525, "age": 24},
    {"property_id": "House_96", "square_meters": 305, "price_thousands": 580, "age": 27},
    {"property_id": "House_97", "square_meters": 218, "price_thousands": 418, "age": 15},
    {"property_id": "House_98", "square_meters": 258, "price_thousands": 495, "age": 20},
    {"property_id": "House_99", "square_meters": 318, "price_thousands": 605, "age": 25},
    {"property_id": "House_100", "square_meters": 228, "price_thousands": 435, "age": 18}
]


def ApplyClusteringManualApp():
    data = GetData()

    x = [[propiedad["square_meters"], propiedad["price_thousands"], propiedad["age"]] for propiedad in data]

    scaler = StandardScaler()
    Xscaled = scaler.fit_transform(x)

    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    labels = model.fit_predict(Xscaled)

    result = []
    for i, propiedad in enumerate(data):
        row = propiedad.copy()
        row["Cluster"] = int(labels[i])
        result.append(row)

    clusterSummary = {}
    for label in labels:
        label = int(label)
        clusterSummary[label] = clusterSummary.get(label, 0) + 1

    #centers = model.cluster_centers_.tolist()

    #return {
    #    "result": result,
    #    "clusterSummary": clusterSummary,
    #    "centers": centers
    #}

    centers_scaled = model.cluster_centers_
     
    centers_original = scaler.inverse_transform(centers_scaled)
    centers = centers_original.tolist()
    return {
        "result": result,
        "clusterSummary": clusterSummary,
        "centers": centers,  # Ahora son valores reales (m², precios, edad)
        "centers_scaled": centers_scaled.tolist(),  # Opcional: centros normalizados
        "scaler_mean": scaler.mean_.tolist(),  # Opcional
        "scaler_scale": scaler.scale_.tolist()  # Opcional
    }
