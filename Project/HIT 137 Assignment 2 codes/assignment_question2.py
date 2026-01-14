
# importing necessary libraries
import numpy as np
import pandas as pd
import os
import glob

# folder path where the csv files are stored
path = r"C:\Users\farih\Project\HIT 137 Assignment 2 codes\temperatures"

# finding the list of all csv file in that 'temperatures' folder
csv_files = glob.glob(path + "/*.csv")

# creating an empty list for storing all the temperature data from each csv file
all_temperatures = []

# looping through each csv files and adding them to the created list
for filename in csv_files:
    df = pd.read_csv(filename, index_col=None)
    all_temperatures.append(df)

# merging all the individual csv files into one dataframe
final_df = pd.concat(all_temperatures)

# printing the final dataframe
print(final_df)



#......processing part start......

# creating list of all months 
months_name= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# converting columns into numeric if in text
for data_column in months_name:
    final_df[data_column] = pd.to_numeric(final_df[data_column], errors='coerce')

#......processing part ends.......



#......SEASONAL AVERAGE part starts.......

# grouping months into season
summer = ['December', 'January', 'February']
autumn = ['March', 'April', 'May']
winter = ['June', 'July', 'August']
spring = ['September', 'October', 'November']

# calculating average temperature for each season as per their station
final_df['summer_average'] = final_df[summer].mean(axis=1)
final_df['autumn_average'] = final_df[autumn].mean(axis=1)
final_df['winter_average'] = final_df[winter].mean(axis=1)
final_df['spring_average'] = final_df[spring].mean(axis=1)

# calculating average temperature fpr each season across all the stations
final_summer_average = final_df['summer_average'].mean()
final_autumn_average = final_df['autumn_average'].mean()
final_winter_average = final_df['winter_average'].mean()
final_spring_average = final_df['spring_average'].mean()

# displaying the final results
seasonal_average_temp = (f"Summer: {final_summer_average:.1f}°C\n"
                         f"Autumn: {final_autumn_average:.1f}°C\n"
                         f"Winter: {final_winter_average:.1f}°C\n"
                         f"Spring: {final_spring_average:.1f}°C\n")

# saving results to the 'average_temp.txt' file
seasonal_average_temp_file = open('average_temp.txt', 'w')
seasonal_average_temp_file.write(seasonal_average_temp)
seasonal_average_temp_file.close()

# checking if the file has been saved or not
if os.path.exists('average_temp.txt'):
    print("average temperature has been saved in the text file")
else:
    print("average temperature not saved")

#......SEASONAL AVERAGE part ends.......

