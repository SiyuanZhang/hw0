data = open('iowa-liquor-sample.csv')
count = 0
for line in data:
        if 'single malt scotch' in line.lower():
                count+=1
print count
data.close()
