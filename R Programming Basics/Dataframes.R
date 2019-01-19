# Dataframes
custData = data.frame(name=c('tom', 'sally', 'sue'),
                      age=c(43, 23, 36),
                      stringsAsFactors=F)
custData

# access data
custData[1,1]    # single name
custData[1,1:2]   # all data

custData[1:3, 2]   # all ages


# add row to data
recordMark = data.frame(name='mark', age=33)
custData = rbind(custData, recordMark)
print(custData)

# add column to data
debt = c(0, 25, 50, 60)
custData = cbind(custData, debt)
custData

# check if money is owed (example) cool
owesMoney = custData[custData$debt > 0,]
owesMoney   # only prints out customers where debt > 0 !