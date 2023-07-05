# TESTS FOR MODULE TIMETOOLS.PY

# Lets import module to be tested
import timetools

# UNIT TESTS DEFINITIONS

# Test if datediff function calculates correct and absolute values
def test_datediff():
    assert timetools.datediff('2023-04-28', '2023-04-10') == 18
    assert timetools.datediff('2023-04-10', '2023-04-28') == 18

# Tälläisissa testeissä kannattaa laittaa joku round. Muuten testi ei välttämättä mene läpi. Pythonisssa on enempi desimaaleja kuin excelis
# Test if timediff function calculates correct and absolute values. 
def test_timediff():
    assert round(timetools.timediff('11:30:15', '10:10:05'), 4) == 1.3361
    assert round(timetools.timediff('10:10:05', '11:30:15'), 4) == 1.3361

# Test if dateTimeDiff works correctly
def test_dateTimeDiff():
    assert timetools.dateTimeDiff('2023-04-27 10:00:00', '2023-04-28 12:30:00') == 26.5


def test_datediff2():
    assert timetools.datediff2('2023-04-10', '2023-04-12', 'day') == 2  # Koska on 3 argumenttia day, monh, year.  
    assert timetools.datediff2('2023-04-10', '2023-06-09', 'month') == 2 # Kaikki pitää testata. Siksi on 3 eri testiä
    assert timetools.datediff2('2023-04-10', '2025-04-09', 'year') == 2
  

def test_timediff2():
    assert timetools.timediff2('10:00:00', '12:30:00', 'hour') == 2.5    # Koska on 3 argumenttia hour, minute, second. 
    assert timetools.timediff2('10:00:00', '12:30:00', 'minute') == 150  # Kaikki pitää testata. Siksi on 3 eri testiä
    assert timetools.timediff2('10:00:00', '12:30:00', 'second') == 9000

def test_dateTimeDiff2():
    assert round (timetools.dateTimeDiff2('2023-04-27 10:00:00', '2023-04-28 12:30:00', 'day'), 1) == 1.1
    assert timetools.dateTimeDiff2('2023-04-27 10:00:00', '2023-04-28 12:30:00', 'hour') == 26.5

# An example of function returning non numerical values
def test_finnisWeekdayOrder():

    # Name of the day is correct
    assert timetools.finnishWeekdayOrder('perjantai') =='perjantai on viikon 5. päivä'
    
    # Name of the day is typed incorrectly, get apropriate error message
    input_value = 'mantai'
    assert timetools.finnishWeekdayOrder(input_value) == f'{input_value} ei ole viikonpäivä, tarkista syötteesi'

    


