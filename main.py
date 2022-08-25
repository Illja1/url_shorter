import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.title('Url shortener')
canvas = Canvas(root, width=500, height=500)
canvas.pack()
canvas.configure(bg='#49A')
url = StringVar()
url_address = StringVar()


# Create shorter func
def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)


# Create copy func
def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)


# Create 'clear' func
def delete_input():
    input_url.delete(0, END)


def delete_output():
    out_url.delete(0, END)


# Create main text
main_text = Label(root, text='My URL Shortener', font=('poppins', 14))
# Create input label
input_url = Entry(root, textvariable=url)
# Create convert btn & clear btn & copy btn
convert = Button(root, text='Convert', font=('poppins', 14), command=urlshortener)
delete_input = Button(root, text='Clear', font=('poppins', 14), command=delete_input)
delete_output = Button(root, text='Clear', font=('poppins', 14), command=delete_output)
copy = Button(root, text='Copy', font=('poppins', 14), command=copyurl)
# Create short url label
out_url = Entry(root, textvariable=url_address)

# Create main text
canvas.create_window(250, 20, window=main_text)

# Create input url
canvas.create_window(250, 50, window=input_url)

# Create convert btn & clear btn
canvas.create_window(200, 100, window=convert)
canvas.create_window(300, 100, window=delete_input)

# Create out url
canvas.create_window(250, 150, window=out_url)

# Create copy btn & clear btn
canvas.create_window(200, 200, window=copy)
canvas.create_window(300, 200, window=delete_output)

root.mainloop()
