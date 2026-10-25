"""
Backward-compatibility test runner for state planner.
"""

from tests.test_planner import test_state_planner

def test_all_16_states():
    test_state_planner()

if __name__ == "__main__":
    test_all_16_states()
