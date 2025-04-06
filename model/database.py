from model.account import Account
from model.anime import Anime
from data.data_io import load_account_json_data, write_account_json_data, load_anime_json_data, write_anime_json_data
from datetime import datetime
import operator

class AccountDatabase:
    def __init__(self):
        self.account_list = list()
        self.account_dict_data = load_account_json_data()

    # Lấy dữ liệu json chuyển thành danh sách đối tượng Account
    def load_data(self):
        for account_dict in self.account_dict_data:
            account = Account(email = account_dict["email"],
                              password = account_dict["password"])
            self.account_list.append(account)

    
class AnimeDatabase:
    def __init__(self):
        self.anime_list = list()
        self.anime_dict_data = load_anime_json_data()

    # Chuyển đối tượng python sang json
    def item_to_data(self):
        json_data = []
        for item in self.anime_list:
            json_data.append(item.__dict__)
        return json_data
    
    # Lấy dữ liệu json chuyển thành danh sách đối tượng Anime
    def load_data(self):
        for anime_dict in self.anime_dict_data:
            anime = Anime(title = anime_dict["title"],
                              release_date= anime_dict["release_date"],
                              image=anime_dict["image"],
                              rating=anime_dict["rating"])
            self.anime_list.append(anime)

    def add_item_from_dict(self, anime_dict):
        # Tạo đối tượng Anime để thêm vào ds đối tượng Anime 
        new_item = Anime(title=anime_dict["title"], release_date=anime_dict["release_date"],
                            image=anime_dict["image"], rating=anime_dict["rating"], link=anime_dict["link"])
        # Thêm anime mới vào danh sách anime 
        self.anime_list.append(new_item)
        # Thêm vào ds json 
        self.anime_dict_data.append(anime_dict)
        # Ghi dữ liệu mới vào file .json 
        write_anime_json_data(self.anime_dict_data)

    def get_item_by_id(self, id):
        for item in self.anime_list:
            if item.id == id:
                return item
        return None
    
    def edit_item_from_dict(self, edit_id, anime_dict: Anime):
        # Lấy ra bộ anime cần sửa bằng id của nó
        item = self.get_item_by_id(edit_id)
        # Sửa lại thông tin của anime
        item.update(anime_dict)
        # Lấy ra danh sách json mới nhất vừa được cập nhật 
        self.anime_dict_data = self.item_to_data()
        # Ghi dư liệu mới vào file .json
        write_anime_json_data(self.anime_dict_data)

    def delete_item(self, item_id):
        # Lấy ra bộ anime cần xoá bằng id
        anime_delete = self.get_item_by_id(item_id)
        # Xoá bộ anime khỏi danh sách đối tượng python
        self.anime_list.remove(anime_delete)
        # Lấy danh sách json mới nhất được chuyển từ danh sách đối tượng Anime
        self.anime_dict_data = self.item_to_data()
        # Viết lại dữ liệu mới trong file .json 
        write_anime_json_data(self.anime_dict_data)

    def sort_item_by_rating(self):
        # Đi lấy anime_list hiện tại đi sắp xếp, sau đó lấy kết quả sắp xếp mới đó 
        # gán vào anime_list hiện tại 
        self.anime_list = sorted(self.anime_list,
                                 key=operator.attrgetter('rating'),
                                 reverse=True)


def date_to_text(date:datetime):
    return date.strftime("%b %Y")

def format_date(date_text):
    return datetime.strptime(date_text, '%b %Y')
