from passenger_analysis import load_data, clean_data, find_loyalty_members_in_class, find_loyalty_members, get_class_statistics,plot_age_distribution, plot_average_age_by_class, plot_age_vs_loyalty, plot_age_distribution_by_class

# Example usage
file_path = '/project1/passengers.csv'
df = load_data(file_path)
df = clean_data(df)

# Get class statistics
stats = get_class_statistics(df)
print("Class Statistics:", stats)

# Find loyalty members in a specific class
members_in_economy = find_loyalty_members_in_class(df, 'ECONOMY')
print("Loyalty Members in Economy:", members_in_economy)

# Find all loyalty members
all_members = find_loyalty_members(df)
print("All Loyalty Members:", all_members)

plot_age_distribution(df)
plot_average_age_by_class(df) 
plot_age_vs_loyalty(df)
plot_age_distribution_by_class(df)
