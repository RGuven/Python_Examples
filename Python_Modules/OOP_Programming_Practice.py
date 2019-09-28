class universty():
    def __init__(self,univ_name,city,total_student,total_department,year_established):
        self.univ_name=str(univ_name)
        self.city=str(city)
        self.total_student=float(total_student)
        self.total_department=int(total_department)
        self.year_established=int(year_established)


    def student_per_depertment(self):
        out=self.total_student/self.total_department
        print("Student Per Depertment Approx==>",int(out))

    def change_total_student(self,new_student):
        self.total_student=new_student
        print("Number of Students Updated with ",new_student)
    def change_total_department(self,new_department):
        self.total_department=new_deparment
        print("Number of Department Updated with ",new_department)

    def univ_info(self):
        print("Universty Name = {}\nCity= {}\nTotal Student= {}\nTotal Department = {}\nYear Established= {}\n".format(self.univ_name,self.city,self.total_student,self.total_department,self.year_established))

    def __len__(self):
        
        print("Number of Total Student= {}\nNumber of Department= {}".format(self.total_student,self.total_department))
        return self.total_student
        raise TypeError("BİR HATA VARR__ ")
        
Uludag_University=universty("Uludağ Üniversitesi","Bursa",80253,60,1975)

Uludag_University.univ_info()

Uludag_University.student_per_depertment()
Uludag_University.change_total_student(67890)
Uludag_University.univ_info()
##len methot
len(Uludag_University)

class YÖK(universty):
    def __init__(self,univ_name,city,total_student,total_department,year_established):
        super().__init__(univ_name,city,total_student,total_department,year_established)
        
    def change_univ_name(self,new_univ_name):
        self.univ_name=new_univ_name
        print("University Name Updated Via YÖK\tWith===> {}".format(new_univ_name))


president=YÖK("Uludag","Bursa",60000,60,1975)
print(president)
print(president.univ_name)
president.change_univ_name("Bursa Uludağ Üniversitesi")
print(dir(YÖK))


























    

