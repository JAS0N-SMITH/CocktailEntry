from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
from cocktail import Cocktail

window = Tk()
"""style = ttk.Style()
style.theme_use('awlight')"""

# lists
cocktails = []
ingredients = []
ingredients_listvar = StringVar(value=ingredients)

has_image = False


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
    """Runs when Add button pressed - Adds text from input_ingredients TKInter object to
    ingredients list and then ingredients_listvar listbox object. Clears input box and updates UI
    TODO: Add second input box to handle weights and quantities"""
    ingredients.append(input_ingredients.get())
    ingredients_listvar.set(ingredients)
    input_ingredients.delete(0, 'end')
    window.update()


def del_ingredient():
    """Runs when Del button pressed - Deletes a item from TKInter listbox object and ingredients
    python list
    TODO: Multi selection functionality"""
    selected = ingredients_listbox.curselection()
    ingredients_listbox.delete(selected)
    item = selected.__getitem__(0)
    ingredients.__delitem__(item)


def get_image():
    """Fetch file chooser and format canvas to fit image
    TODO: Can this function can be broken down into separate parts to help with multi canvas bug?"""
    # image
    # https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    bg_image = ImageTk.PhotoImage(scale_image(img=img))
    # print(bg_image.width())
    # print(bg_image.height())
    image_frame.canvas = Canvas(image_frame, width=bg_image.width(),
                                height=bg_image.height(), bg="grey")
    image_frame.canvas.bg_image = bg_image
    image_frame.canvas.create_image(bg_image.width() / 2, bg_image.height() / 2,
                                    image=image_frame.canvas.bg_image)
    image_frame.canvas.grid(column=0, row=1, columnspan=3)


def has_image():
    """Check to see if an image already exists in the UI
    TODO: Make algorithm for image check to fix multiple canvas creations"""

    return True


def crop_image(img):
    """https://stackoverflow.com/questions/52375035/cropping-an-image-in-tkinter"""
    h, w = img.size
    print_image_size(img)
    left = w / 4
    right = 3 * w / 4
    upper = h / 4
    lower = 3 * h / 4
    return img.crop([left, upper, right, lower])


def scale_image(img):
    """https://www.codegrepper.com/code-examples/python/how+to+resize+image+in+python+tkinter"""
    h, w = img.size
    img_scale = .25
    print_image_size(img)
    w = round(w * img_scale)
    h = round(h * img_scale)
    return img.resize((h, w), Image.ANTIALIAS)


def print_image_size(img):
    h, w = img.size
    print(f"Width: {w} Height: {h}")


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
                             height=400, padding="12 12 12 12")
image_frame.grid(column=3, row=0, padx=5, pady=5, sticky=(N, W))

# labels
"""title_lable = Label(frame, text="Cocktail Entry", font=("Arial", 16, "bold"))
title_lable.config(pady=20)
title_lable.grid(column=0, row=0)"""

# input
input_name = Entry(entry_frame)
input_name.grid(column=0, row=0)

input_ingredients = Entry(ingredient_frame)
input_ingredients.grid(column=0, row=0)

input_directions = Text(directions_frame, height=18, padx=5, pady=5, selectborderwidth=5,
                        wrap=WORD)
input_directions.grid(column=0, row=0)

input_image = Entry(image_frame)
input_image.grid(column=0, row=0, sticky=(N, E))

# buttons
add_drink_button = Button(entry_frame, text="Add", command=add_cocktail)
add_drink_button.grid(column=1, row=0, sticky=(N, W, E), padx=3, pady=2)

add_ingredient_button = Button(ingredient_frame, text="Add", command=add_ingredient)
add_ingredient_button.grid(column=1, row=0, sticky=(N, W, E), padx=3, pady=2)

del_ingredient_button = Button(ingredient_frame, text="Del", command=del_ingredient)
del_ingredient_button.grid(column=1, row=1, sticky=(N, W, E), padx=3, pady=2)

get_image_button = Button(image_frame, text="Img", command=get_image)
get_image_button.grid(column=1, row=0, sticky=(N, W), padx=3, pady=2)

# listbox
ingredients_listbox = Listbox(ingredient_frame, listvariable=ingredients_listvar)
ingredients_listbox.grid(column=0, row=1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window.mainloop()
