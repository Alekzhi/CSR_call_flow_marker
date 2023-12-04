# An app to help the CSR Agent mark the Call-Flow
# This is for Andy and Jerum
# TODO: Add a file self.menu to add/edit more call flows

import tkinter as tk
import json
        
class CallFlowApp:
    def __init__(self):
        # Create the main window. let's have the common: root rather than window
        self.root = tk.Tk()
        self.root.title("Customer Support - Call-Flow Marker")
        self.FONT = ("Consolas", 13)
        self.editing = 0 # Contents are not yet being edited
        self.editing_text_fields = [] # This is where I will transfer contents from sentences
        self.filepath = "CSR_call_flow.txt"
        self.labels = []
        self.sentences = {  # Default values
                "0":"[Opening the Call]\n" \
                "Hello and thank you for calling [Company Name] Customer Support.\n" \
                "My name is [Your Name]. How can I assist you today?",

                "1":"[Empathize/Apologize/Assure]\n" \
                "I'm sorry to hear that you're experiencing an issue.\n" \
                "Please know that we're here to help and make things right.",

                "2":"[Confirm Account]\n" \
                "To better assist you, could you please provide your\n" \
                "account details or order number, if you have them?",

                "3":"[Probe/Ask Questions]\n" \
                "Certainly, let's work together to get to the bottom of this.\n" \
                "Can you please provide more details about the issue you're facing\n" \
                "or the question you have? The more information you can share, the better I can assist you.",

                "4":"[Solve Problem/Answer Question]\n" \
                "Thank you for sharing the details. Based on what you've described,\n"\
                "here's how we can address the situation: [Provide solution or answer to the question].\n" \
                "Please let me know if this resolves your concern or if you have any further questions.",

                "5":"[Offer Additional Assistance]\n" \
                "Is there anything else you'd like to discuss or inquire about?\n" \
                "Our goal is to ensure your complete satisfaction, so feel free to ask any other questions or\n" \
                "share any additional concerns you might have.",

                "6":"[Close the Call]\n" \
                "Thank you for reaching out to us today. I'm glad I could assist you with your concern.\n" \
                "If you encounter any more issues in the future or have more questions,\n " \
                "don't hesitate to call us again. Have a great day!",
            }
        try:
            with open(self.filepath, "r") as f:
                if f:
                    sentences = json.load(f)
                    self.sentences = self.sentences if sentences == "" else sentences
        except FileNotFoundError:
            pass  # Move on with the default sentences values
        
        # Create raised self.labels for each sentence
        for sentence in self.sentences.values():
            self.label = tk.Label(self.root, text=sentence, font=self.FONT,
                            relief="raised", padx=10, pady=10)
            self.label.pack(fill=tk.BOTH, side="top", padx=5, pady=5)
            self.label.bind("<Button-1>", lambda event, label=self.label: self.toggle_label_state(label))
            self.labels.append(self.label)

        # Create a self.menu
        self.menu = tk.Menu(self.root)
        self.menu.add_command(label="Edit Contents", command=self.enable_editing)
        self.menu.add_command(label="Save", command=self.save_changes)
        self.root.config(menu=self.menu)
        
        
    # Create a function to toggle label state
    def toggle_label_state(self, label):
        if label["relief"] == "raised":
            label.config(relief="sunken", fg="grey")
        else:
            label.config(relief="raised", fg="black")


    # Create a function to enable self.editing
    def enable_editing(self):
        self.editing += 1  # If it's the first time the menu button is clicked
        if self.editing and self.editing < 2:  # If not clicked twice (to avoid overflow)
            self.editing_text_fields = []  # # Clear text_fields first
            for i, label in enumerate(self.labels):
                label.pack_forget()
                text_field = tk.Text(self.root, height=4, width=100, wrap="word", font=self.FONT)
                text_field.insert("1.0", self.sentences[str(i)])
                text_field.pack(fill=tk.BOTH, padx=5, pady=5)
                self.editing_text_fields.append(text_field)  # Transferring each sentence to each text_field value


    # Create a function to save changes
    def save_changes(self):
        if self.editing:
            self.editing = 0  # Resets counter to zero
            for i, text_field in enumerate(self.editing_text_fields):
                self.sentences[str(i)] = text_field.get("1.0", "end-1c") # end-1c excludes last byte (eg: \n)
                text_field.pack_forget()  # Now, clear all editing_text_fields
                self.labels[i].config(text=self.sentences[str(i)])
                self.labels[i].pack(fill=tk.BOTH)
        with open(self.filepath, "w") as f:
            json.dump(self.sentences, f, indent=4)


    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = CallFlowApp()
    app.run()