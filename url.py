import pyperclip
import pyshorteners
from tkinter import *
root=Tk()
root.geometry("800x500")
root.title("URL Shortener")
root.configure(bg="#6fd8ba")
url=StringVar()
url_address= StringVar()

def urlshortener():
    urladdress=url.get()
    url_short=pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short=url_address.get()
    pyperclip.copy(url_short)

Label(root,text="URL SHORTENER", fg="Black", bg="yellow", font="Times 30 bold italic").pack(pady=40)
my_label=Label(root,text="Enter the URL to be shortened:- ", font="poppins", fg="red").pack(pady=20)
Entry(root, width=50, textvariable=url).pack(pady=10)
Button(root, text="Generate the Short URL", fg="purple", bg="pink", command=urlshortener, font="Helvitica,14").pack(pady=20)
Entry(root, width=50, textvariable=url_address).pack(pady=20)
Button(root, text="Copy URL on any browser", command=copyurl, bg="pink", fg="purple", font="poppins,14").pack(pady=10)

root.mainloop()