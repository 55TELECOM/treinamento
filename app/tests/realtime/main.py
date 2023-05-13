import unittest
import sys
from HTMLTestRunner.runner import HTMLTestRunner
from app.tests.realtime.panel_detail import PanelDetailTestRealtime


if __name__ == '__main__':
    style = """
        .popup_window {
        overflow: scroll;
        }
    """

    suite = unittest.TestLoader().loadTestsFromTestCase(PanelDetailTestRealtime)

    runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                            open_in_browser=True, description="HTMLTestReport", tested_by="Ravikirana B",
                            add_traceback=False, style=style)
    runner.run(suite)
