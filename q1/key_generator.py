file = open("keys.txt", "w")
for year in ['2022','2021','2020']:
    for month in range(1,13):
        for day in range(1,32):
            date = "{}-{:02}-{:02}".format(year, (month), (day))
            file.write(date+" bigtent\n")
