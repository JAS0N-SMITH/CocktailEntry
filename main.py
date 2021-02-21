from tkinter import *
from tkinter import ttk
from cocktail import Cocktail

window = Tk()
"""style = ttk.Style()
style.theme_use('awlight')"""

# lists
cocktails = []
ingredients = []
ingredients_listvar = StringVar(value=ingredients)


# buttons
def add_cocktail():
    new_cocktail = Cocktail(name=input_name.get(),
                            ingredients=ingredients_listvar.get(),
                            directions=input_directions.get('1.0', 'end'),
                            image=input_image.get())
    cocktails.append(new_cocktail)
    input_name.delete(0, 'end')
    input_ingredients.delete(0, 'end')
    input_directions.delete('1.0', 'end')
    input_image.delete(0, 'end')
    ingredients_listbox.delete(0, 'end')
    for cocktail in cocktails:
        print(cocktail.print())
    return cocktails


def add_ingredient():
    ingredients.append(input_ingredients.get())
    ingredients_listvar.set(ingredients)
    input_ingredients.delete(0, 'end')
    window.update()


# UI
window.title("Cocktail Entry")
window.minsize(width=800, height=450)
window.config(padx=20, pady=20)

frame = ttk.Labelframe(window, text="Cocktail Entry", borderwidth=5, relief='sunken', width=800,
                       height=450, padding="12 12 12 12")
frame.grid(column=0, row=0, sticky=(N, W, E, S))

entry_frame = ttk.Labelframe(frame, text="Name", borderwidth=5, relief='raised', width=300,
                             height=350, padding="12 12 12 12")
entry_frame.grid(column=0, row=0, padx=5, pady=5, sticky=(N, W))

ingredient_frame = ttk.Labelframe(frame, text="Ingredients", borderwidth=5, relief='raised',
                                  width=300, height=350, padding="12 12 12 12")
ingredient_frame.grid(column=1, row=0, padx=5, pady=5, sticky=(N, W))

directions_frame = ttk.Labelframe(frame, text="Directions", borderwidth=5, relief='raised',
                                  width=300, height=350, padding="12 12 12 12")
directions_frame.grid(column=2, row=0, padx=5, pady=5, sticky=(N, W))
directions_frame.columnconfigure(0, weight=10)
directions_frame.grid_propagate(False)

image_frame = ttk.Labelframe(frame, text="Image", borderwidth=5, relief='raised', width=300,
                             height=350, padding="12 12 12 12")
image_frame.grid(column=3, row=0, padx=5, pady=5, sticky=(N, W))

# labels
"""title_lable = Label(frame, text="Cocktail Entry", font=("Arial", 16, "bold"))
title_lable.config(pady=20)
title_lable.grid(column=0, row=0)"""


# input
input_name = Entry(entry_frame)
input_name.grid(column=0, row=1)

input_ingredients = Entry(ingredient_frame)
input_ingredients.grid(column=0, row=1)

input_directions = Text(directions_frame, height=18, padx=5, pady=5, selectborderwidth=5,
                        wrap=WORD)
input_directions.grid(column=0, row=1)

input_image = Entry(image_frame)
input_image.grid(column=0, row=1)

# buttons
add_drink_button = Button(entry_frame, text="Add", command=add_cocktail)
add_drink_button.grid(column=1, row=1)

add_ingredient_button = Button(ingredient_frame, text="Add", command=add_ingredient)
add_ingredient_button.grid(column=1, row=1)

# listbox
ingredients_listbox = Listbox(ingredient_frame, listvariable=ingredients_listvar)
ingredients_listbox.grid(column=0, row=2)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

window.mainloop()
