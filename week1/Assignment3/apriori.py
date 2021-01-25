
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# This method will model the apriori algorithm so it can return the values that have enough confidence

def apriorimodel(support):
    #Takes the support percentage as a parameter
    records = []
    data = pd.read_excel('RetailData.xlsx',header=None,usecols="A,C")
    for i in range(0, len(data) - 1):
        records.append([str(data.values[i,j]) for j in range(0, len(data) - 1)])
    association_rules = apriori(data, min_support=support)
    association_results = list(association_rules)
    return association_rules

def main():
# Loading the Data
    f = open("itemset.txt", "a")
    f.write(apriorimodel(.01))
    f.write(apriorimodel(.05))
    f.write(apriorimodel(.10))
    f.write(apriorimodel(.20))
    f.write(apriorimodel(.30))
    f.close()
    #print record

if __name__ == "__main__":
    main()
