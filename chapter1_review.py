name = "Hello, python"
print(name)

time = "today"

#f字符串用于拼接不同字符
#"\t"是 空格， "\n"是换行
full_line = f"{name}, \t \t the day is \n{time}"
print(full_line)

#strip()，lstrip(),rstrip() 方法用于消除字符串两边的空白
my_line = "   the black    "
my_line = my_line.strip()
print(my_line)

#tittle(),upper(),lower() 方法用于转换字母的大小写
my_line = my_line.upper()
my_line = my_line.title()
print(my_line)

#removesuffix() 方法用于消除指定的后缀， removeprefix() 方法用于消除指定前缀
web = "www.temple.edu"
web = web.removesuffix(".edu")
web = web.removeprefix("www.")
print(web)

