import tkinter as tk
import random

root = tk.Tk()
root.title("20/10 Dễ Thương")
root.geometry("600x450")
root.config(bg="#FFE4F2")

label = tk.Label(root, text="20/10 bạn mún j nek?", font=("Comic Sans MS", 20, "bold"), bg="#FFE4F2", fg="#FF1493")
label.pack(pady=20)

def move_button():
    x = random.randint(50, 500)
    y = random.randint(150, 350)  # Xuống dưới 1 chút để không che chữ
    button_gift.place(x=x, y=y)

def show_message():
    # Ẩn câu hỏi + nút sau khi chọn
    button_gift.place_forget()
    button_wish.place_forget()

    msg_frame = tk.Frame(root, bg="#FFE4F2")
    msg_frame.pack(pady=10)

    msg = tk.Label(msg_frame, text="Chúc bạn có một ngày 20/10 vui vẻ,\nxinh xắn, tràn đầy sức sống,\nko bùn phiện bạn nhé hí hí 💗",
                   font=("Arial", 15, "bold"), bg="#FFE4F2", fg="#FF1493")
    msg.pack(pady=10)

    # Hiệu ứng trái tim chạy xung quanh viền
    def random_heart():
        heart = tk.Label(root, text="❤", font=("Arial", 18),
                         fg=random.choice(["red", "deep pink", "hot pink"]), bg="#FFE4F2")
        heart.place(x=random.randint(0, 580), y=random.randint(0, 430))
        root.after(800, heart.destroy)  # Tự xóa hiệu ứng để đỡ rối
        root.after(300, random_heart)

    random_heart()

    note = tk.Label(root, text="Hết xiền gòi, hok có quà đâu hí hí 🤣",
                    font=("Comic Sans MS", 14, "bold"), fg="purple", bg="#FFE4F2")
    note.pack(pady=20)

button_gift = tk.Button(root, text="Mún quà 🎁", font=("Arial", 14), command=move_button)
button_gift.place(x=200, y=250)

button_wish = tk.Button(root, text="Một lời chúc 💌", font=("Arial", 14), command=show_message)
button_wish.place(x=320, y=250)

button_gift.bind("<Enter>", lambda e: move_button())

root.mainloop()
