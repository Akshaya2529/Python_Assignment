class Department:
    emp_count = 0

    def __init__(self, name, dept_id, loc, hod):
        self.name = name
        self.dept_id = dept_id
        self.loc = loc
        self.hod = hod
        Department.emp_count += 1

    @classmethod
    def getcount(cls):
        return cls.emp_count

    def get_details(self):
        print(f"Name: {self.name}")
        print(f"Dept id: {self.dept_id}")
        print(f"Loc: {self.loc}")
        print(f"HOD: {self.hod}")

def search(departments, searchid):
    found = False
    for dept in departments:
        if dept.dept_id == searchid:
            print("Details are found:")
            dept.get_details()
            found = True
            break
    if not found:
        print("Details are not found.")

num = int(input("Enter number of departments: "))
departments = []

for i in range(num):
    print("\nDepartment details:")
    name = input("Enter name: ")
    deptid = int(input("Enter deptid: "))
    loc = input("Enter loc: ")
    hod = input("Enter hod: ")

    dept = Department(name, deptid, loc, hod)
    departments.append(dept)

    print(f"Total depts: {Department.getcount()}")

searchid = int(input("\nEnter department ID to search: "))
search(departments, searchid)
