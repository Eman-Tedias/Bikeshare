import pandas as pd
import numpy as np
import time

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

def filters(city='', month='', day=''):
    global cities
    cities = ['chicago', 'new york city', 'washington']
    city = str(input('What city do you want to check data from? (Chicago, New York City or Washington): ')).lower()
    while city not in cities:
        city = str(input('Invalid city name, please choose one of the list (Chicago, New York City or Washington): ')).lower()
    global months
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month =  month = str(input('What month do you want to check data from? \nFrom January to June or press \"all" to get information from all months: ')).lower()
    while month not in months:
        month = month = str(input('Invalid value, please choose one month from January to June or press \"all" to get information from all months: ')).lower()
    global dow
    dow = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    day = str(input('What day of week do you want to check data from? \nPress \"all\" to get information from all days of the week: ')).lower()
    while day not in dow:
        day = str(input('Invalid day of week, please type a correct value or press \"all\" to get information from all days of week: ')).lower()
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    if month != 'all':
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day.title()]
    return df

def time_stats(df):
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['months'] = df['Start Time'].month
    common_month = df['months'].mode()
    common_month = months[common_month[0]-1].title()
    print(f'\nThe most common month is: \n\n{common_month}\n\n')
    print('-='*20)
    df['dow'] = df['Start Time'].dt.day_name()
    common_dow = df['dow'].mode()[0]
    print(f'\nThe most common day of week is: \n\n{common_dow}\n\n')
    print('-='*20)
    df['hours'] = df['Start Time'].dt.hour
    common_hour = df['hours'].mode()[0]
    print(f'\nThe most common starting hour is: \n\n{common_hour}\n\n')
    print('=='*20)

def station_stats(df):
    most_common_start = df['Start Station'].mode()[0]
    print(f'\nThe most commonly used start station is: \n\n{most_common_start}\n\n')
    print('-='*20)
    most_common_end = df['End Station'].mode()[0]
    print(f'The most commonly used end station is: \n\n{most_common_end}\n\n')
    print('-='*20)
    df['Combined Station'] = df['Start Station'] + ' and ' + df['End Station']
    most_common_comb = df['Combined Station'].mode()[0]
    print(f'The most frequently used combination of start and end station trips are: \n\n{most_common_comb}\n\n')
    print('=='*20)

def trip_duration_stats(df):
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = int(total_travel_time/60)
    print(f'The total travel time is: \n\n{total_travel_time} minutes\n\n')
    print('-='*20)

    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time = int(mean_travel_time/60)
    print(f'The mean travel time is: \n\n{mean_travel_time} minutes\n\n')
    print('=='*20)

def user_stats(df):
    user_count = df.groupby('User Type').count()
    print('\nUser types:\n\n')
    for name, data in user_count.iteritems():
        print(f'{name} = {data}\n')
    print('-='*20)
    if 'Gender' in df:
        gender_count = df.groupby('Gender').sum()
    print('\nTotal users by gender:\n\n')
    for name, data in gender_count.iteritems():
        print(f'{name} = {data}\n')
    print('-='*20)
    if 'Birth Year' in df:
        earliest_birth = int(df['Birth Year']).min()
        recent_birth = int(df['Birth Year']).max()
        most_common_year = int(df['Birth Year']).mode()[0]
        print(f'\nEarliest year of birth: \n\n{earliest_birth}\n\n')
        print('-='*20)
        print(f'\nMost recent year of birth: \n\n{recent_birth}\n\n')
        print('-='*20)
        print(f'\nMost common year of birth: \n\n{most_common_year}\n\n')
        print('=='*20)

def main():
    while True:
        city, month, day = filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        restart = str(input('\nWould you like to restart? Enter yes or no.\n')).lower()
        while restart not in 'yesno' or len(restart) < 1:
            restart = str(input('\nSorry, I didn\'nt understand...\nWould you like to restart? Enter yes or no.\n')).lower()
        if restart in 'no':
            break

if __name__ == "__main__":
    main()