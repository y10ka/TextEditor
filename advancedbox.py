import customtkinter


class AdvancedTextBox(customtkinter.CTkTextbox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.textbox.delete(*args, **kwargs)

    def get(self, index1, index2):
        return self.textbox.get(index1, index2)

    def search(self, *args, **kwargs):
        return self.textbox.search(*args, **kwargs)
