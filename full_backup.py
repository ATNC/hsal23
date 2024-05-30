import os
import shutil
import datetime


class FullBackup:
    def __init__(self, db_path, backup_path):
        self.db_path = db_path
        self.backup_path = backup_path

    def backup(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        dest_path = os.path.join(self.backup_path, f"full_backup_{timestamp}")
        shutil.copytree(self.db_path, dest_path)
        print(f"Full backup completed at {dest_path}")


# Usage
full_backup = FullBackup('/var/lib/froggy', '/mnt/backups/froggy')
full_backup.backup()
