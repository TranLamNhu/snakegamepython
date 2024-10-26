from tkinter import *
from PIL import Image, ImageTk

def main_window(root):
    # Tạo cửa sổ chính
    win = Toplevel()  # Sử dụng Toplevel để tạo cửa sổ mới
    win.title('Snakegame')
    win.geometry('600x600')

    # Đọc ảnh từ file
    try:
        background_image = Image.open(r'C:\Python\LTP\snakegamepython\img\backgroundselect.jpg')
        background_image = background_image.resize((600, 600))
        background_photo = ImageTk.PhotoImage(background_image)
    except Exception as e:
        print(f"Lỗi khi tải ảnh: {e}")
        return  # Kết thúc hàm nếu không tải được ảnh

    # Tạo widget Canvas để hiển thị ảnh nền
    canvas = Canvas(win, width=600, height=600)
    canvas.pack(fill="both", expand=True)

    # Hiển thị ảnh nền trên Canvas
    canvas.create_image(0, 0, anchor="nw", image=background_photo)


    # Hàm khi nhấn vào chữ "Play"
    def click_play(event=None):
        print("You clicked Play!!")
    def click_difficulty(event=None):
        print("You clicked Play!!")
    def click_skin(event=None):
        print("You clicked Play!!")
    def click_map(event=None):
        print("You clicked Play!!")
    def click_history(event=None):
        print("You clicked Play!!")
    name = canvas.create_text(300,120,text="SNAKEGAME",font=("JetBrains Mono", 40, "bold"), fill="white")
    # Thêm chữ "Play" lên Canvas, không có nền
    play_text = canvas.create_text(300, 220, text="Play", font=("JetBrains Mono", 30, "bold"), fill="white")
    # Ràng buộc sự kiện nhấn chuột trái vào vùng chữ "Play"
    canvas.tag_bind(play_text, "<Button-1>", click_play)

    # Thêm chữ "difficulty" lên Canvas, không có nền
    difficulty_text = canvas.create_text(300, 270, text="Difficulty", font=("JetBrains Mono", 30, "bold"), fill="white")
    # Ràng buộc sự kiện nhấn chuột trái vào vùng chữ "Play"
    canvas.tag_bind(difficulty_text, "<Button-1>", click_difficulty)

    # Thêm chữ "Skin" lên Canvas, không có nền
    skin_text = canvas.create_text(300, 320, text="Skin", font=("JetBrains Mono", 30, "bold"), fill="white")
    # Ràng buộc sự kiện nhấn chuột trái vào vùng chữ "Play"
    canvas.tag_bind(skin_text, "<Button-1>", click_skin)

    # Thêm chữ "Map" lên Canvas, không có nền
    map_text = canvas.create_text(300, 370, text="Map", font=("JetBrains Mono", 30, "bold"), fill="white")
    # Ràng buộc sự kiện nhấn chuột trái vào vùng chữ "Play"
    canvas.tag_bind(map_text, "<Button-1>", click_map)

    # Thêm chữ "History" lên Canvas, không có nền
    history_text = canvas.create_text(300, 420, text="History", font=("JetBrains Mono", 30, "bold"), fill="white")
    # Ràng buộc sự kiện nhấn chuột trái vào vùng chữ "Play"
    canvas.tag_bind(history_text, "<Button-1>", click_history)
    # Bắt đầu vòng lặp chính
    win.mainloop()

