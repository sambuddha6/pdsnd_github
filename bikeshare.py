import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

list_of_month_short_name = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

list_of_day_name = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Would you like to see data for Chicago, New York City or Washington - Please enter full city name: ')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    invalidinput = False
    city = ''
    while city == '' or invalidinput:
        city = input()
        if city.upper() != 'CHICAGO' and city.upper() != 'NEW YORK CITY' and city.upper() != 'WASHINGTON':
            invalidinput = True
            print ('Oops - Invalid Input! Please enter Chicago, New York City or Washington - full city name:')
        else:
            invalidinput = False


    print('Now then - Would you like to filter data by month - if yes please enter first 3 characters of the month name (e.g. JAN) else please enter ALL: ')
    # TO DO: get user input for month (all, january, february, ... , june)
    invalidinput = False
    month = ''

    while month == '' or invalidinput:
        month = input()

        if month.upper() not in list_of_month_short_name and month.upper() != 'ALL':
            invalidinput = True
            print ('Oops - Invalid Input! Please enter first 3 characters of the month name (e.g. JAN) or ALL')
        else:
            invalidinput = False

    print('Great! Would you like to filter data by day of week - if yes please enter the full day name (e.g. SUNDAY) else please enter ALL: ')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    invalidinput = False
    day = ''

    while day == '' or invalidinput:
        day = input()

        if day.upper() not in list_of_day_name and day.upper() != 'ALL':
            invalidinput = True
            print ('Oops - Invalid Input! Please enter the full day name (e.g. SUNDAY) or ALL')
        else:
            invalidinput = False

    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month.lower() != 'all':
        # use the index of the months list to get the corresponding int
        month = list_of_month_short_name.index(month.upper()) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    print('Most common month: ' , list_of_month_short_name[int(df['month'].mode() - 1)])

    # TO DO: display the most common day of week
    most_frequest_week = df['day_of_week'].mode()[0]
    print('Most common day of week: ' , most_frequest_week)

    df2 = df[df['day_of_week'] == most_frequest_week]
    print('Number of times this particular week was chosen for trip: ' , df2.size)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_frequest_hour = df['hour'].mode()[0]
    print('Most common start hour: ' , most_frequest_hour)

    df3 = df[df['hour'] == most_frequest_hour]
    print('Number of times this particular hour was chosen for trip: ' , df3.size)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    if 'Start Station' in df.columns and 'End Station' in df.columns:
        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        # TO DO: display most commonly used start station
        most_frequest_start_station = df['Start Station'].mode()[0]
        print('Most commonly used start station: ' , df['Start Station'].mode()[0])

        df1 = df[df['Start Station'] == most_frequest_start_station]
        print('Number of times this particular start station was chosen for trip: ' , df1.size)

        # TO DO: display most commonly used end station
        most_frequest_end_station = df['End Station'].mode()[0]
        print('Most commonly used end station: ' , most_frequest_end_station)

        df2 = df[df['End Station'] == most_frequest_end_station]
        print('Number of times this particular end station was chosen for trip: ' , df2.size)

        # TO DO: display most frequent combination of start station and end station trip
        df['Start and End Station'] = df['Start Station'] + ' --> ' + df['End Station']

        most_frequest_trip = df['Start and End Station'].mode()[0]
        print('Most frequent combination of start station and end station trip: ' , most_frequest_trip)

        df3 = df[df['Start and End Station'] == most_frequest_trip]
        print('Number of times this particular trip has been completed: ' , df3.size)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    if 'Trip Duration' in df.columns:

        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # TO DO: display total travel time

        print('Total travel time (minutes): ' , df['Trip Duration'].sum()/60)

        # TO DO: display mean travel time
        print('Mean travel time (minutes): ' , df['Trip Duration'].mean()/60)

        print('Maximum travel time (minutes): ' , df['Trip Duration'].max()/60)
        print('Minimum travel time (minutes): ' , df['Trip Duration'].min()/60)
        print('Median travel time (minutes): ' , df['Trip Duration'].median()/60)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_types = df['User Type'].value_counts()
        print ('Counts of user types: ' , user_types)

    # TO DO: Display counts of gender
	# This check is necessary because currently the Washington.csv doesn't have the Gender column
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        null_count = df['Gender'].isnull().sum()
        print ('Counts of gender: ' , gender)
        print ('Count of null values in Gender column: ' , null_count)

    # TO DO: Display earliest, most recent, and most common year of birth
	# This check is necessary because currently the Washington.csv doesn't have the Birth Year column
    if 'Birth Year' in df.columns:
        min_birth_year = df['Birth Year'].min()
        max_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        null_count = df['Birth Year'].isnull().sum()

        print ('Earliest year of birth: ' , int(min_birth_year))
        print ('Most recent year of birth: ' , int(max_birth_year))
        print ('Most common year of birth: ' , int(most_common_birth_year))
        print ('Count of null values in Birth Year column: ' , null_count)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def individual_trip_details(df, startindex, endindex):
    print(df.iloc[startindex : endindex])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if df.empty:
            print('Oops! No Data found for the choices made - please try again')
        else:
            time_stats(df)
            time.sleep(5)
            station_stats(df)
            time.sleep(5)
            trip_duration_stats(df)
            time.sleep(5)
            user_stats(df)
            time.sleep(3)

            startindex = 0
            endindex = 5
            while True:
                individual_trip_data = input('\nWould you like to see individual trip details 5 rows at a time? Enter yes or no.\n')
                if individual_trip_data.lower() == 'yes':
                    if endindex > df.size:
                        endindex = df.size
                    individual_trip_details(df, startindex, endindex)
                    startindex = endindex
                    endindex += 5
                else:
                    break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thats all for now - have a great day!')
            break


if __name__ == "__main__":
	main()
