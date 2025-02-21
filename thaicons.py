import tkinter as tk
import random

# Thai consonants with their names
thai_consonants = [
    ("ก", "กอ ไก่"),
    ("ข", "ขอ ไข่"),
    ("ฃ", "ฃอ ขวด"),
    ("ค", "คอ ควาย"),
    ("ฆ", "ฆอ ระฆัง"),
    ("ง", "งอ งู"),
    ("จ", "จอ จาน"),
    ("ฉ", "ฉอ ฉิ่ง"),
    ("ช", "ชอ ช้าง"),
    ("ซ", "ซอ โซ่"),
    ("ฌ", "ฌอ เฌอ"),
    ("ญ", "ญอ หญิง"),
    ("ฎ", "ฎอ ชฎา"),
    ("ฏ", "ฏอ ปฏัก"),
    ("ฐ", "ฐอ ฐาน"),
    ("ฑ", "ฑอ มณโฑ"),
    ("ฒ", "ฒอ ผู้เฒ่า"),
    ("ณ", "ณอ เณร"),
    ("ด", "ดอ เด็ก"),
    ("ต", "ตอ เต่า"),
    ("ถ", "ถอ ถุง"),
    ("ท", "ทอ ทหาร"),
    ("ธ", "ธอ ธง"),
    ("น", "นอ หนู"),
    ("บ", "บอ ใบไม้"),
    ("ป", "ปอ ปลา"),
    ("ผ", "ผอ ผึ้ง"),
    ("ฝ", "ฝอ ฝา"),
    ("พ", "พอ พาน"),
    ("ฟ", "ฟอ ฟัน"),
    ("ภ", "ภอ สำเภา"),
    ("ม", "มอ ม้า"),
    ("ย", "ยอ ยักษ์"),
    ("ร", "รอ เรือ"),
    ("ล", "ลอ ลิง"),
    ("ว", "วอ แหวน"),
    ("ศ", "ศอ ศาลา"),
    ("ษ", "ษอ ฤๅษี"),
    ("ส", "สอ เสือ"),
    ("ห", "หอ หีบ"),
    ("ฬ", "ฬอ จุฬา"),
    ("อ", "ออ อ่าง"),
    ("ฮ", "ฮอ นกฮูก")
]

# Function to show a new flashcard
def new_flashcard():
    global current_consonant
    current_consonant = random.choice(thai_consonants)
    card_label.config(text=current_consonant[0])
    flip_button.config(state=tk.NORMAL)
    next_button.config(state=tk.DISABLED)

# Function to flip the card
def flip_card():
    card_label.config(text=current_consonant[1])
    flip_button.config(state=tk.DISABLED)
    next_button.config(state=tk.NORMAL)

# Create the main window
root = tk.Tk()
root.title("Thai Consonant Flashcards")
root.geometry("400x300")
root.configure(bg="lightblue")

# Flashcard Label
card_label = tk.Label(root, text="", font=("Arial", 48, "bold"), bg="white", width=10, height=3)
card_label.pack(pady=30)

# Buttons
flip_button = tk.Button(root, text="Flip Card", font=("Arial", 14), command=flip_card, state=tk.DISABLED)
flip_button.pack(pady=10)

next_button = tk.Button(root, text="Next Card", font=("Arial", 14), command=new_flashcard)
next_button.pack(pady=10)

# Load the first flashcard
new_flashcard()

# Run the application
root.mainloop()
