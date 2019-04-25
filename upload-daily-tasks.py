from gtasks import Gtasks

gt = Gtasks(credentials_location='credentials/credentials.json')
daily_tasks_file = open('E:\\dev\\0\\Dropbox\\Dropbox\\today.pm.txt', 'r')
task_list = gt.get_list('My Tasks')
tasks = task_list.get_tasks(include_hidden=True)

if tasks:
    for t in tasks:
        t.deleted = True

task_list.push_task_updates()

aux_list_in_my_order = []
for line in daily_tasks_file:
    aux_list_in_my_order.append(line)

aux_list_in_my_order.reverse()

for line in aux_list_in_my_order:
    task_list.new_task(title=line)
