class  employee:
    company='google'
    salary='100 INR'
# class employee1:
    # company1='jio'
manu= employee()
rajni= employee()
# manu.salary=300
# rajni.salary=400
print(manu.company)
print(rajni.company)
employee.company='you tube'
print(manu.company)
print(rajni.company)
print(f'salary of manu {manu.salary}')
print(f'salary of rajni {rajni.salary}')
