import os
import filecmp
import datetime
import shutil


class IncrementalBackup:

    def __init__(self, db_path, backup_path, last_backup_path):
        self.db_path = db_path
        self.backup_path = backup_path
        self.last_backup_path = last_backup_path

    def backup(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        dest_path = os.path.join(self.backup_path, f"incremental_backup_{timestamp}")
        os.makedirs(dest_path, exist_ok=True)

        for root, dirs, files in os.walk(self.db_path):
            relative_path = os.path.relpath(root, self.db_path)
            backup_root = os.path.join(self.last_backup_path, relative_path)
            for file in files:
                db_file = os.path.join(root, file)
                backup_file = os.path.join(backup_root, file)
                if not os.path.exists(backup_file) or not filecmp.cmp(db_file, backup_file, shallow=False):
                    shutil.copy2(db_file, os.path.join(dest_path, relative_path))

        print(f"Incremental backup completed at {dest_path}")


# Usage
incremental_backup = IncrementalBackup('/var/lib/froggy', '/mnt/backups/froggy', '/mnt/backups/froggy/full_backup_20240530120000')
incremental_backup.backup()
