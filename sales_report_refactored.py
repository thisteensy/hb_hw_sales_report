"""Generate sales report showing total melons each salesperson sold."""


sales_report = {}


f = open('sales-report.txt') 
for line in f:
    line = line.rstrip()
    entries = line.split('|') 
    
    if entries[0] in sales_report.keys():
        sales_report[entries[0]] += int(entries[2])
    else:
        sales_report[entries[0]] = int(entries[2])    

for key, value in sales_report.items(): 
    print(f'{key} sold {value} melons')