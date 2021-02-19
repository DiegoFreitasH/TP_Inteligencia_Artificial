import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def logistic_function(x):
    return 1/(1+np.exp(x))

def logistic_regression(Y, X, alpha=0.01, num_of_iter=1000):
    
    W = np.random.uniform(size=X.shape[1])
  
    rows = X.shape[0]
    
    h = logistic_function

    for k in range(num_of_iter):
        
        grad = np.zeros(shape=W.shape)
        
        for i in range(len(grad)):
            y_h = h(np.dot(-X, W))

            erro = Y - y_h

            grad[i] += np.dot(erro, X[:,i]) * y_h[i] * (1 - y_h[i]) 
        
        grad *= alpha
        W += grad
    
    return W

def predict(Y, X, W):
    h = logistic_function

    predictions = h(np.dot(-X, W))
    predictions = np.where(predictions >= 0.5, 1, 0)
    
    return predictions
        
def normalize(X: np.ndarray):
    return (X - X.mean(axis=0))/ X.std(axis=0)


def main():
    path = "dataset/breast-cancer-wisconsin.data"
    header = [
        "Sample code number",
        "Clump Thickness",
        "Uniformity of Cell Size",
        "Uniformity of Cell Shape",
        "Marginal Adhesion",
        "Single Epithelial Cell Size",
        "Bare Nuclei",
        "Bland Chromatin",
        "Normal Nucleoli",
        "Mitoses",
        "Class"
    ]

    print("Loading dataset")
    dataset = pd.read_csv(path, names=header, na_values=["?"]).dropna()

    print("Defining X and Y")
    Y = dataset["Class"].to_numpy()
    Y = np.array(list(map(lambda x: (x-2)/2, Y)))

    X = dataset.drop(["Sample code number", "Class"], axis=1).to_numpy()
    X = normalize(X)
    X = np.concatenate([np.ones(shape=[X.shape[0], 1]), X], axis=1)

    print("Defining train and test samples")
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    print("Appling Logistic Regression")
    W = logistic_regression(y_train, x_train, alpha=0.01, num_of_iter=10**3)

    predictions = predict(y_test, x_test, W)
    print("Result of Test Samples:")
    print("  Acccuracy:", accuracy_score(y_test, predictions))
    print("  Precision:", precision_score(y_test, predictions))
    print("  Reacall:", recall_score(y_test, predictions))
    print("  F1 Score:", f1_score(y_test, predictions))

if __name__ == '__main__':
    main()