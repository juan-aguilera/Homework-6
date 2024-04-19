import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import csv
from scipy.stats import shapiro

def read_csv(filename : str, encoding='utf-8') -> list[list]:
    my_list = []
    with open(filename, encoding=encoding) as infile:
        data = csv.reader(infile, delimiter=',')
        tittle =  next(data)
        for row in data:
            my_list.append(row)
    return my_list, tittle
def data_dictionary(col_a : str, col_b: str , col_c: str, col_d : str, my_list: list[list], tittles: list[str]) -> dict:
    index = [tittles.index(col_a)]
    index.append(tittles.index(col_b))
    index.append(tittles.index(col_c))
    index.append(tittles.index(col_d))
    data_dict = {}
    for i in index:
            data_dict[tittles[i]] =[]
    for i in index:
         for j in range(len(my_list)):
              if i == tittles.index(col_a):
                data_dict[tittles[i]].append(my_list[j][i])
              else:
                data_dict[tittles[i]].append(float(my_list[j][i]))
    return data_dict
def numeric_assignation(string_list:list[str]) -> dict :
     numbers_assignation = {}
     cnt = 1
     for i in string_list:
        if i not in numbers_assignation.keys():
            numbers_assignation[i] = cnt
            cnt += 1
     return numbers_assignation 
def string_to_number(data_dict, str_tittle, numbers_assignation : dict):
     number_list = []
     cnt = 0
     for i in data_dict[str_tittle]:
        data_dict[str_tittle][cnt] = numbers_assignation[i]
        cnt +=1
def plotting(data_list,data_name):
    #sns.kdeplot(data=data_list)
    sns.histplot(data_list, kde=True, stat="density", linewidth = 0,bins = 70)
    plt.xlabel('value')
    plt.ylabel('Frequency')
    plt.title(data_name)
    plt.show()
def shapiro_test(data_list):
    statistic, p = shapiro(data_list)
    return statistic,p
'''
def plotting(regions_dict,tittle):
    plt.figure(figsize =(10,6))

    for key,value in regions_dict.items():
        plt.plot(range(2014,2019),value, marker = "o", label = key)
    
    plt.title(tittle, fontsize=16)
    plt.xlabel("Year", fontsize = 12)
    plt.ylabel("Indicator Score", fontsize = 12)
    plt.xticks(range(2014,2018), fontsize = 10)
    plt.yticks(fontsize = 10)
    plt.legend(fontsize = 8 , loc = "best")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return plt
'''
#sns.histplot(data_list, kde=True, stat="density", linewidth = 0, bins=2)


if __name__ == "__main__":

    my_list, tittles = read_csv('20000_sample.csv')
    data_dict = data_dictionary('transporter','customer_business_premises', 'total_items', 'service_value', my_list, tittles)
    numbers_assignation = numeric_assignation(data_dict['transporter'])
    string_to_number(data_dict,'transporter',numbers_assignation)
    #plotting(data_dict['transporter'],'transporter')
    #plotting(data_dict['customer_business_premises'],'customer_business_premises')
    plotting(data_dict['total_items'],'total_items')
    #plotting(data_dict['service_value'], 'service value')
    #print(shapiro_test(data_dict['transporter']))

