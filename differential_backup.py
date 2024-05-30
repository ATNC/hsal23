import datetime
import filecmp
import os
import shutil


class DifferentialBackup:
    def __init__(self, db_path, backup_path, full_backup_path):
        self.db_path = db_path
        self.backup_path = backup_path
        self.full_backup_path = full_backup_path

    def backup(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        dest_path = os.path.join(self.backup_path, f"differential_backup_{timestamp}")
        os.makedirs(dest_path, exist_ok=True)

        for root, dirs, files in os.walk(self.db_path):
            relative_path = os.path.relpath(root, self.db_path)
            full_backup_root = os.path.join(self.full_backup_path, relative_path)
            for file in files:
                db_file = os.path.join(root, file)
                full_backup_file = os.path.join(full_backup_root, file)
                if not os.path.exists(full_backup_file) or not filecmp.cmp(db_file, full_backup_file, shallow=False):
                    shutil.copy2(db_file, os.path.join(dest_path, relative_path))

        print(f"Differential backup completed at {dest_path}")

# Usage
differential_backup = DifferentialBackup('/var/lib/froggy', '/mnt/backups/froggy', '/mnt/backups/froggy/full_backup_20240530120000')
differential_backup.backup()
