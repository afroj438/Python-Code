# def sum(a,b):
#     c = a + b
#     print("sum is", c)

# sum(22,76)
# sum(657,643)


# def multi(a,b):
#    c = a * b
#    return f"the sum is c ={c}"


# a = multi(12,34)
# print(a)

# """local variable/global variable"""

# def xyz(a,b):
#     a = 20
#     b = 30
#     c = a * b
#     return c


# x = xyz(20,30)
# print(x)


# def odd_even():
#     num = int(input("enter number of cheak = "))
#     if num % 2 == 0:
#         print("even")
        
#     else:
#         print("odd")
#     return num

# user = odd_even()
# print(user)


# file = open("file_name. txt","a")
# f = open('file.txt','w')
# f.write('welcome to python programing language')
# f.close()

# f = open('file.txt','r')
# x = f.read()
# print(x)
# f.close()
# import io
# buffer = io.StringIO()  # স্ট্রিং সংরক্ষণের জন্য ইন-মেমোরি বাফার
# buffer.write("Hello, Python Buffer!")
# print(buffer.getvalue())  # আউটপুট: "Hello, Python Buffer!"
# with open("example.txt", "w") as file:
#     file.write("Hello, Python!\n")
#     file.write("This is a new line.")
# from datetime import datetime

# # ফাইলের নাম নির্ধারণ
# file_name = "date_storage.txt"

# # বর্তমান তারিখ ও সময় নেওয়া
# current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# # ফাইলে তারিখ ও সময় সংরক্ষণ
# with open(file_name, "a") as file:
#     file.write(current_datetime + "\n")

# print(f"✅ তারিখ ও সময় সংরক্ষিত হয়েছে: {current_datetime}")


# ফাইলের নাম
# file_name = "userdata.txt"

# # 🔹 ব্যবহারকারীর কাছ থেকে ডাটা নেওয়া এবং ফাইলে সংরক্ষণ করা
# with open(file_name, "a") as file:  # "a" মোড ব্যবহার করলে নতুন ডাটা আগের ডাটার সাথে যোগ হবে
#     while True:
#         data = input("Enter data to store (or type 'exit' to stop): ")
#         if data.lower() == 'exit':
#             break
#         file.write(data + "\n")  # নতুন লাইন যোগ করে ফাইলে লেখা হবে
#     print("✅ Data successfully stored in the file.")

# # 🔹 সংরক্ষিত ডাটা ফাইল থেকে পড়া
# print("\n📂 Stored Data from File:")
# with open(file_name, "r") as file:
#     print(file.read())  # পুরো ফাইলের ডাটা দেখাবে
