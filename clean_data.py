 
import pandas as pd
from steps.clean import Cleaner

cleaner = Cleaner()

train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

cleaner.clean_data(train).to_csv("data/train_clean.csv", index=False)
cleaner.clean_data(test).to_csv("data/test_clean.csv", index=False)

print("Data cleaning completed successfully.")
