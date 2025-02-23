classes={
    'car':0,
    'fish':1,
    'house':2,
    'tree':3,
    'bicycle':4,
    'guitar':5,
    'pencil':6,
    'clock':7
}

def readFeatureFile(filePath):
    f=open(filePath,'r')
    lines=f.readlines()

    x=[]
    y=[]

    for i in range(1,len(lines)):
        row = lines[i].split(",")
        x.append(
            [float(row[j]) for j in range(len(row)-1)]
        )
        y.append(classes[row[-1].strip()])
    return x,y

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(
    n_neighbors=5,
    algorithm="brute",
    weights="distance"
)

x,y=readFeatureFile('../data/dataset/training.csv')
print(x,y)
knn.fit(x,y)

x,y = readFeatureFile('../data/dataset/testing.csv')
print(len(x),len(y))
accuracy=knn.score(x,y)

print("Accuracy:",accuracy)