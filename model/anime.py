import uuid
class Anime:
    def __init__(self, title, release_date, image=None, rating=None, link=None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.release_date = release_date
        self.image = image
        self.rating = rating
        self.link = link

    # Hàm giúp đi chỉnh sửa lại những trường dữ liệu cần thiết
    def update(self, new_data):
        for key, value in new_data.items():
            if value:
                setattr(self, key, value)