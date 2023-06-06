# # def avg(lst):
# #     print(lst,"ooooooooooo")
# #     return (lst[0]+lst[1]+lst[2])/n

# # if __name__=='__main__':
# #     n = int(input("enter the students: "))
# #     student_marks = {}
# #     for i in range(n): 
# #         # print(i,"------------------------------------")
# #         name, *line = input().split()
# #         # print(name,"ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp")
# #         # print(*line,"jjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
# #         scores = list(map(float, line))
# #         # print(scores,"mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
# #         student_marks[name] = scores
# #         # print(student_marks,"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
# #     query_name = input("enter the name of stud whose avg u want: ")
# #     print(f'{avg(student_marks[query_name]):.2f}')

# # if __name__ == '__main__':
# #     N = int(input("enter the num: "))
# #     arr = []
# #     for i in range(N):
# #         print(i,"**************************************************")
# #         line = input("enter the lines: ").split()
# #         print(line,"kkkkkkkkkkkkkkk")
# #         command = line[0]
# #         # print(int(line[1]),"_______________________________________")
# #         print(command,"+++++++++++++++++++++++++++++")
        
# #         if command=='insert':
# #             arr.insert(int(line[1]),int(line[2]))
            
# #             print(arr,"iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        
# #         elif command=='print':
# #             print(arr,"arrayyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        
# #         elif command=='remove':
# #             arr.remove(int(line[1]))
# #             print(arr,"removeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            
# #         elif command=='append':
# #             arr.append(int(line[1]))
        
# #         elif command=='sort':
# #             arr.sort()
            
# #         elif command=='pop':
# #             arr.pop()
            
# #         else:#reverse
# #             arr.reverse()
# #     # print(arr,"lllllllllllllllllllllllllllllllllllllllllllllllllllll")


# # if __name__ == '__main__':
#     # n = int(input("enter the num: "))
#     # print(n,"oooooooooooo")
#     # # a=input("enter value: ").split()
#     # # print(a,"++++++++++++++++++")
#     # integer_list = map(int, input().split())
#     # # print(integer_list,"wwwwwwww")
#     # t = tuple(integer_list)
#     # print(t,"uuuuuuuuu")
#     # print(hash(t))



# l1 = [1,3,5,7,6,8]
# l2 = [2,4,6,8,3]
# l3=l1+l2
# print(len(l3))
# n=len(l3)
# print(n)
# # for removing duplicate:
# l4=[]
# for i in l3:
#     # print(i)
#     if i not in l4:
#         l4.append(i)
# print(l4)

    
    
# def sort_and_dup(li1,li2):
#     li3 = li1+li2
#     li4 = []

#     for x in li3:
#         if x not in li4:
#             li4.append(x)
#     print(li4)
#     n = len(li4)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if li4[j]<li4[j+1]:
#                 li4[j],li4[j+1]=li4[j+1],li4[j]

#     return li4

# print(sort_and_dup([1,3,5,7,6,8],[2,4,6,8,3]))



# def print_full_name(first, last):
#     # Write your code here
#     print(f"Hello {first} {last}! You just delved into python.")

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
    # print_full_name(first_name, last_name)


# def count_substring(string, sub_string):

#     count = 0
#     for i in range(0, len(string)):
        
#         if string.find(sub_string) != -1:
#             start_index = string.find(sub_string)
#             print(start_index,"uuuuuuuuuuuuuuu")
#             string = string[start_index+1:]
#             print(string)
#             count += 1
                        
#     return count
    
    

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)



# def check_alp(s):
#       a=b=c=d=e="False"
#       for i in s:
#         if i.isalnum():
#             a="True"
#         if i.isalpha():
#             b="True"
#         if i.isdigit():
#             c="True"
#         if i.islower():
#             d="True"
#         if i.isupper():
#             e="True"
#       return a + "\n" + b + "\n" + c +  "\n" + d + "\n" + e
# if __name__ == '__main__':
#     s = input()
#     print(check_alp(s))
# import textwrap

# def wrap(string, max_width):
#     l=[]
#     while len(string)!=0:
#        l.append(string[0:max_width])
#        l.append("\n")
#     string=string[max_width:]
#     return string
    
   

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)



# def print_formatted(number):
    
#     for i in range(1,number+1):
#         # binlen = len(str(bin(number)))
#         b=bin(number)
#         print(b,"oooooooooooo")
#         octf = oct(i).split('o')
#         hexf = hex(i).split('x')
#         binf = bin(i).split('b')
#         print(i , octf[1] , hexf[1].upper() , binf[1] )
  
# if __name__ == '__main__':
#     n = int(input("9UIEWIOW: "))
    # print_formatted(n)


# n = int(input("enter  the num: "))
# set1 = set(map(int,input("enter the s1: ").split()))
# # print(set1,"ooooooooooooo")
# b = int(input("enter  the num: "))
# set2 = set(map(int,input("enter the s2: ").split()))
# # print(set2,"ppppppppppppppppppp")
# u = set1.union(set2)
# print(len(u))



student_english=int(input("enter the num of students who have subscribe english news papaer: "))
set1 = set(map(int,input().split()))
student_french=int(input("enter the num of students who have subscribe french news papaer: "))
set2=set(map(int,input().split()))
u=set1.intersection(set2)
print(len(u))