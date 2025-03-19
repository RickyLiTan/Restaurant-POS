from escpos.printer import Usb, Network
import sqlite3
from datetime import datetime
import json
from textwrap import fill
class Printer():
    MAX_CHAR_LINE = 48
    MAX_TOTALS_CHAR_LINE = 12
    MAX_QUANT_CHAR_LINE = 3

    def __init__(self, DATA, Type, printer):
        self.printer = printer
        self.BusinessName = "PLACEHOLDER\n\n"
        self.Address = "ADDRESS\n"
        self.Province = "PROVINCE\n"
        self.postal = "POSTAL CODE\n"
        self.phone = ("PHONE NUMBER\n")
        self.date = f'{datetime.now().date()}\n'
        self.time = f'{datetime.now().strftime("%H:%M:%S")}\n'
        self.GSTNo = "GST # NUMBER\n\n"
        self.data = DATA[0]
        self.type = Type

    def Print(self):
        self.header()
        self.Items()
        if self.type == "Reciept":
            self.TotalReciept()
        if self.type == "Bill":
            self.TotalBill()

    def header(self):
        self.printer.text(self.BusinessName)
        self.printer.text(self.Address)
        self.printer.text(self.Province)
        self.printer.text(self.postal)
        self.printer.text("\n")
        self.printer.text(self.date)
        self.printer.text(self.time)
        self.printer.text(self.GSTNo)
        self.printer.text(f'{self.data[0]}\n\n')

    def Items(self):
        self.discount = False
        for item_dict in json.loads(self.data[1]):
            if item_dict['NAME'] == "Cash Discount" or item_dict['NAME'] == 'dis':
                self.discount = True
                continue

            item = item_dict['NAME']
            price = item_dict["Price"]
            quant = int(item_dict['QTY'])
            notes = item_dict["NOTES"]


            chars_remain = Printer.MAX_CHAR_LINE - len(item) - len(str(quant)) - len(" x ") - len(price)
            if chars_remain < 0:
                newitem = item.split()
                chars_remain = Printer.MAX_CHAR_LINE - len(newitem[-1]) - len(str(quant)) - len(" x ") - len(price)
                self.printer.text(f"{quant} x {' '.join(newitem[:-1])}\n{' '*len(f'{str(quant)} x ')}{newitem[-1]}{' '*chars_remain}{price}\n")
                if notes:
                    self.printer.text(" "* len(f"{quant} x ")+f"Notes: {notes}\n\n")
                else:
                    self.printer.text("\n")
            else:
                self.printer.text(f"{quant} x {item}{' '*chars_remain}{price}\n")
                if notes:
                    self.printer.text(" "* len(f"{quant} x ")+f"Notes: {notes}\n\n")
                else:
                    self.printer.text("\n")
        
        if self.data[12] != "Notes...":
            self.printer.text(f"Notes: {self.data[12]}\n\n")
            
        

    def TotalBill(self):
        self.printer.text(f"Subtotal{' ' * (Printer.MAX_CHAR_LINE - 9 - len(str("%.2f" % self.data[8])))}${self.data[8]:.2f}\n")
        self.printer.text(f'GST (5%){' ' * (Printer.MAX_CHAR_LINE - 9 - len(str("%.2f" % self.data[6])))}${self.data[6]:.2f}\n')
        if self.discount:
            self.printer.text(f'Discount{' ' * (Printer.MAX_CHAR_LINE - 10 - len(str("%.2f" %self.data[7])))}-${self.data[7]:.2f}\n')
        self.printer.text("\n")
        self.printer.text(f'Total{' ' * (Printer.MAX_CHAR_LINE - 6 - len(str("%.2f" % self.data[9])))}${self.data[9]:.2f}')

        self.printer.cut()

    def TotalReciept(self):
        self.printer.text(f"Subtotal{' ' * (Printer.MAX_CHAR_LINE - 9 - len(str("%.2f" %self.data[8])))}${self.data[8]:.2f}\n")
        self.printer.text(f'GST (5%){' ' * (Printer.MAX_CHAR_LINE - 9 - len(str("%.2f" %self.data[6])))}${self.data[6]:.2f}\n')
        if self.discount:
            self.printer.text(f'Discount{' ' * (Printer.MAX_CHAR_LINE - 10 - len(str("%.2f" %self.data[7])))}-${self.data[7]:.2f}\n')
        self.printer.text("\n")
        self.printer.text(f'Amount{' ' * (Printer.MAX_CHAR_LINE - 7 - len(str("%.2f" %self.data[9])))}${self.data[9]:.2f}\n\n')
        if self.data[3]:
            self.printer.text(f"Cash{' ' * (Printer.MAX_CHAR_LINE - 5 - len(str("%.2f" % (self.data[3] + self.data[10]))))}${(self.data[3] + self.data[10]):.2f}\n")
        if self.data[4]:
            self.printer.text(f"Credit{' ' * (Printer.MAX_CHAR_LINE - 7 - len(str("%.2f" %self.data[4])))}${self.data[4]:.2f}\n")
        if self.data[5]:
            self.printer.text(f"Tips{' ' * (Printer.MAX_CHAR_LINE - 5 - len(str("%.2f" % self.data[5])))}${self.data[5]:.2f}\n")
        if self.data[11]:
            self.printer.text(f"Change{' ' * (Printer.MAX_CHAR_LINE - 8 - len(str("%.2f" % self.data[11])))}-${self.data[11]:.2f}\n")
        self.printer.text(f'Total{' ' * (Printer.MAX_CHAR_LINE - 6 - len(str("%.2f" %(self.data[9] + self.data[5]))))}${(self.data[9] + self.data[5]):.2f}')

        
        self.printer.cut()
    
    def GrossPaper(self):
        if self.type == "Gross":
            con = sqlite3.connect(f'..\\POSsystem\\Datas\\{str(datetime.now().date())}.db')

            cur = con.cursor()
            try:
                cur.execute("CREATE TABLE tickets(id, items, completed, cash, credit, tips, taxes, discounts, subtotal, total, change, roundedchange)")
            except Exception as i:
                pass
            List = list(cur.execute("SELECT * FROM tickets"))
            con.close()
            if not List:
                return
            else:
                cash = 0
                credit = 0
                tips = 0
                taxes = 0
                discounts = 0
                subtotal = 0
                total = 0
                change = 0
                roundedchange = 0
                cashrefunds = 0
                creditrefunds = 0
                subrefunds = 0
                for i in List:
                    if i[2]:
                        cash += i[3]
                        if i[0] == "Refunded":
                            creditrefunds += i[4]
                            cashrefunds += i[3]
                            subrefunds += i[8]
                        credit += i[4] + i[5]
                        subtotal += i[8]
                        total += i[9]
                        tips += i[5]
                        taxes += i[6]
                        discounts += i[7]
                        change += i[10]
                        roundedchange += (i[11])
                refunds = creditrefunds + cashrefunds
                self.printer.text("Daily Report\n")
                self.printer.text(self.BusinessName)
                self.printer.text(self.Address)
                self.printer.text(self.Province)
                self.printer.text(self.postal)
                self.printer.text(self.date)
                self.printer.text("\n")
                self.printer.text(f"Gross Sales{' ' * (Printer.MAX_CHAR_LINE - 12 - len(str("%.2f" % (subtotal - subrefunds))))}${(subtotal - subrefunds):.2f}\n")
                self.printer.text(f"Refunds{' ' * (Printer.MAX_CHAR_LINE - 10 - len(str("%.2f" % (subrefunds*-1))))}(${(subrefunds*-1):.2f})\n")
                self.printer.text(f"Discounts{' ' * (Printer.MAX_CHAR_LINE - 12 - len(str("%.2f" % (discounts))))}(${(discounts):.2f})\n\n")
                self.printer.text(f"Net Sales{' ' * (Printer.MAX_CHAR_LINE - 10 - len(str("%.2f" % (subtotal - discounts))))}${(subtotal - discounts):.2f}\n")
                self.printer.text(f"Taxes{' ' * (Printer.MAX_CHAR_LINE - 6 - len(str("%.2f" % taxes)))}${taxes:.2f}\n")
                self.printer.text(f"Tips{' ' * (Printer.MAX_CHAR_LINE - 5 - len(str("%.2f" % tips)))}${tips:.2f}\n")
                self.printer.text(f'Cash Rounding{' ' * (Printer.MAX_CHAR_LINE - 14 - len(str("%.2f" % (change-roundedchange))))}${(change-roundedchange):.2f}\n\n')
                self.printer.text(f'Total{' ' * (Printer.MAX_CHAR_LINE - 6 - len(str("%.2f" % (total + tips + change-roundedchange))))}${(total + tips + change-roundedchange):.2f}\n\n')
                self.printer.text(f'Payments\n')
                self.printer.text(f"Cash{' ' * (Printer.MAX_CHAR_LINE - 5 - len(str("%.2f" % (cash))))}${(cash):.2f}\n")
                self.printer.text(f"Credit{' ' * (Printer.MAX_CHAR_LINE - 7 - len(str("%.2f" % (credit))))}${(credit):.2f}\n")

                self.printer.cut()




                        
