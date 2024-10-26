from tkinter import *
from PIL import Image, ImageTk
import pymongo

# Kết nối với MongoDB (đã cấu hình trong VS Code)
client = pymongo.MongoClient('mongodb+srv://tranlamnhu04:snakegame@cluster0.ttifa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client["your_database"]
user_collection = db["user"]

def main_window(root):
    win = Toplevel()
    win.title('Snakegame')
    win.geometry('600x600')
    
    # Tải ảnh nền từ file
    try:
        background_image = Image.open(r'C:\Python\LTP\snakegamepython\img\backgroundselect.jpg')
        background_image = background_image.resize((600, 600))
        background_photo = ImageTk.PhotoImage(background_image)
    except Exception as e:
        print(f"Lỗi khi tải ảnh: {e}")
        return

    canvas = Canvas(win, width=600, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=background_photo)

    # Hàm mở cửa sổ chơi game
    def open_play_window():
        win.destroy()
        play_window()

    # Hàm mở cửa sổ chọn độ khó
    def open_difficulty_window():
        win.destroy()
        difficulty_window()

    # Hàm mở cửa sổ chọn giao diện (skin)
    def open_skin_window():
        win.destroy()
        skin_window()

    # Hàm mở cửa sổ chọn bản đồ
    def open_map_window():
        win.destroy()
        map_window()

    # Hàm mở cửa sổ lịch sử người chơi
    def open_history_window():
        win.destroy()
        history_window()

    # Tạo văn bản và ràng buộc sự kiện nhấn cho từng mục trên màn hình chính
    canvas.create_text(300, 120, text="SNAKEGAME", font=("JetBrains Mono", 40, "bold"), fill="white")
    play_text = canvas.create_text(300, 220, text="Play", font=("JetBrains Mono", 30, "bold"), fill="white")
    canvas.tag_bind(play_text, "<Button-1>", lambda e: open_play_window())
    
    difficulty_text = canvas.create_text(300, 270, text="Difficulty", font=("JetBrains Mono", 30, "bold"), fill="white")
    canvas.tag_bind(difficulty_text, "<Button-1>", lambda e: open_difficulty_window())

    skin_text = canvas.create_text(300, 320, text="Skin", font=("JetBrains Mono", 30, "bold"), fill="white")
    canvas.tag_bind(skin_text, "<Button-1>", lambda e: open_skin_window())

    map_text = canvas.create_text(300, 370, text="Map", font=("JetBrains Mono", 30, "bold"), fill="white")
    canvas.tag_bind(map_text, "<Button-1>", lambda e: open_map_window())

    history_text = canvas.create_text(300, 420, text="History", font=("JetBrains Mono", 30, "bold"), fill="white")
    canvas.tag_bind(history_text, "<Button-1>", lambda e: open_history_window())

    win.mainloop()

# Hàm cửa sổ chơi game
def play_window():
    play_win = Toplevel()
    play_win.title("Play")
    play_win.geometry("600x600")
    play_win.configure(bg="black")
    Label(play_win, text="Chơi trò chơi!", font=("JetBrains Mono", 20, "bold")).pack(pady=20)
    Button(play_win, text="Quay lại", command=lambda: [play_win.destroy(), main_window(root)]).pack()

# Hàm cửa sổ chọn độ khó
def difficulty_window():
    difficulty_win = Toplevel()
    difficulty_win.title("Chọn độ khó")
    difficulty_win.geometry("600x600")
    difficulty_win.configure(bg="black")
    
    Label(difficulty_win, text="Chọn độ khó:", font=("JetBrains Mono", 20, "bold")).pack(pady=20)
    speeds = ["Chậm", "Trung bình", "Nhanh"]
    selected_speed = StringVar(value="Trung bình")

    for speed in speeds:
        Radiobutton(difficulty_win, text=speed, variable=selected_speed, value=speed,
                    font=("JetBrains Mono", 15)).pack(anchor=W)

    Button(difficulty_win, text="Quay lại", command=lambda: [difficulty_win.destroy(), main_window(root)]).pack(pady=20)

# Hàm cửa sổ chọn giao diện (Skin)
def skin_window():
    skin_win = Toplevel()
    skin_win.title("Chọn giao diện")
    skin_win.geometry("600x600")
    skin_win.configure(bg="black")
    
    Label(skin_win, text="Chọn giao diện (Skin):", font=("JetBrains Mono", 20, "bold")).pack(pady=20)
    Button(skin_win, text="Quay lại", command=lambda: [skin_win.destroy(), main_window(root)]).pack(pady=20)

# Hàm cửa sổ chọn bản đồ
def map_window():
    map_win = Toplevel()
    map_win.title("Chọn bản đồ")
    map_win.geometry("600x600")
    map_win.configure(bg="black")
    
    Label(map_win, text="Chọn bản đồ:", font=("JetBrains Mono", 20, "bold")).pack(pady=20)
    Button(map_win, text="Quay lại", command=lambda: [map_win.destroy(), main_window(root)]).pack(pady=20)

# Hàm cửa sổ lịch sử người chơi
def history_window():
    history_win = Toplevel()
    history_win.title("Lịch sử người chơi")
    history_win.geometry("600x600")
    history_win.configure(bg="black")

    Label(history_win, text="10 Người chơi gần nhất:", font=("JetBrains Mono", 20, "bold")).pack(pady=20)

    # Lấy 10 người chơi gần nhất từ MongoDB
    players = user_collection.find().sort("date", -1).limit(10)
    for player in players:
        Label(history_win, text=player["name"], font=("JetBrains Mono", 15)).pack(anchor=W)

    Button(history_win, text="Quay lại", command=lambda: [history_win.destroy(), main_window(root)]).pack(pady=20)

# Khởi tạo chương trình
root = main_window


