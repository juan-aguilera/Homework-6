import matplotlib.pyplot as plt 
import seaborn as sns
import csv
from scipy.stats import shapiro

def read_csv(filename : str, encoding='utf-8') -> list[list]:
    my_list = []
    with open(filename, encoding=encoding) as infile:
        data = csv.reader(infile, delimiter=',')
        title =  next(data)
        for row in data:
            my_list.append(row)
    return my_list, title
def data_dictionary(col_a : str, col_b: str , col_c: str, col_d : str, my_list: list[list], titles: list[str]) -> dict:
    index = [titles.index(col_a)]
    index.append(titles.index(col_b))
    index.append(titles.index(col_c))
    index.append(titles.index(col_d))
    data_dict = {}
    for i in index:
            data_dict[titles[i]] =[]
    for i in index:
         for j in range(len(my_list)):
              if i == titles.index(col_a):
                data_dict[titles[i]].append(my_list[j][i])
              else:
                data_dict[titles[i]].append(float(my_list[j][i]))
    return data_dict
def numeric_assignation(string_list:list[str]) -> dict :
     numbers_assignation = {}
     cnt = 1
     for i in string_list:
        if i not in numbers_assignation.keys():
            numbers_assignation[i] = cnt
            cnt += 1
     return numbers_assignation 
def string_to_number(data_dict: dict , str_title: str, numbers_assignation : dict) -> None:
     number_list = []
     cnt = 0
     for i in data_dict[str_title]:
        data_dict[str_title][cnt] = numbers_assignation[i]
        cnt +=1
def plotting(data_list: list ,data_name: str)->None:
    #sns.kdeplot(data=data_list)
    sns.histplot(data_list, kde=True, stat="density", linewidth = 0)
    plt.xlabel('value')
    plt.ylabel('Frequency')
    plt.title(data_name)
    plt.show()
def shapiro_test(data_list:list):
    statistic, p = shapiro(data_list)
    return statistic,p


if __name__ == "__main__":

    my_list, titles = read_csv('20000_sample.csv')
    data_dict = data_dictionary('transporter','customer_business_premises', 'total_items', 'service_value', my_list, titles)
    numbers_assignation = numeric_assignation(data_dict['transporter'])
    string_to_number(data_dict,'transporter',numbers_assignation)
    plotting(data_dict['transporter'],'transporter')
    plotting(data_dict['customer_business_premises'],'customer_business_premises')
    plotting(data_dict['total_items'],'total_items')
    plotting(data_dict['service_value'], 'service value')


