#输入5个学生的成绩，然后输出最高分学生的信息以及平均成绩
import numpy as np
grade_dir={'Student_1':10,'Student_2':3,'Student_3':15,
           'Student_4':7,'Student_5':9}
#index=input('Please input a name:')
print('最高分的学生信息：')
a=list(sorted(grade_dir.items(),key=lambda item:item[1]))
e=a[4]
print(e[0],e[1])
b=list(grade_dir.values())
b.sort()
print(b[4])
print("平均成绩：")
mean=np.mean(b)
print(mean)
    
    

