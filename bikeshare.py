from _ast import mod

import pandas as pd
import numpy as np
from datetime import datetime as dt
import time




# import DateTime
from numpy.core.tests.test_scalarinherit import C

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    c = True
    m = True
    d = True
    while c or m or d  :
        cities = ['chicago', 'new york city', 'washington']
        city = str(input('Chose the city name(chicago, new york city, washington) : ').lower())
        cities = ['chicago', 'new york city', 'washington']
        if city in cities:
            c=False
            print(city)
        else:
            print('Wrong city enterd ')



    # TO DO: get user input for month (all, january, february, ... , june)
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
              'november',
              'december', 'all']
        month = str((input('choose month from (all, january, february, ... , june)) : ').lower()))
        if month in months:
            m = False
            print(month)
        else:
            print('Wrong month enterd ')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
            'sunday', 'all']
        day = str((input('choose day from ((all, monday, tuesday, ... sunday)) : ').lower()))
        if day in days:
            d = False
            print(day)
        else:
            print('Wrong day enterd ')
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load the city data
    df = pd.read_csv(CITY_DATA[city])
     #     seprate start time to month,day
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())
    if month != 'all' :
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                  'november','december', ]
        month = months.index(month) + 1
        df = df.loc[df['month'] == month, :]
    if day != 'all' :
        df = df.loc[df['day_of_week'] == day, :]

    return df


def time_stats(df, month,day):
    """Displays statistics on the most frequent times of travel."""

    print( '\nCalculating The Most Frequent Times of Travel...\n' )
    start_time = time.time()

    # TO DO: display the most common month
    if(month == 'all'):
        mon = df['month'].value_counts().idxmax()
        print ("the most common month is "+ str(mon))
    else :
        print('the df just have 1 month : '+ str(month))
    # TO DO: display the most common day of week
    if(day == 'all'):
        d = df['day_of_week'].value_counts().idxmax()
        print('the most common day of week is '+ str(d))
    else:
        print(' the df just have 1 day : ' + str(day))

    # TO DO: display the most common start hour

    hour = int (df['Start Time'].dt.hour.mode())
    print(' the most common start hour : ' + str(hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40 )



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    SS = df['Start Station'].value_counts().idxmax()
    print('most commonly used start station' + str(SS))

    # TO DO: display most commonly used end station
    ES = df['End Station'].value_counts().idxmax()
    print('most commonly used End station' + str(ES))
    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_trip = df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most frequent combination of start station and end station trip : '+ str(most_frequent_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip = df['Trip Duration'].sum()
    print(trip)
    # TO DO: display mean travel time
    trip = np.mean(df['Trip Duration'])
    print(trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The df counts of user types  : '+ str(df['User Type'].value_counts()))
    # TO DO: Display counts of gender
    if city != 'washington':
        gender = df.groupby(['Gender']).size()
        print(gender)
    else:
        print('washington city does not have the Gender data .')
    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        eariest = df['Birth Year'].min()
        most = df['Birth Year'].value_counts().idxmax()
        recent = df['Birth Year'].max()
        print('the earliest year of birth : '+str(eariest))
        print('the most recent year of birth : ' + str(recent))
        print('the most most common year of birth : ' + str(most))

    else:
        print('washington city does not have the Birth Date data .')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display(df) :
    data = str(input('Input Yes to print 5 rows of data : ').lower())
    start = 0
    end = 5
    if data == 'yes':
        while True:
            print(df.iloc[start:end])
            start +=5
            end+=5
            if str(input('Input Exit to quit : ').lower()) == 'exit':
                break

def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df , month , day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
