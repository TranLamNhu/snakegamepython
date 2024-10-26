import pygame

# Khởi tạo Pygame
pygame.init()

# Tạo cửa sổ game
screen = pygame.display.set_mode((600, 600))

# Tên và logo game
pygame.display.set_caption('SNAKE GAME')
logo = pygame.image.load(r'C:\Python\LTP\tieuluan\RanSanMoi\image\logo.jpg')
pygame.display.set_icon(logo)

# Vòng lặp chính để giữ cửa sổ không tắt
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Kiểm tra nếu người dùng nhấn nút thoát
            running = False  # Đặt biến running thành False để thoát vòng lặp

    # Có thể làm gì đó ở đây, như vẽ hình hoặc cập nhật màn hình

    pygame.display.flip()  # Cập nhật cửa sổ

# Thoát Pygame
pygame.quit()
