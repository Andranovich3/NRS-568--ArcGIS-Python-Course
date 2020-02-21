import csv

# Parses the CSV by checking for for a delimiter (,) and appending the appropriate list.
# Also counts the number of data lines, which is needed for calculating average.

years = []
months = []
values = []

with open("co2-ppm-daily.csv") as codingChallengeCO2:
    csv_reader = csv.reader(codingChallengeCO2, delimiter=',')
    line_count = 0
    headerline = codingChallengeCO2.next()

    for row in csv_reader:
        year, month, day = row[0].split("-")

        if year not in years:
            years.append(year)
        if month not in months:
            months.append(month)
        values.append(float(row[1]))

        line_count = line_count + 1

print years
print months
print values
print "There are " + str(line_count) + " total datapoints."

# Print the Minimum, maximum and average for the entire dataset.
# str() must be used to convert the floats to strings and make them concatable and printable.
# min() & max() are built in functions for lists, the average is based on arithmetic (Total values / total number)

print "Dataset Minimum = " + str(min(values))
print "Dataset Maximum = " + str(max(values))
print "Dataset Average = " + str(float(sum(values) / int(line_count)))


# Seasonal average calculations based on Spring, Summer, Fall, Winter
# Split the data into "seasonal" lists by chekcing against the returned value for month
# len() is a built in function in Python (like min() & max()) to calculate length of a list.

spring_list = []
summer_list = []
autumn_list = []
winter_list = []

with open("co2-ppm-daily.csv") as codingChallengeCO2:
    csv_reader = csv.reader(codingChallengeCO2, delimiter=',')
    line_count = 0
    headerline = codingChallengeCO2.next()

    for row in csv_reader:
        year, month, day = row[0].split("-")  # Here I split my date string into queryable chunks

        if month == '03' or month == '04' or month == '05':
            spring_list.append(float(row[1]))  # this stores my values in a list, you must make this a float or math will fail
        if month == '06' or month == '07' or month == '08':
            summer_list.append(float(row[1]))
        if month == '09' or month == '10' or month == '11':
            autumn_list.append(float(row[1]))
        if month == '12' or month == '01' or month == '02':
            winter_list.append(float(row[1]))

print "Spring Average = " + str(sum(spring_list) / len(spring_list))
print "Summer Average = " + str(sum(summer_list) / len(summer_list))
print "Autumn Average = " + str(sum(autumn_list) / len(autumn_list))
print "Winter Average = " + str(sum(winter_list) / len(winter_list))

# Annual average for each year in the dataset.
# Only calculated for one annual average because I'm still a bit shaky on how dictionaries work and store values.
# If a user wanted to draw this out, they could create a new list for every known year and append each list by checking against
#  the 60+ year values.

year1958 = []

with open("co2-ppm-daily.csv") as codingChallengeCO2:
    csv_reader = csv.reader(codingChallengeCO2, delimiter=',')
    line_count = 0
    headerline = codingChallengeCO2.next()

    for row in csv_reader:
        year, month, day = row[0].split("-")

        if year == '1958':
            year1958.append(float(row[1]))

        line_count = line_count + 1

print "The average reading in 1958 was " + str(sum(year1958) / len(year1958)) + "."
