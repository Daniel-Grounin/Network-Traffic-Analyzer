import unittest
from gui.dashboard import Dashboard

class TestDashboard(unittest.TestCase):
    def test_window_title(self):
        dashboard = Dashboard()
        self.assertEqual(dashboard.windowTitle(), "Network Traffic Analyzer")
