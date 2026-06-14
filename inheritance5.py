class organization:
    def set_organization(self):
        self.organization_name="abc healthcare"
class securityteam(organization):
    def set_security(self):
        self.securityteam_name="sos team"
class analystsrole(securityteam):
    def set_analystrole(self):
        self.analystsrole_name="sos analyst"
class student(analystsrole):
    def display(self):
        
        print("organization:",self.organization_name)
        print("security team:",self.securityteam_name)
        print("analysts role:",self.analystsrole_name)
        print("analyst name:",self.student_name)
        
a=student()
a.set_organization()
a.set_securityteam()
a.student_name=input("enter the analyst name:")
a.display()