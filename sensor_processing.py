calculate_average function
def calculate_average(data):
return sum(data) / len(data)

data = [72, 55, 101, 90]
average_result = calculate_average(data)
print("Average:", average_result)

The stations list and printing code
stations = [
["A1", 62],
["A2", 75],
["B1", 50],
["B2", 90]
]
for station in stations:
 print(f"{station[0]} → {station[1]}")


The stations list and printing code
def report_status(stations, threshold):
    for station in stations:
        pm25 = station[1]
        if pm25 > threshold:
            print(f"Warning: {station[0]} has a PM2.5 level of {pm25}, which exceeds the threshold of {threshold}.")
        else:
            print(f"{station[0]} is within safe limits with a PM2.5 level of {pm25}.")
            
report_status(stations, 100)
