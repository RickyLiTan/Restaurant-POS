import sqlite3
import json
con = sqlite3.connect(f'..//POSsystem//Default Databases//MenuItems.db')
cur = con.cursor()
cur.execute("VACUUM")
con.commit()
con.close()