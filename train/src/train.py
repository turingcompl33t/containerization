"""
Train a classifier.
"""

import sys
import pickle
import argparse
from typing import Tuple

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def parse_arguments() -> Tuple[str, str]:
    """
    Parse commandline arguments.
    :return: The path to the dataset, the path to which model is saved
    :rtype: Tuple[str, str]
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("ipath", type=str, help="The path to the training dataset.")
    parser.add_argument("opath", type=str, help="The path to which model parameters are saved.")
    args = parser.parse_args()
    return args.ipath, args.opath

def load_csv(path: str) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Load the CSV with training data from `path`.
    :param path: The path to the dataset
    :type path: str
    :return: The loaded dataset as a Pandas dataframe
    :rtype: Tuple[pd.DataFrame, pd.Series]
    """
    df = pd.read_csv(path)
    return df.iloc[:,:-1], df.iloc[:,-1]

def main() -> int:
    # Parse the data path
    ipath, opath = parse_arguments()
    
    # Load the dataset
    X, y = load_csv(ipath)
    
    # Train the classifier
    clf = DecisionTreeClassifier()
    clf.fit(X, y)

    # Save trained classifier
    with open(opath, "wb") as f:
        pickle.dump(clf, f)

    return 0

if __name__ == "__main__":
    sys.exit(main())
