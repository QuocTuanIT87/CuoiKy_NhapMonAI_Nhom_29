import random


# Đếm xem trong từng tiết có bao nhiêu lớp học hoặc có bao nhiêu giáo viên có thể học hoặc có thể dạy

def count_lessons(mt):
    schedule_le = []
    count = 0
    for j in range(len(mt[0])):
        for i in range(len(mt)):
            if (mt[i][j] == 1):
                count += 1
        schedule_le.append(count)
        count = 0
    return schedule_le


# Tìm ra tổng số tiết học mà các lớp được học

def class_lesson(t, cd):
    total = 0
    lesson_cl = count_lessons(cd)
    lesson_te = count_lessons(t)
    for j in range(len(t[0])):
        if (lesson_te[j] < lesson_cl[j]):
            lesson_cl[j] = lesson_te[j]
    for j in range(len(t[0])):
        total += lesson_cl[j]
    return total


# Hàm mục tiêu đếm xem trong mỗi phương án tkb có bao nhiêu giáo viên được xếp lịch hợp lý

def total_teacher(cd, t, schedule):
    count = 0
    teacher = 0
    mt = [row[:] for row in t]
    for i in range(len(cd)):
        for j in range(len(cd[i])):
            if (cd[i][j] == 1):
                teacher = schedule[i][j]
                if (t[teacher][j] == 1):
                    for h in range(len(mt)):
                        if (mt[h][j] == 1):
                            if (h == teacher):
                                count += 1
                                mt[h][j] = 0
                                break
                            elif (h != teacher):
                                mt[h][j] = 0
                                break
                else:
                    for k in range(len(mt)):
                        if (mt[k][j] == 1):
                            mt[k][j] = 0
                            break
    return count


# hàm lựa chọn ngẫu nhiên 1 giáo viên 1 lớp học và 1 tiết học để thay đổi

def get_random_move(n, m, p):
    teacher_id = random.randint(0, n - 1)
    class_id = random.randint(0, m - 1)
    time_slot = random.randint(0, p - 1)
    return (teacher_id, class_id, time_slot)


# hàm áp dụng thay đổi vào thời khóa biểu

def apply_move(schedule, move):
    teacher_id, class_id, time_slot = move
    schedule[class_id][time_slot] = teacher_id


# hàm xếp thời khóa biểu sử dụng thuật toán Leo Đồi

def hill_climbing(n, m, p, cd, t):
    # khởi tạo thời khóa biểu ngẫu nhiên
    schedule = [[random.randint(0, n - 1) for j in range(p)] for i in range(m)]
    total_tea = total_teacher(cd, t, schedule)
    sum_le = class_lesson(t, cd)
    while total_tea != sum_le:
        # tìm một thay đổi ngẫu nhiên
        move = get_random_move(n, m, p)
        new_schedule = [row[:] for row in schedule]
        apply_move(new_schedule, move)
        new_total_tea = total_teacher(cd, t, new_schedule)
        # nếu hàm mục tiêu của thời khóa biểu mới tốt hơn
        if new_total_tea > total_tea:
            schedule = new_schedule
            total_tea = new_total_tea
    return schedule


# In lịch dạy cuối tốt nhất

def print_schedule(schedule, t, cd):
    mt = [row[:] for row in t]
    for i in range(len(cd)):
        for j in range(len(cd[i])):
            if (cd[i][j] == 1):
                teacher_id = schedule[i][j]
                if mt[teacher_id][j] == 1:
                    mt[teacher_id][j] = 0
                    print(
                        f"Giáo viên {teacher_id+1} dạy lớp {i+1} tiết {j+1}")


# In ma trận

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(cell) for cell in row))


# Random ma trận 

def random_matrix(a, b):
    mt = []
    for i in range(a):
        mt.append([random.randint(0, 1) for j in range(b)])
    return mt


# Tạo ma trận R dựa trên ma trận T và CD

def matrix_r(m, n, cd, t):
    r = [[0]*n for _ in range(m)]
    mt = [row[:] for row in t]
    for i in range(len(cd)):
        for j in range(len(cd[i])):
            if (cd[i][j] == 1):
                for h in range(len(mt)):
                    if (mt[h][j] == 1):
                        r[i][h] += 1
                        mt[h][j] = 0
                        break
    return r


# Tạo ma trận lịch học cho các lớp 
# Chỉ những tiết có lịch học ở cả ma trận C và D thì mới được xếp lịch học

def matrix_schedule(c, d):
    cd = [row[:] for row in c]
    for i in range(len(cd)):
        for j in range(len(cd[i])):
            if (c[i][j] == 1 and d[i][j] == 1):
                cd[i][j] = 1
            else:
                cd[i][j] = 0
    return cd


m = int(input("Nhập số lớp học: "))
n = int(input("Nhập số giáo viên: "))
p = int(input("Nhập số tiết học trong tuần: "))


T = random_matrix(n, p)
C = random_matrix(m, p)
D = random_matrix(m, p)
CD = matrix_schedule(C, D)
R = matrix_r(m, n, CD, T)


# Thực thi Thuật toán

schedule = hill_climbing(n, m, p, CD, T)


print("********************")
print("Ma Trận R: ")
print_matrix(R), "\n"
print("********************")
print("Ma Trận C: ")
print_matrix(C), "\n"
print("********************")
print("Ma Trận D: ")
print_matrix(D), "\n"
print("********************")
print("Ma Trận Lịch Học Lớp: ")
print_matrix(CD), "\n"
print("********************")
print("Ma Trận T: ")
print_matrix(T), "\n"
print("********************")
print("Lịch dạy: ")
print_schedule(schedule, T, CD)
