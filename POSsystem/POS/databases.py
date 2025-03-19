import sqlite3
import json
from datetime import datetime
from pathlib import Path


class Database():
    def add(meme, id, itemdata, status, cash, credit, tips, taxes, discounts, subtotal, total, change, roundedchange, notes, time):
        con = sqlite3.connect(f'..\\Desktop\\POSsystem\\Datas\\{str(datetime.now().date())}.db')
        cur = con.cursor()
        try:
            cur.execute("CREATE TABLE tickets(id, items, completed, cash, credit, tips, taxes, discounts, subtotal, total, change, roundedchange, notes, time)")
        except Exception as i:
            pass
        data = [(id, json.dumps(itemdata), status, float(cash), float(credit), float(tips), float(taxes), float(discounts), float(subtotal), float(total), float(change), float(roundedchange), notes, str(time))]
        cur.executemany("INSERT INTO tickets VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
        con.commit()
        con.close()

    def Update(meme, data, taxes, discounts, subtotal, total, notes, rowid, name):
        con = sqlite3.connect(f'..\\Desktop\\POSsystem\\Datas\\{str(datetime.now().date())}.db')
        cur = con.cursor()
        cur.execute('UPDATE tickets SET id=?, items=?, taxes=?, discounts=?, subtotal=?, total=?, notes=? WHERE rowid=?', [name, json.dumps(data), float(taxes), float(discounts), float(subtotal), float(total), notes, int(rowid)])
        con.commit()
        con.close()

    def Paid(meme, data, cash, credit, tips, taxes, discounts, subtotal, total, change, rowid, roundedchange, time):
        con = sqlite3.connect(f'..\\Desktop\\POSsystem\\Datas\\{str(datetime.now().date())}.db')
        cur = con.cursor()
        cur.execute('UPDATE tickets SET items=?, completed=?, cash=?, credit=?, tips=?, taxes=?, discounts=?, subtotal=?, total=?, change=?, roundedchange=?, time=?  WHERE rowid=?', [json.dumps(data), True, float(cash), float(credit), float(tips), float(taxes), float(discounts), float(subtotal), float(total), float(change) , float(roundedchange), str(time), int(rowid)])
        con.commit()

        con.close()

    def Delete(meme, rowid):
        con = sqlite3.connect(f'..\\Desktop\\POSsystem\\Datas\\{str(datetime.now().date())}.db')
        cur = con.cursor()
        cur.execute('DELETE from tickets where rowid=?', [int(rowid)])
        con.commit()
        con.close()
        con = sqlite3.connect(f'..\\Desktop\\POSsystem\\Datas\\{str(datetime.now().date())}.db')
        cur = con.cursor()
        cur.execute("VACUUM")
        con.commit()
        con.close()

    def EditPaid(meme, rowid):
        con = sqlite3.connect(f'..\\Desktop\\POSsystem\\Datas\\{str(datetime.now().date())}.db')
        cur = con.cursor()
        cur.execute('UPDATE tickets SET completed=?, cash=?, credit=?, tips=?, change=?, roundedchange=? WHERE rowid=?', [False, float(0), float(0), float(0), float(0) , float(0), int(rowid)])
        con.commit()

        con.close()

    