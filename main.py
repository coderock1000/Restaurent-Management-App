import tkinter as ik
from tkinter import ttk, messagebox

class RestaurentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Restaurent Management App')

        self.menu_items = {
            'French Fries' : 2,
            'Lunch Meal' : 2,
            'Burger Meal' : 3,
            'Pizza Meal' : 4,
            'Cheese Burger' : 2.5,
            'Drinks' : 1
        }

        self.exchange_rate = 84

        self.setup_background(root)

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(frame,
                  text= 'restaurent order management',
                  font=('Areal', 20 ,'bold' )).grid(row=0, columnspan=3, padx=10, pady=10)
        
        self.menu_labels = {}
        self.menu_quantities = {        }

        for i , (item, price) in enumerate(self.menu_items(), start=1):
            label = ttk.Label(frame,
                              text='f{item} (${price}):',
                              font = ('Areal', 12))
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

            self.currency_var = tk.StringVar()
            ttk.Label(frame, text='Currency: ', font=('Areal',12)).grid(row=len(self.menu_items)+1,
                                                                        coloumn= 10, padx=10                                                         pady=5)
            currency_dropdown = ttk.Combobox(frame, textvariable=self.currency_var, state='readonly', width=18, values=('USD', 'INR'))

            currency_dropdown.current(0)

            self.currency_var.trace('w', self.pygame.display.update_menu_prices)

            order_button= ttk.Button(frame, text='Place Order', command=self.place_order)
            order_button.grid(row=len(self.menu_items)+2, column=3, padx=10, pady=10)

            def setup_background(self, root):
                bg_width, bg_height = 800, 600
                canvas = tk.Canvas(root, width= bg_width, height=bg_height)
                canvas.pack()
                orginal_image = tk.PhotoImage(file='food.jpg')
                background_image = orginal_image.subsample(orginal_image.width() // bg_width,
                orginal_image.height() // bg_height)
                canvas.create_image(0,0,anchor=tk.NW, image= background_image)
            