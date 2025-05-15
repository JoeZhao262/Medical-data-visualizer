import unittest
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from medical_data_visualizer import draw_cat_plot, draw_heat_map

class CatPlotTestCase(unittest.TestCase):
    def test_cat_plot(self):
        fig = draw_cat_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure, "The function should return a matplotlib figure object.")
        self.assertTrue(len(fig.axes) > 0, "Figure should have at least one axis.")
        fig.savefig("catplot_test_output.png")

class HeatMapTestCase(unittest.TestCase):
    def test_heat_map(self):
        fig = draw_heat_map()
        self.assertIsInstance(fig, matplotlib.figure.Figure, "The function should return a matplotlib figure object.")
        self.assertTrue(len(fig.axes) > 0, "Figure should have at least one axis.")
        fig.savefig("heatmap_test_output.png")

if __name__ == "__main__":
    unittest.main()
