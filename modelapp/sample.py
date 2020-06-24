import _csv
import _sqlite3


writer = _csv.writer(open("out.csv", 'w'))
writer.writerow(['name', 'address', 'phone', 'etc'])
writer.writerow(['bob', '2 main st', '703', 'yada'])
writer.writerow(['mary', '3 main st', '704', 'yada'])




