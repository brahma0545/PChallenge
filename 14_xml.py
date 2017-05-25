import xmlrpc.client
conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(conn)
print(conn.system.listMethods())
print(conn.system.methodHelp("phone"))
print(conn.phone("Bert"))
