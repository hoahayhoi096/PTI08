class Task:
    def __init__(self, name, priority, completed=False):
        self.name = name
        self.priority = priority
        self.completed = completed

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Thêm công việc vào danh sách."""
        self.tasks.append(task)

    def all_tasks_done(self):
        """Kiểm tra xem tất cả công việc đã hoàn thành hay chưa."""
        # Đi lấy ds công việc chưa hoàn thành
        dsCVChuaHoanThanh = []
        for task in self.tasks:
            if task.completed == False:
                dsCVChuaHoanThanh.append(task)

        if dsCVChuaHoanThanh == []:
            print("All tasks completed")
        else:
            for task in dsCVChuaHoanThanh:
                print(task.name)

# Ví dụ sử dụng:
task1 = Task("Đi chợ", 3, False)
task2 = Task("Viết báo cáo", 2, False)
task3 = Task("Tập thể dục", 1, False)

task_list = TaskList()
task_list.add_task(task1)
task_list.add_task(task2)
task_list.add_task(task3)

# task_list.all_tasks_done()



class HocSinh: 
    def __init__(self, ten, tuoi, lop):
        self.ten = ten 
        self.tuoi = tuoi
        self.lop = lop 

tenHs1 = "Thiện"
tuoiHs1 = 13
lopHs1 = "PTI08"

hs1 = HocSinh("Thiện", 13, "PTI08")
hs2 = HocSinh("Kiên", 12, "PTI08")
hs3 = HocSinh("Nguyên", 14, "PTI08")

dsHs = []
dsHs.append(hs1)
dsHs.append(hs2)
dsHs.append(hs3)

for hs in dsHs:
    print(hs.ten, "-", hs.tuoi, "-", hs.lop)

# Quy trình thác nước 
# -> Lênh kế hoạch 
# -> Thiết kế
# -> Xây dựng
# -> Kiểm thử 
# -> Triển khai 

## Lên kế hoạch: Ý tưởng(Về ứng dụng đánh giá và xem anime),
# (Quản lý các bộ Anime(thêm, xoá, sửa), Phải hiển thị được lên giao
# diện các bộ anime có sẵn những thông tin đã được dánh giá), 
# Thời gian (Các mốc thời gian,)

## Thiết kế: Thiết kế giao diện trong QT designer, Cơ sở dữ liệu
# 