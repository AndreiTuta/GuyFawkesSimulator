from crate import client

invalid_host = 'http://not_responding_host:4200'
crate_host='http://localhost:8000'
connection = client.connect([invalid_host, crate_host])

connection = client.connect()
connection.client._active_servers

cursor = connection.cursor()
cursor.execute("""INSERT INTO locations
(name, date, kind, position) VALUES (?, ?, ?, ?)""",
            ('Einstein Cross', '2007-03-11', 'Quasar', 7))
