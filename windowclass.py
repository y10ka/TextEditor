import customtkinter
import tkinter
import tkinter.messagebox
from advancedbox import AdvancedTextBox

from tkinter.filedialog import askopenfilename, asksaveasfilename

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    WIDTH = 1200
    HEIGHT = 700

    def __init__(self):
        super().__init__()

        self.title("Text Editor")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}+10+10")
        self.resizable(0, 0)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.text_field = AdvancedTextBox(master=self, width=800, height=650,
                                          corner_radius=15,
                                          border_width=5,
                                          fg_color="#E6FFFF",
                                          text_color="Black",
                                          font=("Verdana", 20),
                                          wrap="none")
        self.text_field.configure(text_font=("Consolas", 14), insertbackground='black')
        self.text_field.place(x=120, y=20)

        self.font = "Consolas"
        self.font_size_int = 14

        self.scrollbar = customtkinter.CTkScrollbar(self, command=self.text_field.yview)
        self.scrollbar.configure(height=650)
        self.scrollbar.place(x=920, y=20)

        self.scrollbar_x = customtkinter.CTkScrollbar(self, command=self.text_field.xview,
                                                      orientation="horizontal")
        self.scrollbar_x.configure(height=15, width=800)
        self.scrollbar_x.place(x=120, y=670)

        self.text_field.configure(yscrollcommand=self.scrollbar.set,
                                  xscrollcommand=self.scrollbar_x.set)

        self.open_button = customtkinter.CTkButton(master=self,
                                                   text="Open File",
                                                   width=100,
                                                   height=40,
                                                   border_width=0,
                                                   corner_radius=7,
                                                   command=self.open_file)
        self.open_button.place(x=10, y=100)
        self.save_button = customtkinter.CTkButton(master=self,
                                                   text="Save File",
                                                   width=100,
                                                   height=40,
                                                   border_width=0,
                                                   corner_radius=7,
                                                   command=self.save_file)
        self.save_button.place(x=10, y=150)

        self.font_choose = customtkinter.CTkOptionMenu(master=self,
                                                       values=["Consolas",
                                                               "Times",
                                                               "Calibri"],
                                                       command=self.font_style)
        self.font_choose.configure(width=100, height=20)
        self.font_choose.place(x=10, y=400)

        self.font_size = customtkinter.CTkEntry(master=self,
                                                placeholder_text="Size",
                                                width=60,
                                                height=30)

        self.font_size.place(x=10, y=360)

        self.font_apply = customtkinter.CTkButton(master=self,
                                                  text="OK",
                                                  width=30,
                                                  height=30,
                                                  corner_radius=7,
                                                  command=self.apply_font)
        self.font_apply.place(x=80, y=360)

        self.search = customtkinter.CTkEntry(master=self,
                                             placeholder_text="Search",
                                             width=230,
                                             height=30)
        self.search.place(x=950, y=100)

        self.search_but = customtkinter.CTkButton(master=self,
                                                  text="Search",
                                                  width=110,
                                                  height=30,
                                                  command=self.search_text)

        self.clear_but = customtkinter.CTkButton(master=self,
                                                 text="Clear",
                                                 width=110,
                                                 height=30,
                                                 command=self.clear_search)

        self.search_but.place(x=1070, y=140)
        self.clear_but.place(x=950, y=140)

        self.insert_from = customtkinter.CTkEntry(master=self,
                                                  placeholder_text="Insert from",
                                                  width=230,
                                                  height=30)
        self.insert_from.place(x=950, y=300)

        self.insert_to = customtkinter.CTkEntry(master=self,
                                                placeholder_text="Insert to",
                                                width=230,
                                                height=30)
        self.insert_to.place(x=950, y=340)

        self.insert_but = customtkinter.CTkButton(master=self,
                                                  text="Insert",
                                                  width=110,
                                                  height=30,
                                                  command=self.insert_text)
        self.insert_but.place(x=1070, y=380)

        self.str_number = customtkinter.CTkEntry(master=self,
                                                 placeholder_text="Number",
                                                 width=110,
                                                 height=30)

        self.str_number.place(x=950, y=460)

        self.str_number_button = customtkinter.CTkButton(master=self,
                                                         text="Delete",
                                                         width=110,
                                                         height=30,
                                                         command=self.remove_string)

        self.str_number_button.place(x=1070, y=460)

        self.bind('<Control-s>', self.save_file)
        self.bind('<Control-o>', self.open_file)
        self.bind('<Control-Alt-F4>', self.destroy)

    def font_style(self, s=None):
        font_in = str(self.font_choose.get())
        if len(font_in) > 0:
            self.font = str(font_in)
        self.text_field.configure(text_font=(str(self.font), int(self.font_size_int)))

    def apply_font(self):
        try:
            size_in = int(self.font_size.get())
            if size_in and not isinstance(size_in, str):
                self.font_size_int = int(size_in)
        except Exception:
            raise TypeError
        self.text_field.configure(text_font=(str(self.font), int(self.font_size_int)))

    def search_text(self):
        self.text_field.tag_remove('found', '1.0', tkinter.END)
        ser = self.search.get()
        if ser:
            idx = '1.0'
            while 1:
                idx = self.text_field.search(ser, idx, nocase=1,
                                             stopindex=tkinter.END)
                if not idx:
                    break
                last_idx = '%s+%dc' % (idx, len(ser))

                self.text_field.tag_add('found', idx, last_idx)
                idx = last_idx
            self.text_field.tag_config('found', foreground='red')
        self.search.focus_set()

    def remove_string(self):
        idx = int(self.str_number.get()) - 1
        text = (self.text_field.get(1.0, tkinter.END)).split('\n')
        text.pop(idx)
        self.text_field.delete(1.0, tkinter.END)
        self.text_field.insert(tkinter.END, '\n'.join(text))

    def clear_search(self):
        self.text_field.tag_remove('found', '1.0', tkinter.END)
        self.search.delete(0, tkinter.END)

    def insert_text(self, i=None):
        text = self.text_field.get(1.0, tkinter.END)
        txt_from = self.insert_from.get()
        txt_to = self.insert_to.get()
        text = text.replace(txt_from, txt_to)
        self.text_field.delete(1.0, tkinter.END)
        self.text_field.insert(tkinter.END, text)

    def open_file(self, o=None):
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt .cpp .h .py"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        self.text_field.delete(1.0, tkinter.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            self.text_field.insert(tkinter.END, text)
        self.title(f"Text Editor Application - {filepath}")

    def save_file(self, s=None):
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt *.txt .cpp .h .py"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = self.text_field.get(1.0, tkinter.END)
            output_file.write(text)
        self.title(f"Text Editor - {filepath} saved")

    @staticmethod
    def optionmenu_callback(self, choice):
        print("optionmenu dropdown clicked:", choice)

    @staticmethod
    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()
