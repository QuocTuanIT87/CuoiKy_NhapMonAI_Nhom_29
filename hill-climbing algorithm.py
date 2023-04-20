import random

# hàm tính tổng số tiết mà giáo viên dạy trong tuần


def count_teacher_hours(schedule, teacher_id):
    return sum([1 for i in range(len(schedule)) if schedule[i] == teacher_id])

# hàm tính hàm mục tiêu


def fines(schedule, r):
    conflicts = 0
    # kiểm tra xem các giáo viên có bị dạy quá số tiết quy định không
    for i in range(len(r)):
        for j in range(len(r[i])):
            if count_teacher_hours(schedule, j) > r[i][j]:
                conflicts += 1
    return conflicts

# hàm lựa chọn ngẫu nhiên một giáo viên và tiết học để thay đổi


def get_random_move(schedule, n, m, p):
    teacher_id = random.randint(0, n - 1)
    class_id = random.randint(0, m - 1)
    time_slot = random.randint(0, p - 1)
    return (teacher_id, class_id, time_slot)

# hàm áp dụng thay đổi vào thời khóa biểu


def apply_move(schedule, move):
    teacher_id, class_id, time_slot = move
    schedule[class_id][time_slot] = teacher_id

# hàm xếp thời khóa biểu sử dụng thuật toán Leo Đồi


def hill_climbing(n, m, p, r, max_iter):
    # khởi tạo thời khóa biểu ngẫu nhiên
    schedule = [[random.randint(0, n - 1)
                 for j in range(p)] for i in range(m)]
    current_fines = fines(schedule, r)
    for i in range(max_iter):
        # tìm một thay đổi ngẫu nhiên
        move = get_random_move(schedule, n, m, p)
        new_schedule = [row[:] for row in schedule]
        apply_move(new_schedule, move)
        new_fines = fines(new_schedule, r)
        # nếu hàm mục tiêu của thời khóa biểu mới tốt hơn
        if new_fines < current_fines:
            schedule = new_schedule
            current_fines = new_fines
        # nếu đã tìm được thời khóa biểu tối ưu
        if current_fines == 0:
            break
    return schedule


def print_schedule(schedule, t, cd):
    for i in range(len(schedule)):
        for j in range(len(schedule[i])):
            teacher_id = schedule[i][j]
            if t[teacher_id][j] == 1 and cd[i][j] == 1:
               print(f"Giáo viên {teacher_id+1} dạy lớp {i+1} tiết {j+1}")

# Hàm in ma trận


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(cell) for cell in row))


def random_matrix(a, b, x, y):
    mt = []
    for i in range(a):
        mt.append([random.randint(x, y) for j in range(b)])
    return mt


def matrix_schedule(c, d):
    cd = c
    for i in range(len(cd)):
        for j in range(len(cd[i])):
            if (c[i][j] == 1 and d[i][j] == 1):
                cd[i][j] = 1
            else:
                cd[i][j] = 0
    return cd


p = int(input("Nhập số tiết học trong tuần: "))
m = int(input("Nhập số lớp học: "))
n = int(input("Nhập số giáo viên: "))
max_hours = int(input("Nhập số tiết tối đa giáo viên dạy trong tuần: "))

# sử dụng chương trình
# Số liệu để test
# m = 3  # số lớp học
# p = 5  # số tiết học trong tuần
# n = 4  # số giáo viên
# max_hours = 4  # số tiết tối đa mỗi giáo viên dạy trong tuần

R = random_matrix(m, n, 1, max_hours)
T = random_matrix(n, p, 0, 1)
C = random_matrix(m, p, 0, 1)
D = random_matrix(m, p, 0, 1)
CD = matrix_schedule(C, D)

max_iter = 10000  # số lần lặp tối đa của thuật toán

# Thực thi Thuật toán
schedule = hill_climbing(n, m, p, R, max_iter)

print("Ma trận R: ")
print_matrix(R), "\n"
print("*****************")
print("Ma trận T: ")
print_matrix(T), "\n"
print("*****************")
print("Ma trận C: ")
print_matrix(C), "\n"
print("*****************")
print("Ma trận D: ")
print_matrix(D), "\n"
print("*****************")
print("Ma trận lịch học lớp: ")
print_matrix(CD), "\n"
print("*****************")
print("Lịch dạy: ")
print_schedule(schedule, T, CD)
