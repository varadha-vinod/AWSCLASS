import os
import csv

filename = "vinod.csv"
header = ("S.NO", "Applications", "ENV")
data = [(1, "CHECKIN", "DCSFAT"), (2, "TRAVEL", "UTDCS"), (3, "SEATS", "DCSFAT")]

def writer(header, data, filename):
    with open(filename, "w", newline = "") as csvfile:
        applications = csv.writer(csvfile)
        applications.writerow(header)
        for x in data:
            applications.writerow(x)
def updater(header, data, filename):

writer(header, data, filename)
