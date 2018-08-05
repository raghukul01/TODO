import sys
import os

x = sys.argv
param = x[1:]
cmd = ["-h", "add", "del", "clear"]

TASKS = []
try:
    file_todo = open("/tmp/todo/todo.txt","r")
    x = file_todo.read().split("\n")
except IOError:
    # this would eventually create a new file
    x = []

# normalize task list.
for i in x:
    if i != '':
        TASKS.append(i);

def delete(element):
    try:
        x = int(element)
        data = TASKS[x - 1]
    except:
        data = element
    try:
        TASKS.remove(data)
    except ValueError:
        print("\"%s\" not found in TODOS" % element)
        print_todo()
        sys.exit(0)

def print_util():
    n = 0
    for i in TASKS:
        n = max(n, len(i))
    return n

def print_todo():
    # get the size of terminal window
    rows, columns = os.popen('stty size', 'r').read().split()

    # find width of banner
    col = min(print_util() + 7, int(columns) - 1)
    # case when print_util return small number
    if col < 25:
        col = 25

    # make symmetric
    if col%2 == 0:
        col = col + 1
    top_sz = (col - 19) / 2
    top = ""
    bottom = ""
    for i in range(top_sz):
        top += "="
    for i in range(col):
        bottom += "="

    print("\n"+top+"      :TODOS:      "+top)
    if len(TASKS) == 0:
        print("No TODOS now, enjoy!!")
    else:
        for i in range(len(TASKS)):
            print(str(i + 1) + ": " + TASKS[i])
    print(bottom)
    
    
if len(param) == 0:
    # just print all todos
    print_todo()
    sys.exit(0)

elif param[0] == cmd[0]:
    print("With no arguments it print all tasks in TODO list\n\n"
        "-h       : Print usage and this help message and exit.\n"
        "add TASK : Add TASK in TODO list\n"
        "del TASK : Remove TASK from TODO list\n"
        "clear    : Remove all TODOs from list")
    sys.exit(0)

elif param[0] == cmd[1]:
    # insert into todo list
    for i in range(1,len(param)):
        TASKS.append(param[i].strip())

elif param[0] == cmd[2]:
    # delete from todo list
    # param can be the index or the item itself
    for i in range(1, len(param)):
        delete(param[i])

elif param[0] == cmd[3]:
    #delete all tasks
    TASKS = []

else:
    print("INVALID COMMAND")
    sys.exit(0)

file_todo = open("/tmp/todo/todo.txt","w")
for i in TASKS:
    file_todo.write(i)
    file_todo.write("\n")

file_todo.close()
print_todo()