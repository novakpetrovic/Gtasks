from gtasks import Gtasks

gt = Gtasks(credentials_location='credentials/credentials.json')
incoming_tasks_file = open('E:\\dev\\0\\Dropbox\\Dropbox\\incoming.pmd.txt',
                           'a')
task_list = gt.get_list('Incoming')
tasks = task_list.get_tasks(include_hidden=True)

for t in tasks:
    if not t.complete:
        incoming_tasks_file.write(t.title)
        incoming_tasks_file.write('\n')
    t.deleted = True

task_list.push_task_updates()
