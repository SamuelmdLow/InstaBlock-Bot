data_name   = "total.csv"
data        = open(data_name, "r", encoding="utf-8").readlines()

data = [line.split(",") for line in data]

cols = []

for column in range(len(data[0])):
    list = []
    for row in data:
        list.append(row[column])
    cols.append(list)

print(cols)

def myFunc(e):
    return int(e[-1])

cols.sort(key=myFunc, reverse=True)
print(cols)

new_data_name   = "total.csv"
new_data        = open(new_data_name, "w", encoding="utf-8")

for row in range(len(cols[0])):
    line = ""
    for column in cols:
        item = column[row].replace("\n", "")
        line = line + item + ","
    line = line[0:-1] + "\n"
    new_data.write(line)
new_data.close()

