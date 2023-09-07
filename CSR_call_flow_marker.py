# An app to help the CSR Agent mark the Call-Flow
# This is for Andy and Jerum
# TODO: Add a file menu to add/edit more call flows

import tkinter as tk
from tkinter import filedialog

FONT = ("Consolas", 13)
        
# Create a function to toggle label state
def toggle_label_state(label):
    if label["relief"] == "raised":
        label.config(relief="sunken", fg="grey")
    else:
        label.config(relief="raised", fg="black")


# Create a function to enable editing
text_fields = []
def enable_editing():
    if not_editing:  # TODO fix enable_editing so that it is active only once
        not_editing = 0
        for i, label in enumerate(labels):
            label.pack_forget()
            text = tk.Text(root, height=4, width=100, wrap="word", font=FONT)
            text.insert("1.0", sentences[i])
            text.pack(fill=tk.BOTH, padx=5, pady=5)
            text_fields.append(text)

# Create a function to save changes
def save_changes():
    for i, text in enumerate(text_fields):
        sentences[i] = text.get("1.0", "end") # end-1c if excluding last byte (eg: \n)
        labels[i].config(text=sentences[i])
        text.pack_forget()
        labels[i].pack(fill=tk.BOTH)
    not_editing = 1

# Create the main window
root = tk.Tk()
root.title("Customer Support - Call-Flow Marker")

# Default list of sentences / Call Flow
sentences = [
    "[Opening the Call]\n" \
    "Hello and thank you for calling [Company Name] Customer Support.\n" \
    "My name is [Your Name]. How can I assist you today?",

    "[Empathize/Apologize/Assure]\n" \
    "I'm sorry to hear that you're experiencing an issue.\n" \
    "Please know that we're here to help and make things right.",

    "[Confirm Account]\n" \
    "To better assist you, could you please provide your\n" \
    "account details or order number, if you have them?",

    "[Probe/Ask Questions]\n" \
    "Certainly, let's work together to get to the bottom of this.\n" \
    "Can you please provide more details about the issue you're facing\n" \
    "or the question you have? The more information you can share, the better I can assist you.",

    "[Solve Problem/Answer Question]\n" \
    "Thank you for sharing the details. Based on what you've described,\n"\
    "here's how we can address the situation: [Provide solution or answer to the question].\n" \
    "Please let me know if this resolves your concern or if you have any further questions.",

    "[Offer Additional Assistance]\n" \
    "Is there anything else you'd like to discuss or inquire about?\n" \
    "Our goal is to ensure your complete satisfaction, so feel free to ask any other questions or\n" \
    "share any additional concerns you might have.",

    "[Close the Call]\n" \
    "Thank you for reaching out to us today. I'm glad I could assist you with your concern.\n" \
    "If you encounter any more issues in the future or have more questions,\n " \
    "don't hesitate to call us again. Have a great day!",
]

# Create raised labels for each sentence
labels = []
for sentence in sentences:
    label = tk.Label(root, text=sentence, font=FONT,
                     relief="raised", padx=10, pady=10)
    label.pack(fill=tk.BOTH, side="top", padx=5, pady=5)
    label.bind("<Button-1>", lambda event, label=label: toggle_label_state(label))
    labels.append(label)

# Create a menu
menu = tk.Menu(root)
menu.add_command(label="Edit Contents", command=enable_editing)
root.config(menu=menu)

# Create a File menu
# file_menu = tk.Menu(menu, tearoff=0)
# menu.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="Edit Contents", command=enable_editing)
# file_menu.add_command(label="Save", command=save_changes)

root.mainloop()
