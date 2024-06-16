import pandas as pd 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px

def load_data(file_path):
    try:
        df = pd.read_csv(file_path, header=None, skiprows=1)
        df.columns = ['PassengerID', 'Name', 'Birthdate', 'TravelClass', 'LoyaltyMember', 'FlightNumber']
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")

def clean_data(df):
  
    # Print column names to ensure correct loading
    print("Columns in DataFrame:", df.columns)

    # Check and handle missing values
    if df.isnull().sum().sum() > 0:
        df = df.fillna({
            'Name': 'Unknown',
            'Birthdate': '1900-01-01',  # Example default date
            'TravelClass': 'Economy',
            'LoyaltyMember': False,
            'FlightNumber': 'Unknown'
        })
        print("Missing values handled.")

    # Correct data types
    df['Birthdate'] = pd.to_datetime(df['Birthdate'])
    df['LoyaltyMember'] = df['LoyaltyMember'].astype(bool)
    
    print("Data types corrected.")
    
    return df

# Example usage
file_path = 'project1/passengers.csv'  # Replace with your actual file path
df = load_data(file_path)
df = clean_data(df)
def find_loyalty_members_in_class(df, travel_class):
    """
    Returns the names of passengers who are loyalty program members in a specific travel class.
    """
    # Filter the DataFrame for loyalty members in the specified travel class
    filtered_df = df[(df['LoyaltyMember'] == True) & (df['TravelClass'] == travel_class)]
    # Get the list of names
    names = filtered_df['Name'].tolist()
    return names

def find_loyalty_members(df):
    """
    Returns a list of names of all loyalty program members.
    """
    # Filter the DataFrame for loyalty members
    loyalty_members_df = df[df['LoyaltyMember'] == True]
    # Get the list of names
    names = loyalty_members_df['Name'].tolist()
    return names

# Example usage
travel_class = 'ECONOMY'  # Example travel class (e.g BUSINESS, FIRSTCLASS)
loyalty_members_in_class = find_loyalty_members_in_class(df, travel_class)
all_loyalty_members = find_loyalty_members(df)

print("Loyalty Members in", travel_class, ":", loyalty_members_in_class)
print("All Loyalty Members:", all_loyalty_members)
def get_class_statistics(df):
    class_stats = {}
    for travel_class in df['TravelClass'].unique():
        class_df = df[df['TravelClass'] == travel_class]
        average_age = class_df['Birthdate'].apply(lambda x: (pd.Timestamp.now() - x).days // 365).mean()
        loyalty_count = class_df[class_df['LoyaltyMember'] == True].shape[0]
        class_stats[travel_class] = {'Average Age': round(average_age), 'Loyalty Members': loyalty_count}
    return class_stats

def plot_age_distribution(df):
    """
    Plots the distribution of ages using a histogram.
    """
    # Calculate age from 'Birthdate'
    now = pd.Timestamp.now() 
    df['Age'] = df['Birthdate'].apply(lambda x: (now - x).days // 365)
    
    # Plot histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Age Distribution of Passengers')
    plt.xlabel('Age')
    plt.ylabel('Number of Passengers')
    plt.grid(True)
    plt.savefig('age_distribution.png')  # Save the plot
    plt.show()

def plot_average_age_by_class(df):
    """
    Plots the average age by travel class using a bar chart.
    """
    # Calculate age from 'Birthdate'
    now = pd.Timestamp.now()
    df['Age'] = df['Birthdate'].apply(lambda x: (now - x).days // 365)
    
    # Calculate average age by class
    avg_age_by_class = df.groupby('TravelClass')['Age'].mean().sort_values()
    
    # Plot bar chart
    plt.figure(figsize=(10, 6))
    avg_age_by_class.plot(kind='bar', color='lightgreen', edgecolor='black')
    plt.title('Average Age by Travel Class')
    plt.xlabel('Travel Class')
    plt.ylabel('Average Age')
    plt.grid(True)
    plt.savefig('average_age_by_class.png')  # Save the plot
    plt.show()
def plot_age_vs_loyalty(df):
    """
    Plots a scatter plot of age vs. loyalty membership using Seaborn.
    """
    # Calculate age from 'Birthdate'
    now = pd.Timestamp.now()
    df['Age'] = df['Birthdate'].apply(lambda x: (now - x).days // 365)
    
    # Plot scatter plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Age', y='LoyaltyMember', data=df)
    plt.title('Age vs. Loyalty Membership')
    plt.xlabel('Age')
    plt.ylabel('Loyalty Member (True/False)')
    plt.grid(True)
    plt.savefig('age_vs_loyalty.png')  # Save the plot
    plt.show()

def plot_age_distribution_by_class(df):
    """
    Plots the distribution of ages for each travel class using a box plot with Plotly.
    """
    # Calculate age from 'Birthdate'
    now = pd.Timestamp.now()
    df['Age'] = df['Birthdate'].apply(lambda x: (now - x).days // 365)
    
    # Plot box plot
    fig = px.box(df, x='TravelClass', y='Age', color='TravelClass',
                 labels={'Age': 'Age of Passengers', 'TravelClass': 'Travel Class'},
                 title='Age Distribution by Travel Class')
    fig.write_image('age_distribution_by_class.png')  # Save the plot
    fig.show()