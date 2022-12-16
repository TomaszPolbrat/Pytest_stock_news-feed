# conftest file that aggregate all the fixture data
import pytest  # import pytest for @pytest.fixture
from json_data_stocks import stock_data_json    # import stock data
from json_news_data import news_json        # import news data

# 1st fixture, company name string
@pytest.fixture
def COMPANY_NAME():
    COMPANY_NAME = "Tesla Inc"
    return COMPANY_NAME

# 2nd fixture, stock data in json format
@pytest.fixture
def sixtymin_points():
    sixtymin_points = stock_data_json
    return sixtymin_points

#  3rd fixture, news data in json format
@pytest.fixture
def all_news():
    all_news = news_json
    return all_news

# 4th fixture, current day date as a string
@pytest.fixture
def today_date_time():
    today_date_time = "2022-12-13 20:00:00"
    return today_date_time

# 5th fixture, yesterday date as a string
@pytest.fixture
def yesterday_date_time():
    yesterday_date_time = "2022-12-12 20:00:00"
    return yesterday_date_time

# pytest fixture that will be used in tests
@pytest.fixture
def stock_data_analysis(sixtymin_points, all_news, today_date_time, yesterday_date_time, COMPANY_NAME):  # import data
    # from fixtures above
    today_close = float(sixtymin_points[today_date_time]["4. close"])       # takes float value of stock index
    yesterday_close = float(sixtymin_points[yesterday_date_time]["4. close"])   # takes float value of stock index
    one_day_delta = (((today_close - yesterday_close) / yesterday_close) * 100.).__round__(2)   # returns % of
    # difference between today's and yesterday's index value
    list1 = []      # empty list for news feed test
    if one_day_delta > 0:   # if index value rose, create string tittle message and find 3 news feed why
        alarm = f"We got a rise of {COMPANY_NAME}! 🔺{one_day_delta}%"
        for news in range(3):
            news_title = all_news[news]["title"]
            list1.append(news_title)
        return alarm, list1
    else:      # if index value fell, create string tittle message and find 3 news feed why
        alarm = f"Value of {COMPANY_NAME} dropped! 🔻{one_day_delta}%"
        for news in range(3):
            news_title = all_news[news]["title"]
            list1.append(news_title)
        return alarm, list1
