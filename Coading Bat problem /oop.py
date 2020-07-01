class Employees():

    def how_many(cls):
        return cls()

    def __init__(self,emp_name,dept_name,job_desig,join_date,modules_name):
        self.emp_name = emp_name 
        self.dept_name = dept_name
        self.job_desig =job_desig
        self.join_date = join_date
        self.modules_name = modules_name


