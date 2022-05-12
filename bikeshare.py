import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
print('Hello! Let\'s explore some US bikeshare data!')
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    inputcityx=True
    while inputcityx:
        load_city=input('Which city do you like to analyse,Chicago,New York City,or Washington?')
        load_city = load_city.lower()
        if load_city in ("chicago","new york city","washington",):
            inputcityx=False
        else:
            print("Your input is wrong,please input again")
            continue
    # get user input for month (all, january, february, ... , june)
    inputmonthx=True
    while inputmonthx:
        load_month=input('Which month?January,February,March,April,May,June?Or you can input \'all\' to all of months.---')
        load_month = load_month.lower()
        if load_month in ("january","february","march","april","may","june","all" ):
            inputmonthx=False
        else:
            print("Your input is wrong,please input again")
            continue
    # get user input for day of week (all, monday, tuesday, ... sunday)
    inputdayx=True
    while inputdayx:
        load_day=input('Which day?Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday?Or you can input \'all\' to all of days.---')
        load_day = load_day.lower()
        if load_day in ("sunday","monday","tuesday","wednesday","thursday","friday","saturday","all"):
            inputdayx=False
        else:
            print("Your input is wrong,please input again")
            continue
    return load_city, load_month, load_day
def  load_date(load_city,load_month,load_day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[load_city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
    if load_month!='all':
        months=['january','february','march','april','may','june']
        load_month=months.index(load_month)+1
        df=df[df['month']==load_month]
    if load_day!='all':
        df=df[df['day_of_week']==load_day.title()]
    return df

def see_date(df):
    """Displays 5 lines data."""
    inputcitydt=True
    while inputcitydt:
        citydt=input('Do you want see 5 lines data for this city?Yes or No---')
        if citydt in  ("Yes","yes" ):
            print(df.sample(n=5))
            continue
        elif citydt in  ("No","no" ):
            break
        else:
            print("Your input is wrong,please input again")
            continue

def  pop_data(df):
    """Displays statistics on the most frequent times of travel."""
    popular_month = df['month'].mode()[0]
    counts_popmonth=df['Start Time'].dt.month.value_counts()[popular_month]
    popular_day = df['day_of_week'].mode()[0]
    counts_popday=df['Start Time'].dt.day_name().value_counts()[popular_day]
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    counts_hour=df['Start Time'].dt.hour.value_counts()[popular_hour]
    print("The most common month of this city is:",popular_month)
    print("and counts is:",counts_popmonth)
    print("The most common day of this city is:",popular_day)
    print("and counts is:",counts_popday)
    print('The most popular  hour is:',popular_hour)
    print('And most popular hour of counts is',counts_hour)
    print(df['Start Time'].dt.hour.value_counts().to_frame())

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('-'*40)
    print('And next,let\'s explore the station data!')
    common_start_station = df['Start Station'].value_counts()[0:1]
    print('The most common start station of this city is:', common_start_station)
    common_end_station  = df['End Station'].value_counts()[0:1]
    print('The most common end station of this city is:', common_end_station)
    common_start_end_station = (df['Start Station'] + df['End Station']).value_counts()[0:1]
    print('The most frequent combination of start station and end station trip of this city is:', common_start_end_station)

def trip_duration(df):
    """Displays statistics on the total and average trip duration."""
    print('-'*40)
    print('And next,let\'s explore the trip duration data!')
    total_travel = df['Trip Duration'].sum()
    print('The total travel time is:', total_travel)
    mean_travel = df['Trip Duration'].mean()
    print('The mean travel time is:', mean_travel)

def user_info(df,load_city):
    """Displays statistics on bikeshare users."""
    print('-'*40)
    print('And next,let\'s explore the user info data!')
    count_usertype = df['User Type'].value_counts()[0:3]
    print('The counts of each user type is:', count_usertype)
    while load_city in ("chicago","Chicago","new york city","New York City" ):
        input_gender=input('Do you want see gender data for this city?Yes or No---')
        if input_gender in  ("Yes","yes" ):
            count_gender=df['Gender'].value_counts()[0:3]
            print('The counts of each of gender is:',count_gender)
            break
        elif input_gender in  ("No","no" ):
            break
        else:
            print("Your input is wrong,please input again")
            continue
    while load_city in ("chicago","Chicago","new york city","New York City" ):
        input_birth=input('Do you want see birth data for this city?Yes or No---')
        if input_birth in  ("Yes","yes" ):
            common_birth=df['Birth Year'].mode()[0]
            print('The most common year of birth is:',common_birth)
            break
        elif input_birth in  ("No","no" ):
            break
        else:
            print("Your input is wrong,please input again")
            continue

def main():
    while True:
        load_city, load_month, load_day = get_filters()
        df = load_date(load_city, load_month, load_day)
        see_date(df)
        pop_data(df)
        station_stats(df)
        trip_duration(df)
        user_info(df,load_city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
