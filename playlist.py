# Danh sách lưu trữ bài hát
songs = []

def add_song(title, artist, duration):
    """Thêm bài hát vào playlist dưới dạng dictionary"""
    song = {
        'title': title,
        'artist': artist,
        'duration': duration
    }
    songs.append(song)
    print("Đã thêm bài hát:", song)

def view_playlist():
    """In ra toàn bộ playlist"""
    if not songs:
        print("Playlist trống.")
        return
    
    print("\n--- DANH SÁCH PHÁT ---")
    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song['title']} - {song['artist']} ({song['duration']}s)")

def search_by_artist(artist_name):
    """Tìm bài hát theo tên ca sĩ"""
    found = False
    print("\n--- KẾT QUẢ TÌM KIẾM ---")
    for song in songs:
        if artist_name.lower() in song["artist"].lower():
            print(f"- {song['title']} ({song['duration']}s)")
            found = True
    
    if not found:
        print("Không tìm thấy bài hát nào của ca sĩ này.")

def view_playlist():
    """In ra toàn bộ playlist"""
    if not songs:
        print("Playlist trống.")
        return
    
    print("\n--- DANH SÁCH PHÁT ---")
    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song['title']} - {song['artist']} ({song['duration']}s)")

def search_by_artist(artist_name):
    """Tìm bài hát theo tên ca sĩ"""
    found = False
    print("\n--- KẾT QUẢ TÌM KIẾM ---")
    
    for song in songs:
        # So sánh không phân biệt hoa thường
        if artist_name.lower() in song["artist"].lower():
            print(f"- {song['title']} ({song['duration']}s)")
            found = True
    
    if not found:
        print("Không tìm thấy bài hát nào của ca sĩ này.")


def main():
    while True:
        print("\n--- MUSIC PLAYLIST MANAGER ---")
        print("1. Thêm bài hát")
        print("2. Xem danh sách phát")
        print("3. Tìm bài hát theo ca sĩ")
        print("4. Thoát")
        
        choice = input("Chọn chức năng: ")

        if choice == '1':
            title = input("Tên bài hát: ")
            artist = input("Tên ca sĩ: ")
            duration = int(input("Thời lượng (giây): "))
            add_song(title, artist, duration)

        elif choice == '2':
            view_playlist()

        elif choice == '3':
            artist_name = input("Nhập tên ca sĩ: ")
            search_by_artist(artist_name)

        elif choice == '4':
            print("Kết thúc chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
