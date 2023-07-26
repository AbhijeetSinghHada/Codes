from Search_Employee import search_emp
from view_employee import View

def modify_employee(name):
    empData ={}
    index= search_emp(name)
    index -=1
    obj_view = View()
    empData = obj_view.fetch_data()
    print(f"Name : {empData['employee'][index]['name']}")
    print(f"ID : {empData['employee'][index]['id']}")
    print(f"Department : {empData['employee'][index]['department']}")
    print(f"Email : {empData['employee'][index]['email']}")
    
    
modify_employee("Raj")
