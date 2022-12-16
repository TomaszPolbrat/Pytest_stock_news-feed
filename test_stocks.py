from datetime import date   # imports date function from datetime library
import pytest   # imports pytest library


@pytest.mark.parametrize("curr_date, result",[("2022-12-03","It's weekend, relax. NY stock market"
    " is close."),("2022-12-04","It's weekend, relax. NY stock market is close.")])  # testing two different dates
# (Saturday and Sunday) with mark.parameters
def test_weekend(curr_date,result):  # testing case when program will be run on weekend
    split_date = curr_date.split("-")   # preparing date format
    if int(date(int(split_date[0]),int(split_date[1]),int(split_date[2])).weekday()) >= 5:  # if statement testing
        # current day of the week
        return result   # if it's Saturday or Sunday, return string
    assert test_weekend == result   # test if result  == return value


def test_alarm(stock_data_analysis):    # tests the analysis of stock main string title
    assert stock_data_analysis[0] == "Value of Tesla Inc dropped! 🔻-4.0%"


def test_news(stock_data_analysis):     # tests the news feed
    assert stock_data_analysis[1] == ["Twitter suspends bot account tracking Elon Musk's jet - Reuters",
                             "Panasonic agrees to supply EV batteries to Lucid Group - Reuters",
                             "Futures flat ahead of Fed's rate decision - Reuters"]
