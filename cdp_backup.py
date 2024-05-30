from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import logging


class CDPBackup:
    def __init__(self, db_path, cdp_log_path):
        self.db_path = db_path
        self.cdp_log_path = cdp_log_path
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(filename=self.cdp_log_path, level=logging.INFO,
                            format='%(asctime)s - %(message)s')

    def watch(self):
        event_handler = FileSystemEventHandler()
        event_handler.on_modified = self.on_modified
        event_handler.on_created = self.on_created
        event_handler.on_deleted = self.on_deleted

        observer = Observer()
        observer.schedule(event_handler, self.db_path, recursive=True)
        observer.start()
        print("Start watching for changes...")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    def on_modified(self, event):
        if not event.is_directory:
            change = f"Modified: {event.src_path}"
            self.backup([change])

    def on_created(self, event):
        if not event.is_directory:
            change = f"Created: {event.src_path}"
            self.backup([change])

    def on_deleted(self, event):
        if not event.is_directory:
            change = f"Deleted: {event.src_path}"
            self.backup([change])

    def backup(self, changes):
        for change in changes:
            logging.info(change)

# Usage
cdp_backup = CDPBackup('/var/lib/froggy', '/mnt/backups/froggy/cdp_log')
cdp_backup.watch()
