from crate import client

connection = client.connect([crate_host], error_trace=True)

cursor = connection.cursor()
cursor.execute("""INSERT INTO locations
(name, date, kind, position) VALUES (?, ?, ?, ?)""",
            ('Einstein Cross', '2007-03-11', 'Quasar', 7))
