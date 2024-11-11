import csv
from datetime import datetime

from matplotlib import pyplot as plt
        
    
def highs_or_lows():  
    while True:
        weather_input = input("Enter highs or lows (exit to quit): ").lower()
        
        if weather_input == "exit":
            break
        # Get dates and high temperatures from this file.
        elif weather_input == "highs":
            dates, highs = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date) 
                high = int(row[5])
                highs.append(high)
                
            # Build the plot.
            fig, ax = plt.subplots()
            ax.plot(dates, highs, c='red')
            
            # Format plot.
            plt.title("Daily high temperatures - 2018", fontsize=24)
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)",         fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)
            plt.show()
            highs_or_lows()
        # Get dates and low temperatures from this file.
        elif weather_input == "lows": 
            dates, lows = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                low = int(row[6])
                lows.append(low)
            # Build the plot.
            fig, ax = plt.subplots()
            ax.plot(dates, lows, c='blue')
            # Format plot.
            plt.title("Daily low temperatures - 2018", fontsize=24)
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)
            plt.show()
            highs_or_lows()
        else:
            print("Invalid input. Please enter highs or lows.")
            highs_or_lows()
def main():
    print("This program will create a graph of the high and low temperatures based on your input entered.") 
    highs_or_lows()
    
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    main()

if __name__ == '__main__' :
    main()
