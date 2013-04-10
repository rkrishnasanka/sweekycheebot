import EmoDB

quotestablecontext = EmoDB.QuotesContext()

file = open('quotes.txt','r')
lines = file.readlines()
file.close()
for line in lines:
    quotestablecontext.insertQuote(line)
#quotestablecontext.insertQuotes(lines)