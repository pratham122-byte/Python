class employee:
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id
    
    def details(self):
        print("employee name:(self.name)")
        print("employee id:(self.emp_id)")
        print("employee domain:(self.domain)")

class developer(employee):
    def __init__(self, name, emp_id,domain):
        employee.__init__(self,name, emp_id)
        self.domain=domain
    
    def show_domain(self):
        print("primary programming domain:(self.domain)")
dev1=developer("asha",102,"python")
dev2=developer("pratham",103,"java")
dev1.details()
dev1.show_domain()
dev2.details()
dev2.show_domain()

    