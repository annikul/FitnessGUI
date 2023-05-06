# TESTS FOR MODULE TIMETOOLS.PY

# Lets import module to be tested
import timetools

# UNIT TESTS DEFINITIONS

# Test if datediff function calculates correct and absolute values
def test_datediff():
    assert timetools.datediff('2023-04-28', '2023-04-10') == 18
    assert timetools.datediff('2023-04-10', '2023-04-28') == 18