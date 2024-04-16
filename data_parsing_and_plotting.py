import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import csv

def read_csv(filename, encoding='utf-8'):
    my_list = []
    with open(filename, encoding=encoding) as infile:
        data = csv.reader(infile, delimiter=',')
        #tittle = next(data)[1]
        for row in data:
            my_list.append(row)
        for row in my_list:
            print(row)

'''
def read_xlsx():
    df_dict = pd.read_excel('Environment_Social_and_Governance_(ESG)_Data final.xlsx', sheet_name=['Python Data'])
    df = df_dict['Python Data']
    col_list = df.columns
    data_dict = {}
    for i in range(len(col_list)):
        data_dict[col_list[i]] = df[col_list[i]].tolist()

    return data_dict
def delete_nan_values(data_series):
    data_dict = read_xlsx()
    table = []
    table.append(list(filter(lambda x: x != 'nan',data_dict['Region'])))
    table.append(list(filter(lambda x: x != 'nan',data_dict['Time'])))
    table.append(list(filter(lambda x: x != 'nan', data_dict['Country Name'])))
    table.append(list(filter(lambda x: x != 'nan', data_dict[data_series])))
    return table
def delete_empty_values(data_series):
    table = delete_nan_values(data_series)
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == '..':
                table[i][j] = 0
    return table

def country_agrupation(data_series):
    table = delete_empty_values(data_series)
    countries_dict = {}
    for i in range(len(table[2])):
        if table[2][i] not in countries_dict.keys():
            countries_dict[table[2][i]] = [table[0][i]]
            countries_dict[table[2][i]].append(table[3][i])
        else:
            countries_dict[table[2][i]].append(table[3][i])
    return countries_dict
def mean_calculation_by_country(data_series):
    country_dict = country_agrupation(data_series)
    for key,value in country_dict.items():
        country_dict[key].append(np.mean(list(filter(lambda x: x > 0, value[1:]))))
        #last position of each value is the mean of eight years of data (excluding 0 because 0 represents no data in the source file)
    return country_dict
def region_agrupation(data_series):
    countries_dict = mean_calculation_by_country(data_series)
    regions_dict = {}
    #regions dict creation
    for key,value in countries_dict.items():
        if value[0] not in regions_dict.keys():
            regions_dict[value[0]] = [[],[],[],[],[]]
    for key,value in countries_dict.items():
        for i in range(5):
            regions_dict[value[0]][i].append(value[i+1])
    for key,value in regions_dict.items():
        for i in range(len(value)):
            regions_dict[key][i] = np.mean(list(filter(lambda x: x >0,value[i])))
        #regions_dict[key] = np.mean(value)
    return regions_dict

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



if __name__ == "__main__":

    print(read_csv('20000_sample.csv', encoding='utf-8'))
    
    '''
    regions_dict_1 = region_agrupation('Economic and Social Rights Performance Score [SD.ESR.PERF.XQ]')
    plotting(regions_dict_1, tittle = 'Economic and Social Rights Performance Score evolution (2014-2018) per Región (2014-2018)')

    regions_dict_2 = region_agrupation('Access to electricity (% of population) [EG.ELC.ACCS.ZS]')
    plotting(regions_dict_2, tittle = 'Access to electricity (% of population) evolution (2014-2018) per Región')

    regions_dict_3 = region_agrupation('CO2 emissions (metric tons per capita) [EN.ATM.CO2E.PC]')
    plotting(regions_dict_3, tittle = 'CO2 emissions (metric tons per capita) evolution (2014-2018) per Region')
'''
   