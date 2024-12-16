famous_person = " 鲁迅 "
nobel_word = ' "时间就像海绵里的水，只要挤一挤，总会有的." '
message = f" {famous_person}说过：{nobel_word} "
print(message)

message = message.lstrip()
print(message)

message = message.rstrip()
print(message)

message = message.strip()
print(message)

filenmae = 'python_notes.txt'
print(filenmae)
filenmae = filenmae.removesuffix(".txt")
print(filenmae)