import camelot

table = camelot.read_pdf('Gama.pdf',pages = '3')
table.export('foo.csv', f = 'csv')
