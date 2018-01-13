

# friends = itchat.get_friends(update=True)[0:]
# male = female = other =0
# for i in friends[1:]:
# 	sex = i["Sex"]
# 	if sex ==1:
# 		male +=1
# 	elif sex ==2:
# 		female += 1
# 	else:
# 		other += 1
# print("male:%.2f" % (float(male)/total*100)+"\n"+"female:%.2f" % (float(male)/total*100))
# import os
# from multiprocessing import Process
# print(os.getpid())
# def run_proc(name):
#     print('child process %s (%s) Running ...' % (name, os.getpid()))
# if __name__ == '__main__':
#     print("parent procesing %s." % os.getpid())
#     for i in range(5):
#         print(os.getpid())
#         p = Process(target=run_proc,args=(str(i),))
#         print("process will start %s" %i)
#         p.start()
#     p.join()
#     print("process end.")

import os,time,random

def run_task(name):
    print("Task %s (pid=%s) is running " % (name,os.getpid()))
    time.sleep(random.random()*3)
    print("Task")



