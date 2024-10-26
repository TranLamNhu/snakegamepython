# main.py
import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
import re
from homepage import main_window

# Kết nối với MongoDB
client = MongoClient('mongodb+srv://tranlamnhu04:snakegame@cluster0.ttifa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['mydatabase']
collection_user = db['user']

# Kiểm tra định dạng email
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Chuyển sang khung đăng nhập
def show_login_frame():
    frame_register.pack_forget()
    frame_login.pack(fill='both', expand=True)

# Chuyển sang khung đăng ký
def show_register_frame():
    frame_login.pack_forget()
    frame_register.pack(fill='both', expand=True)

# Đăng ký
def register():
    username = entry_register_username.get()
    password = entry_register_password.get()
    email = entry_register_email.get()
    if not username:
        messagebox.showerror("Lỗi", "Tên người dùng không được để trống.")
        return
    if len(password) < 6:
        messagebox.showerror("Lỗi", "Mật khẩu phải có ít nhất 6 ký tự.")
        return
    if not is_valid_email(email):
        messagebox.showerror("Lỗi", "Địa chỉ email không hợp lệ.")
        return
    if collection_user.find_one({"username": username}):
        messagebox.showerror("Lỗi", "Tên người dùng đã tồn tại.")
    else:
        collection_user.insert_one({"username": username, "password": password, "email": email})
        messagebox.showinfo("Đăng ký thành công", "Bạn đã đăng ký thành công!")
        show_login_frame()

# Đăng nhập
def login():
    username = entry_login_username.get()
    password = entry_login_password.get()
    if not username:
        messagebox.showerror("Lỗi", "Tên người dùng không được để trống.")
        return
    if len(password) < 6:
        messagebox.showerror("Lỗi", "Mật khẩu phải có ít nhất 6 ký tự.")
        return
    user = collection_user.find_one({"username": username, "password": password})
    if user:
        root.withdraw()  # Ẩn cửa sổ đăng nhập
        main_window(root)  # Hiển thị cửa sổ chính sau khi đăng nhập thành công
    else:
        messagebox.showinfo("Đăng nhập thất bại", "Tên người dùng hoặc mật khẩu không đúng.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("SNAKEGAME")
root.geometry('600x600')
root.configure(bg='black')

# Khung đăng ký
frame_register = tk.Frame(root, bg='black')
frame_register.pack(fill='both', expand=True)

label_namegame = tk.Label(frame_register, text="SNAKEGAME", font=("JetBrains Mono", 30, "bold"), bg="black", fg="white")
label_namegame.place(x=150, y=100)

label_register_username = tk.Label(frame_register, text="Tên người dùng:", font=("JetBrains Mono", 15, "bold"), bg="black", fg="white")
label_register_username.place(x=100, y=200)
entry_register_username = tk.Entry(frame_register)
entry_register_username.place(x=270, y=205)

label_register_password = tk.Label(frame_register, text="Mật khẩu:", font=("JetBrains Mono", 15, "bold"), bg="black", fg="white")
label_register_password.place(x=100, y=250)
entry_register_password = tk.Entry(frame_register, show="*")
entry_register_password.place(x=270, y=255)

label_register_email = tk.Label(frame_register, text="Email:", font=("JetBrains Mono", 15, "bold"), bg="black", fg="white")
label_register_email.place(x=100, y=300)
entry_register_email = tk.Entry(frame_register)
entry_register_email.place(x=270, y=305)

# Nút Đăng ký
button_register = tk.Button(frame_register, text="Đăng ký", command=register, width=25, font=("JetBrains Mono", 10, "bold"))
button_register.place(x=200, y=350)

# Nút Đã có tài khoản
label_login = tk.Label(frame_register, text="Đã có tài khoản? Nhấn vào đây để đăng nhập", bg='black', fg='white', font=("JetBrains Mono", 10))
label_login.place(x=150, y=400)
label_login.bind("<Button-1>", lambda e: show_login_frame())

# Khung đăng nhập
frame_login = tk.Frame(root, bg='black')

label_login_namegame = tk.Label(frame_login, text="SNAKEGAME", font=("JetBrains Mono", 30, "bold"), bg="black", fg="white")
label_login_namegame.place(x=150, y=100)

label_login_username = tk.Label(frame_login, text="Tên người dùng:", font=("JetBrains Mono", 15, "bold"), bg="black", fg="white")
label_login_username.place(x=100, y=200)
entry_login_username = tk.Entry(frame_login)
entry_login_username.place(x=270, y=205)

label_login_password = tk.Label(frame_login, text="Mật khẩu:", font=("JetBrains Mono", 15, "bold"), bg="black", fg="white")
label_login_password.place(x=100, y=250)
entry_login_password = tk.Entry(frame_login, show="*")
entry_login_password.place(x=270, y=255)

# Nút Đăng nhập
button_login = tk.Button(frame_login, text="Đăng nhập", command=login, width=25, font=("JetBrains Mono", 10, "bold"))
button_login.place(x=200, y=350)

# Nút Chưa có tài khoản
label_register_redirect = tk.Label(frame_login, text="Chưa có tài khoản? Đăng ký tại đây", bg='black', fg='white', font=("JetBrains Mono", 10))
label_register_redirect.place(x=150, y=400)
label_register_redirect.bind("<Button-1>", lambda e: show_register_frame())

# Hiển thị khung đăng ký đầu tiên
show_register_frame()

root.mainloop()
