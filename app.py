from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from deep_translator import GoogleTranslator

# ================== App Setup ==================
root = Tk()
root.title("Google Translator Bro")
root.geometry("1080x400")
root.config(bg="white")

dark_mode = False

# ================== Functions ==================
def label_change():
    c1 = combobox1.get()
    c2 = combobox2.get()
    label1.config(text=c1.upper())
    label2.config(text=c2.upper())
    root.after(1000, label_change)


def toggle_mode():
    global dark_mode

    if not dark_mode:
        # 🌙 Dark Mode
        root.config(bg="#1e1e1e")

        label1.config(bg="#1e1e1e", fg="white")
        label2.config(bg="#1e1e1e", fg="white")

        f1.config(bg="#333333")
        f2.config(bg="#333333")

        text1.config(bg="#2b2b2b", fg="white", insertbackground="white")
        text2.config(bg="#2b2b2b", fg="white", insertbackground="white")

        translate_button.config(bg="#444", fg="white")
        mode_button.config(text="☀️ Light Mode")

        dark_mode = True
    else:
        # ☀️ Light Mode
        root.config(bg="white")

        label1.config(bg="white", fg="black")
        label2.config(bg="white", fg="black")

        f1.config(bg="black")
        f2.config(bg="black")

        text1.config(bg="white", fg="black", insertbackground="black")
        text2.config(bg="white", fg="black", insertbackground="black")

        translate_button.config(bg="red", fg="white")
        mode_button.config(text="🌙 Dark Mode")

        dark_mode = False


def translate_now():
    try:
        text_ = text1.get(1.0, END).strip()

        if text_ == "":
            messagebox.showwarning("Warning", "Enter text to translate")
            return

        source_lang = combobox1.get()
        target_lang = combobox2.get()

        lang_dict = googletrans.LANGUAGES
        lang_code = None

        for key, value in lang_dict.items():
            if value.lower() == target_lang.lower():
                lang_code = key
                break

        if lang_code is None:
            messagebox.showerror("Error", "Invalid target language")
            return

        translated = GoogleTranslator(source='auto', target=lang_code).translate(text_)

        text2.delete(1.0, END)
        text2.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ================== Icons ==================
try:
    image_icon = PhotoImage(file="download.png")
    root.iconphoto(False, image_icon)

    arrow_image = PhotoImage(file="images.png")
    image_label = Label(root, image=arrow_image, width=120, bg="white")
    image_label.place(x=460, y=130)
except:
    pass


# ================== Language Data ==================
language = googletrans.LANGUAGES
language_value = list(language.values())


# ================== Combobox 1 ==================
combobox1 = ttk.Combobox(root, values=language_value,
                         font=("Roboto", 14), state="readonly")
combobox1.place(x=110, y=20)
combobox1.set("english")

label1 = Label(root, text="ENGLISH",
               font=("Segoe UI", 20, "bold"),
               bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)


# ================== Text 1 ==================
f1 = Frame(root, bg="black", bd=5)
f1.place(x=10, y=118, width=430, height=210)

text1 = Text(f1, font=("Roboto", 14),
             bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side="right", fill='y')
scrollbar1.config(command=text1.yview)
text1.config(yscrollcommand=scrollbar1.set)


# ================== Combobox 2 ==================
combobox2 = ttk.Combobox(root, values=language_value,
                         font=("Roboto", 14), state="readonly")
combobox2.place(x=730, y=20)
combobox2.set("arabic")

label2 = Label(root, text="ARABIC",
               font=("Segoe UI", 20, "bold"),
               bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)


# ================== Text 2 ==================
f2 = Frame(root, bg="black", bd=5)
f2.place(x=620, y=118, width=430, height=210)

text2 = Text(f2, font=("Roboto", 14),
             bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill='y')
scrollbar2.config(command=text2.yview)
text2.config(yscrollcommand=scrollbar2.set)


# ================== Buttons ==================
translate_button = Button(root, text="Translate",
                          font=("Roboto", 15, "bold"),
                          activebackground="purple",
                          cursor="hand2", bd=5,
                          bg="red", fg="white",
                          command=translate_now)
translate_button.place(x=470, y=280)


mode_button = Button(root,
                     text="🌙 Dark Mode",
                     font=("Roboto", 12, "bold"),
                     cursor="hand2",
                     command=toggle_mode)
mode_button.place(x=480, y=20)


# ================== Run ==================
label_change()
root.mainloop()