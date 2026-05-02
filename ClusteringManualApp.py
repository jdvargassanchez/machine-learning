from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def GetData():
    return [
        {"id_propiedad": "Casa_1", "metros2": 120, "precio_miles": 210, "antiguedad": 12},
        {"id_propiedad": "Casa_2", "metros2": 145, "precio_miles": 260, "antiguedad": 9},
        {"id_propiedad": "Casa_3", "metros2": 160, "precio_miles": 310, "antiguedad": 14},
        {"id_propiedad": "Casa_4", "metros2": 115, "precio_miles": 195, "antiguedad": 10},
        {"id_propiedad": "Casa_5", "metros2": 175, "precio_miles": 340, "antiguedad": 11},
        {"id_propiedad": "Casa_6", "metros2": 130, "precio_miles": 225, "antiguedad": 15},
        {"id_propiedad": "Casa_7", "metros2": 150, "precio_miles": 280, "antiguedad": 8},
        {"id_propiedad": "Casa_8", "metros2": 165, "precio_miles": 320, "antiguedad": 13},
        {"id_propiedad": "Casa_9", "metros2": 105, "precio_miles": 185, "antiguedad": 9},
        {"id_propiedad": "Casa_10", "metros2": 140, "precio_miles": 250, "antiguedad": 11},
        {"id_propiedad": "Casa_11", "metros2": 155, "precio_miles": 290, "antiguedad": 12},
        {"id_propiedad": "Casa_12", "metros2": 125, "precio_miles": 215, "antiguedad": 10},
        {"id_propiedad": "Casa_13", "metros2": 170, "precio_miles": 330, "antiguedad": 14},
        {"id_propiedad": "Casa_14", "metros2": 135, "precio_miles": 240, "antiguedad": 8},
        {"id_propiedad": "Casa_15", "metros2": 148, "precio_miles": 275, "antiguedad": 15},
        {"id_propiedad": "Casa_16", "metros2": 162, "precio_miles": 305, "antiguedad": 11},
        {"id_propiedad": "Casa_17", "metros2": 118, "precio_miles": 200, "antiguedad": 13},
        {"id_propiedad": "Casa_18", "metros2": 152, "precio_miles": 285, "antiguedad": 9},
        {"id_propiedad": "Casa_19", "metros2": 178, "precio_miles": 345, "antiguedad": 12},
        {"id_propiedad": "Casa_20", "metros2": 122, "precio_miles": 210, "antiguedad": 10},
        {"id_propiedad": "Casa_21", "metros2": 142, "precio_miles": 255, "antiguedad": 14},
        {"id_propiedad": "Casa_22", "metros2": 168, "precio_miles": 325, "antiguedad": 8},
        {"id_propiedad": "Casa_23", "metros2": 132, "precio_miles": 230, "antiguedad": 11},
        {"id_propiedad": "Casa_24", "metros2": 158, "precio_miles": 295, "antiguedad": 15},
        {"id_propiedad": "Casa_25", "metros2": 128, "precio_miles": 220, "antiguedad": 12},
        {"id_propiedad": "Casa_26", "metros2": 172, "precio_miles": 335, "antiguedad": 9},
        {"id_propiedad": "Casa_27", "metros2": 146, "precio_miles": 265, "antiguedad": 13},
        {"id_propiedad": "Casa_28", "metros2": 112, "precio_miles": 190, "antiguedad": 10},
        {"id_propiedad": "Casa_29", "metros2": 164, "precio_miles": 315, "antiguedad": 14},
        {"id_propiedad": "Casa_30", "metros2": 138, "precio_miles": 245, "antiguedad": 11},
        {"id_propiedad": "Casa_31", "metros2": 156, "precio_miles": 285, "antiguedad": 8},
        {"id_propiedad": "Casa_32", "metros2": 126, "precio_miles": 215, "antiguedad": 15},
        {"id_propiedad": "Casa_33", "metros2": 174, "precio_miles": 340, "antiguedad": 12},
        {"id_propiedad": "Casa_34", "metros2": 144, "precio_miles": 260, "antiguedad": 9},
        {"id_propiedad": "Casa_35", "metros2": 65, "precio_miles": 95, "antiguedad": 2},
        {"id_propiedad": "Casa_36", "metros2": 85, "precio_miles": 140, "antiguedad": 4},
        {"id_propiedad": "Casa_37", "metros2": 55, "precio_miles": 85, "antiguedad": 1},
        {"id_propiedad": "Casa_38", "metros2": 75, "precio_miles": 120, "antiguedad": 3},
        {"id_propiedad": "Casa_39", "metros2": 88, "precio_miles": 145, "antiguedad": 5},
        {"id_propiedad": "Casa_40", "metros2": 60, "precio_miles": 90, "antiguedad": 2},
        {"id_propiedad": "Casa_41", "metros2": 80, "precio_miles": 130, "antiguedad": 4},
        {"id_propiedad": "Casa_42", "metros2": 70, "precio_miles": 110, "antiguedad": 1},
        {"id_propiedad": "Casa_43", "metros2": 52, "precio_miles": 82, "antiguedad": 3},
        {"id_propiedad": "Casa_44", "metros2": 82, "precio_miles": 135, "antiguedad": 5},
        {"id_propiedad": "Casa_45", "metros2": 68, "precio_miles": 105, "antiguedad": 2},
        {"id_propiedad": "Casa_46", "metros2": 78, "precio_miles": 125, "antiguedad": 4},
        {"id_propiedad": "Casa_47", "metros2": 58, "precio_miles": 88, "antiguedad": 1},
        {"id_propiedad": "Casa_48", "metros2": 86, "precio_miles": 142, "antiguedad": 3},
        {"id_propiedad": "Casa_49", "metros2": 62, "precio_miles": 92, "antiguedad": 5},
        {"id_propiedad": "Casa_50", "metros2": 72, "precio_miles": 115, "antiguedad": 2},
        {"id_propiedad": "Casa_51", "metros2": 84, "precio_miles": 138, "antiguedad": 4},
        {"id_propiedad": "Casa_52", "metros2": 54, "precio_miles": 84, "antiguedad": 1},
        {"id_propiedad": "Casa_53", "metros2": 76, "precio_miles": 122, "antiguedad": 3},
        {"id_propiedad": "Casa_54", "metros2": 66, "precio_miles": 100, "antiguedad": 5},
        {"id_propiedad": "Casa_55", "metros2": 89, "precio_miles": 148, "antiguedad": 2},
        {"id_propiedad": "Casa_56", "metros2": 64, "precio_miles": 96, "antiguedad": 4},
        {"id_propiedad": "Casa_57", "metros2": 74, "precio_miles": 118, "antiguedad": 1},
        {"id_propiedad": "Casa_58", "metros2": 56, "precio_miles": 86, "antiguedad": 3},
        {"id_propiedad": "Casa_59", "metros2": 81, "precio_miles": 132, "antiguedad": 5},
        {"id_propiedad": "Casa_60", "metros2": 61, "precio_miles": 91, "antiguedad": 2},
        {"id_propiedad": "Casa_61", "metros2": 79, "precio_miles": 128, "antiguedad": 4},
        {"id_propiedad": "Casa_62", "metros2": 69, "precio_miles": 108, "antiguedad": 1},
        {"id_propiedad": "Casa_63", "metros2": 51, "precio_miles": 81, "antiguedad": 3},
        {"id_propiedad": "Casa_64", "metros2": 83, "precio_miles": 136, "antiguedad": 5},
        {"id_propiedad": "Casa_65", "metros2": 63, "precio_miles": 94, "antiguedad": 2},
        {"id_propiedad": "Casa_66", "metros2": 73, "precio_miles": 112, "antiguedad": 4},
        {"id_propiedad": "Casa_67", "metros2": 57, "precio_miles": 87, "antiguedad": 1},
        {"id_propiedad": "Casa_68", "metros2": 250, "precio_miles": 480, "antiguedad": 20},
        {"id_propiedad": "Casa_69", "metros2": 310, "precio_miles": 590, "antiguedad": 25},
        {"id_propiedad": "Casa_70", "metros2": 220, "precio_miles": 420, "antiguedad": 18},
        {"id_propiedad": "Casa_71", "metros2": 280, "precio_miles": 530, "antiguedad": 22},
        {"id_propiedad": "Casa_72", "metros2": 340, "precio_miles": 640, "antiguedad": 28},
        {"id_propiedad": "Casa_73", "metros2": 210, "precio_miles": 405, "antiguedad": 16},
        {"id_propiedad": "Casa_74", "metros2": 260, "precio_miles": 500, "antiguedad": 21},
        {"id_propiedad": "Casa_75", "metros2": 320, "precio_miles": 610, "antiguedad": 26},
        {"id_propiedad": "Casa_76", "metros2": 230, "precio_miles": 440, "antiguedad": 19},
        {"id_propiedad": "Casa_77", "metros2": 290, "precio_miles": 550, "antiguedad": 23},
        {"id_propiedad": "Casa_78", "metros2": 330, "precio_miles": 625, "antiguedad": 29},
        {"id_propiedad": "Casa_79", "metros2": 240, "precio_miles": 460, "antiguedad": 17},
        {"id_propiedad": "Casa_80", "metros2": 270, "precio_miles": 520, "antiguedad": 24},
        {"id_propiedad": "Casa_81", "metros2": 300, "precio_miles": 575, "antiguedad": 27},
        {"id_propiedad": "Casa_82", "metros2": 215, "precio_miles": 415, "antiguedad": 15},
        {"id_propiedad": "Casa_83", "metros2": 255, "precio_miles": 490, "antiguedad": 20},
        {"id_propiedad": "Casa_84", "metros2": 315, "precio_miles": 600, "antiguedad": 25},
        {"id_propiedad": "Casa_85", "metros2": 225, "precio_miles": 430, "antiguedad": 18},
        {"id_propiedad": "Casa_86", "metros2": 285, "precio_miles": 540, "antiguedad": 22},
        {"id_propiedad": "Casa_87", "metros2": 345, "precio_miles": 645, "antiguedad": 28},
        {"id_propiedad": "Casa_88", "metros2": 205, "precio_miles": 400, "antiguedad": 16},
        {"id_propiedad": "Casa_89", "metros2": 265, "precio_miles": 510, "antiguedad": 21},
        {"id_propiedad": "Casa_90", "metros2": 325, "precio_miles": 620, "antiguedad": 26},
        {"id_propiedad": "Casa_91", "metros2": 235, "precio_miles": 450, "antiguedad": 19},
        {"id_propiedad": "Casa_92", "metros2": 295, "precio_miles": 560, "antiguedad": 23},
        {"id_propiedad": "Casa_93", "metros2": 335, "precio_miles": 635, "antiguedad": 29},
        {"id_propiedad": "Casa_94", "metros2": 245, "precio_miles": 470, "antiguedad": 17},
        {"id_propiedad": "Casa_95", "metros2": 275, "precio_miles": 525, "antiguedad": 24},
        {"id_propiedad": "Casa_96", "metros2": 305, "precio_miles": 580, "antiguedad": 27},
        {"id_propiedad": "Casa_97", "metros2": 218, "precio_miles": 418, "antiguedad": 15},
        {"id_propiedad": "Casa_98", "metros2": 258, "precio_miles": 495, "antiguedad": 20},
        {"id_propiedad": "Casa_99", "metros2": 318, "precio_miles": 605, "antiguedad": 25},
        {"id_propiedad": "Casa_100", "metros2": 228, "precio_miles": 435, "antiguedad": 18}
    ]

def ApplyClusteringManualApp():
    data = GetData()

    x = [[propiedad["metros2"], propiedad["precio_miles"], propiedad["antiguedad"]] for propiedad in data]
    
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
        
    centers = model.cluster_centers_.tolist()

    return {
        "result": result,
        "clusterSummary": clusterSummary,
        "centers": centers
    }