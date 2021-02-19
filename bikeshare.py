import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

ANALYSE_CITIES = ['chicago', 'new york', 'washington']

ANALYSE_MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

ANALYSE_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    while True:
       city = input('Please input name of the city you wish to analyze (either chicago, new york or washington? \n> ').lower()
       if city in ANALYSE_CITIES:
           break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please input month you wish to analyze \n> ').lower()
        if month in ANALYSE_MONTHS:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please input day you wish to analyze \n> ').lower()
        if day in ANALYSE_DAYS:
            break

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
    #print(city,month,day)
           
    df = pd.read_csv(CITY_DATA[city]) #read df
    
    df['Start Time'] = pd.to_datetime(df['Start Time']) #convert start time to datetime
    
    df['month'] = df['Start Time'].dt.month
    
    df['day of week'] = df['Start Time'].dt.weekday_name
    
    df['hour'] = df['Start Time'].dt.hour


    month = ANALYSE_MONTHS.index(month) #filter by month
    df = df.loc[df['month'] == month] #generates new df
    
    
    #day = ANALYSE_DAYS.index(day)   
    df = df.loc[df['day of week'] == day.title()]
    
    return df


def time_stats(df):


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print('Most common month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day of week'].value_counts().idxmax()
    print('Most commond day:', most_common_day)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print('Most common start hour:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_startstation = df['Start Station'].value_counts().idxmax()
    print('most common startstation =', most_common_startstation)

    # TO DO: display most commonly used end station
    most_common_endstation = df['End Station'].value_counts().idxmax()
    print('Most common end station =', most_common_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_sest = df[['Start Station', 'End Station']].mode().loc[0]
    print("most common start and end station: {}, {}".format(most_common_sest[0], most_common_sest[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time in hours=', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time in hours = ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usertype_count = df['User Type'].value_counts()
    print('How many user typess:', usertype_count)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('How many genders:', gender_count)
    
    except KeyError:
        print('Gender does not exist for your selected variable')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        birthyear = df['Birth Year']
        
        birthyear_earliest = birthyear.min()
        print('the earliest birth year =', birthyear_earliest)

        birthyear_recent = birthyear.max()
        print('the most recent birth year:', birthyear_recent) 

        birthyear_common = birthyear.value_counts().idxmax()
        print('the most common birth year:', birthyear_common)
        
    except KeyError:
        print('birth year does not exist for your selected variable')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def aks_view(df):

    print(df.head())
    start_loc = 0
    while True:
        view_data = input('\nWould you like to view 5 row of trip data? yes or no?\n')
        if view_data.lower() != 'yes':
            return
        start_loc = start_loc + 5
        print(df.iloc[start_loc:start_loc+5])
	
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            view_data = input('\nWould you like to view 5 row of trip data? yes or no?\n')
            if view_data.lower() != 'yes':
                break
            aks_view(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
