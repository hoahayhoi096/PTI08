from model.account import Account
from model.anime import Anime
from data.data_io import load_account_json_data, write_account_json_data, load_anime_json_data, write_anime_json_data

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
