import unittest
import data_parsing_and_plotting
import math 
import matplotlib.pyplot as plt

class AlgorithmsTests(unittest.TestCase):
    n = "CO2 emissions (metric tons per capita) [EN.ATM.CO2E.PC]"
    def test_read(self):
            result = data_parsing_and_plotting.read_xlsx()
            self.assertIsInstance(result, dict)
    def test_delete_nan_values(self):
            result = data_parsing_and_plotting.delete_nan_values(self.n)
            self.assertIsInstance(result,list)
            for i in result:
                self.assertIsInstance(i, list)
                if all(isinstance(x,float) for x in i):
                        self.assertTrue(any(math.isnan(x) for x in i), "Hay valores nan")
    def test_delete_empty_values(self):
            result = data_parsing_and_plotting.delete_empty_values(self.n)
            self.assertIsInstance(result,list)
            for i in result:
                  self.assertIsInstance(i,list)
                  self.assertTrue(all(x != ".." for x in i ), "Hay celdas vacias")
    def test_country_agrupation(self):
            result = data_parsing_and_plotting.country_agrupation(self.n)
            self.assertIsInstance(result,dict)
    def test_mean_calculation(self):
            result = data_parsing_and_plotting.mean_calculation_by_country(self.n)
            self.assertIsInstance(result,dict)
    def test_region_agrupation(self):
            result = data_parsing_and_plotting.region_agrupation(self.n)
            self.assertIsInstance(result,dict)
'''
    def test_is_plot_figure(self):
            regions_dict = data_parsing_and_plotting.region_agrupation(self.n)
            result = data_parsing_and_plotting.plotting(regions_dict,self.n)
            self.assertIsInstance(result,plt.Figure)
'''
if __name__ == "__main__":
   unittest.main()
