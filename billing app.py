from tkinter import *

root = Tk()
root.title("BILLING APP")
root.configure(background = "black")

icon_image = PhotoImage(file = r"billing app icon.png")
root.tk.call('wm', 'iconphoto', root._w, icon_image)

def fresh_start():
    global root
    global bill_serial_number
    global bill_list
    global grand_total

    bill_serial_number = 0
    grand_total = []
    bill_list = []

    label_customer_name = Label(root, text = "Customer name:", foreground = "white", background = "black")
    label_customer_name.grid(row = 0, column = 0, padx = 4, pady = 4, sticky = W)
     
    global customer_name_entry
    customer_name_entry = Entry(root)
    customer_name_entry.grid(row = 0, column = 1, padx = 4, pady = 4)

    label_phone_number = Label(root, text = "Phone number:", foreground = "white", background = "black")
    label_phone_number.grid(row = 1, column = 0, padx = 4, pady = 4, sticky = W)
    
    global phone_number_entry
    phone_number_entry = Entry(root)
    phone_number_entry.grid(row = 1, column = 1, padx = 4, pady = 4)

    label_bill_number = Label(root, text = "Bill number:", foreground = "white", background = "black")
    label_bill_number.grid(row = 2, column = 0, padx = 4, pady = 4, sticky = W)
    
    global bill_number_entry
    bill_number_entry = Entry(root)
    bill_number_entry.grid(row = 2, column = 1, padx = 4, pady = 4)

    next_button = Button(root, text = "NEXT", foreground = "black", background = "white",command = lambda : collecting_details())
    next_button.grid(row = 3, column = 1, padx = 4, pady = 4, sticky = E)

    exit_button = Button(root, text = "EXIT", background = "red", foreground = "black", command = lambda : exit_window())
    exit_button.grid(row = 3, column = 0, padx = 4, pady = 4, sticky = W)

def exit_window():
    global exit_widget
    exit_widget = Tk()
    exit_widget.title("EXIT")

    exit_label = Label(exit_widget, text = "DO YOU WANT TO EXIT?")
    exit_label.grid(row = 0, column = 0, padx = 2, pady = 2, columnspan = 2)

    yes_button = Button(exit_widget, text = "YES", borderwidth = 2, command = lambda : destroy_app(1))
    yes_button.grid(row = 1, column = 0, padx = 2, pady = 2)

    no_button = Button(exit_widget, text = "NO", background = "black", foreground = "white", borderwidth = 2, command = lambda : destroy_app(0))
    no_button.grid(row = 1, column = 1, padx = 2, pady = 2)

def destroy_app(a):
    global root
    if a == 1:
        root.destroy()
        exit_widget.destroy()
        quit()
    else:
        exit_widget.destroy()

def collecting_details():
    global customer_name_entry
    global customer_name
    customer_name = (customer_name_entry.get()).title()

    global phone_number_entry
    global phone_number
    phone_number = phone_number_entry.get()

    global bill_number_entry
    global bill_number
    bill_number = bill_number_entry.get()

    if customer_name != "" and phone_number != "" and bill_number != "" and type(int(phone_number)) == int and type(int(bill_number)) == int:
        global root_item_list
        root_item_list = root.grid_slaves()
    
        for item in root_item_list:
            item.destroy()

        billing_main()
    
def billing_main():
    global left_side
    global right_side

    left_side = Frame(root)
    right_side = Frame(root)
    left_side.grid(row=0, column=0)
    right_side.grid(row=0, column=1)
    right_side.configure(background = "black")
    left_side.configure(background = "black")

    label_item_name = Label(left_side, text = "Item name:", foreground = "white", background = "black")
    label_item_name.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = W)
     
    global item_name_entry
    item_name_entry = Entry(left_side)
    item_name_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

    label_item_price = Label(left_side, text = "Item price:", foreground = "white", background = "black")
    label_item_price.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W)
    
    global item_price_entry
    item_price_entry = Entry(left_side)
    item_price_entry.grid(row = 1, column = 1, padx = 10, pady = 10)

    label_item_quantity = Label(left_side, text = "quantity:", foreground = "white", background = "black")
    label_item_quantity.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = W)
    
    global item_quantity_entry
    item_quantity_entry = Entry(left_side)
    item_quantity_entry.grid(row = 2, column = 1, padx = 10, pady = 10)

    add_button = Button(left_side, text = "ADD ITEM", background = "green", foreground = "black",command = lambda : add_item())
    add_button.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = EW)

    exit_button = Button(left_side, text = "  EXIT  ", background = "red", foreground = "black", command = lambda : exit_window())
    exit_button.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = W)

    new_bill_button = Button(left_side, width = 29, text = "NEW BILL", background = "white", foreground = "black", command = lambda : new_bill())
    new_bill_button.grid(row = 4, column = 0, columnspan = 2, padx = 4, pady = 4)

    font_for_bill_heading = ("monospace", 10)
    bill_heading = Label(right_side, text = "S/N              ITEM NAME                        PRICE    QTY.  TOTAL", font = font_for_bill_heading, background = "black", foreground = "gold")
    bill_heading.grid(row = 0, column = 0, padx = 4 , pady = 4, columnspan = 3)

    global bill_display
    bill_display = Text(right_side, height = 10, width = 71 ,background = "white", foreground = "black")
    bill_display.grid(row = 1, column = 0, padx = 4, pady = 4, columnspan = 3)

    button_save_bill = Button(right_side, text = "SAVE BILL", background = "gold", foreground = "black", command = lambda : save_bill())
    button_save_bill.grid(row = 2, column = 0)

    button_delete = Button(right_side, text = "DELETE", background = "light blue", foreground = "white", command = lambda : delete_item(delete_entry.get()))
    button_delete.grid(row = 2, column = 1, padx = 4, pady = 4, sticky = E)

    global delete_entry
    delete_entry = Entry(right_side, width = 2)
    delete_entry.grid(row = 2, column = 2, padx = 4, pady = 4, sticky = W)

def add_item():
    global item_name_entry
    global item_price_entry
    global item_quantity_entry   
    global price
    global item_name
    global item_quantity
    global bill_serial_number

    price = item_price_entry.get()
    item_name = item_name_entry.get()
    item_quantity = (item_quantity_entry.get()).title()
    
    if (price != "" and item_name != "" and item_quantity != "" and type(int(price)) == int and type(int(item_quantity)) == int
        and int(price) < 100000 and int(item_quantity) < 1000 and len(item_name) < 46 and bill_serial_number < 1000):

        bill_serial_number += 1

        item_name_entry.delete(0, "end")
        item_price_entry.delete(0, "end")
        item_quantity_entry.delete(0, "end")

        item_name = item_name.title()
        global bill_serial_number_str
        bill_serial_number_str = str(bill_serial_number) + "."
        
        price = int(price)
        item_quantity = int(item_quantity)

        global item_total_price

        item_total_price = price * item_quantity
        item_total_price = str(item_total_price)

        price = str(price)
        item_quantity = str(item_quantity)

        while len(bill_serial_number_str) < 4:
            bill_serial_number_str += " "

        while len(item_name) < 45:
            item_name += " "
        
        while len(price) < 5:
            price += " "
        
        while len(item_quantity) < 3:
            item_quantity += " "

        while len(item_total_price) < 8:
            item_total_price += " "

        global bill_display
        bill_display.insert('end -1 chars',f"{bill_serial_number_str} " + f"{item_name} {price}" + " x " + f"{item_quantity} {item_total_price}\n")
        bill_list.append(f"{item_name} {price}" + " x " + f"{item_quantity} {item_total_price}\n")

        global grand_total
        item_total_price = int(item_total_price)
        grand_total.append(item_total_price)

def delete_item(line):
    line = int(line)
    global bill_serial_number

    global delete_entry
    delete_entry.delete(0, "end")

    if line <= bill_serial_number:

        bill_display.delete(1.0, END)
        del bill_list[line - 1]

        bill_serial_number = 0

        global grand_total
        del grand_total[line - 1]

        for item in bill_list:
            bill_serial_number += 1
            bill_serial_number_str = str(bill_serial_number) + "."

            while len(bill_serial_number_str) < 4:
                bill_serial_number_str += " "

            bill_display.insert('end -1 chars', f"{bill_serial_number_str} " + item)

def save_bill():
    global bill_file
    global bill_display
    bill_file = open(f"Bill {bill_number}", "w")
    bill_file.write(f"BILLING APP\nCUSTOMER NAME: {customer_name}\nCUSTOMER PHONE NUMBER: {phone_number}\nBILL NUMBER: {bill_number}\n\n")
    bill_file.write("S/N              ITEM NAME                        PRICE    QTY.  TOTAL\n")
    bill_file.write(bill_display.get(1.0, END))
    bill_file.write("\n")

    global sum_grand_total
    sum_grand_total = 0
    for price in grand_total:
        sum_grand_total += price

    bill_file.write(f"TOTAL: {sum_grand_total}")
    bill_file.close()

def new_bill():
    if bill_display != "":
        save_bill()
        
    left_side.destroy()
    right_side.destroy()

    fresh_start()

fresh_start()

root.mainloop()