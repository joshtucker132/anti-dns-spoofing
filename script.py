from subprocess import Popen, PIPE, STDOUT
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ExampleHandler(FileSystemEventHandler):
    def on_created(self, event):
    	print("New snort log detected...")
    	args = [event.src_path]
    	Popen(['sudo', 'python', 'extract.py'] + args)

snort_process = Popen(['sudo', 'snort', '-k', 'none', '-c', '/etc/snort/snort.conf', '-A', 'console'],
                      stdout=PIPE, stderr=STDOUT, bufsize=1,
                      universal_newlines=True, close_fds=True)

observer = Observer()
event_handler = ExampleHandler() 

observer.schedule(event_handler, path='/var/log/snort')
observer.start()

rc = snort_process.wait()


