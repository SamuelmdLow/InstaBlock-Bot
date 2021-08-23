data_name   = "original_data.csv"
data        = open(data_name, "r", encoding="utf-8").readlines()

new_data_name   = "total.csv"
new_data        = open(new_data_name, "w", encoding="utf-8")

header = "blocked,not blocked,daily,post,viral,funny,memes,clips,|,follow,backup,hacked,dose,feed,relatable,collab,curator,admin,remov,dm,inquiries,enquiries,promo,ad,ads,tik,tok,positivity,content,creator,influencer,lifestyle,reels,goal,fan,0k,1k,2k,3k,4k,5k,6k,7k,8k,9k,investor,crypto,bitcoin,business,trades,entrepreneur,study,tips,📍,🔞,fitness,weightlift,model,exercise,language,france"
terms = header.split(",")
new_data.write(header+"\n")

row = []
for i in range(len(terms)):
    row.append(0)

line = 0
while line < len(data):
    info = data[line][0:-1].split(",")

    for term in terms:
        if term in info:
            row[terms.index(term)] = row[terms.index(term)] + 1

    row_write = ""
    for cell in row:
        row_write = row_write + str(cell) + ","
    row_write = row_write[0:-1] + "\n"
    new_data.write(row_write)

    line = line + 1