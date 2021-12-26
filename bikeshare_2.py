import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = ''
    while(city not in CITY_DATA):
        city = input("enter one city from these three (chicago, new york city, washington) ?").lower()
        print(city)

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = ''
    while month not in months:
        month = input("enter a month from january to june, or you can type 'all' if you don't want any month filter?").lower()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday']
    day = ''
    while day not in days:
        day = input("enter a day of the week, or you can type 'all' if you don't want any day filter ?").lower()
        
    print("\n\nyou have chosen city = {} as name of the city to analyze, in addition to these two values:\n month = {},"
          "day = {} to filter by\n".format(city, month, day))

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    commonMonth = df['month'].mode()[0]
    print("The most common month is:",commonMonth)

    # TO DO: display the most common day of week
    commonDay = df['Start Time'].dt.day_name().mode()[0]
    print("The most common day of week is :",commonDay)

    # TO DO: display the most common start hour
    commonHour = df['Start Time'].dt.hour.mode()[0]
    print("The most common start hour is:",commonHour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonSs = df['Start Station'].mode()[0]
    print("Most commonly used start station is:",commonSs)

    # TO DO: display most commonly used end station
    commonEs = df['End Station'].mode()[0]
    print("Most commonly used end station is:",commonEs)

    # TO DO: display most frequent combination of start station and end station trip
    commonComb = df.groupby(['Start Station','End Station']).size().idxmax() #i've got the answer from stackoverflow
    print("most frequent combination of start station and end station trip is:",commonComb)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    ToTravelTime = df['Trip Duration'].sum()
    print("Total travel time is:",ToTravelTime)

    # TO DO: display mean travel time
    MeanTravelTime = df['Trip Duration'].mean()
    print("Mean travel time is:",MeanTravelTime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    UserTypesCount = df['User Type'].value_counts()
    print("Total number of each user type is:\n",UserTypesCount)

    # TO DO: Display counts of gender
    if(city != 'washington'):
        GenderCount = df['Gender'].value_counts()
        print("Total number of each gender is:\n",GenderCount)
    else:
        print('Missing gender values in the washington city data file!')

    # TO DO: Display earliest, most recent, and most common year of birth
    if(city != 'washington'):
        EarlyBY = df['Birth Year'].min()
        print("earliest year of birth is:",EarlyBY)
        RecentBY = df['Birth Year'].max()
        print("Recent year of birth is: ",RecentBY)
        CommonBY = df['Birth Year'].mode()[0]
        print("Most common year of birth is",CommonBY)
    else:
        print('Missing Birth Year values in the washington city data file!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """
    display 5 lines of raw data in each request confirmed by the user

    Args:
        df - Pandas DataFrame containing city data 
    Returns:
        None.
    """
    print('\nDisplaying requested lines of raw data...\n')
    start_time = time.time()
    
    answers = ['yes', 'no']
    answer = ''
    iteration = 0
    answer = input("\ndo you want to display the first 5 lines of data ?\nyour answer should be 'yes' or 'no'.").lower()
    while(answer != answers[1]):
        while(answer not in answers ):
            answer = input("\nthere's an error in your response, please make sure to answer by 'yes' or 'no'!\n").lower()
        if(answer == answers[0]):
            print(df[iteration: iteration + 5])
            iteration += 5
            answer = input("\nin order to display the next 5 lines of data, please answer 'yes', otherwise answer 'no'.\n").lower()
            
    print("you've displayed {} iteration of 5 lines of raw data".format(int(iteration/5)))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()




