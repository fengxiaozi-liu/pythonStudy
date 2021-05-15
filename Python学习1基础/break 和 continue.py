"""
break 和 continue 是循环中满足一定条件退出循环的两种不同方式
break
   当某些条件成立终止此循环
continue
    当某些条件成立 退出当前一次循环继而向下执行下一次代码
    如果使用continue，在continue之前一定要修改计数器 continue之后的代码是不执行的直接跳到开始循环的位置
"""
# break
i = 1
j = 1
while i < 5:
    if i == 3:
        break
    i += 1
print(f'吃了{i}个苹果，吃饱了，不吃了')
# continue
while j < 5:
    if j == 3:
        j += 1
        print('吃出一个虫子,吃下一个苹果吧')
        continue
    j += 1
print('吃完苹果了')
