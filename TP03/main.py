import pandas as pd

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
    dataset = pd.read_csv(path, names=header, na_values=["?"])
    print(dataset.info())

if __name__ == '__main__':
    main()