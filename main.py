print(" Hello World! ")

tasks = []


def add_task():
    title = input("ชื่อเรื่อง: ")
    description = input("รายละเอียด: ")
    due_date = input("วันครบกำหนด: ")
    task_id = max((task["id"] for task in tasks), default=0) + 1

    tasks.append({
        "id": task_id,
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
    })


def view_tasks():
    pass


def edit_task():
    pass


def delete_task():
    pass


def main():
    while True:
        print("\nเมนูหลัก")
        print("1. เพิ่มงานใหม่")
        print("2. ดูงานทั้งหมด")
        print("3. แก้ไขงาน")
        print("4. ลบงาน")
        print("5. ออกจากโปรแกรม")

        choice = input("เลือกเมนู (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("กรุณาเลือกเมนู 1-5")


if __name__ == "__main__":
    main()