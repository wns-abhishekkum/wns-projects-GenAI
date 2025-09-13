import pandas as pd
from app import model_utils

if __name__ == '__main__':
    # Example: use a CSV file data/sample.csv with columns text,label
    df = pd.read_csv('data/sample.csv')
    report = model_utils.train_from_dataframe(df, algorithm='svm')
    print('Training complete. Report:')
    print(report)
