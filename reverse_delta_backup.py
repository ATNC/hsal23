import datetime
import difflib
import os
import shutil


class ReverseDeltaBackup:
    def __init__(self, db_path, backup_path, last_backup_path):
        self.db_path = db_path
        self.backup_path = backup_path
        self.last_backup_path = last_backup_path

    def backup(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        latest_backup_path = os.path.join(self.backup_path, f"reverse_delta_backup_{timestamp}")
        os.makedirs(latest_backup_path, exist_ok=True)

        for root, dirs, files in os.walk(self.db_path):
            relative_path = os.path.relpath(root, self.db_path)
            last_backup_root = os.path.join(self.last_backup_path, relative_path)
            for file in files:
                db_file = os.path.join(root, file)
                last_backup_file = os.path.join(last_backup_root, file)
                dest_file = os.path.join(latest_backup_path, relative_path, file)

                if os.path.exists(last_backup_file):
                    with open(db_file, 'r') as db_f, open(last_backup_file, 'r') as last_f:
                        db_content = db_f.readlines()
                        last_content = last_f.readlines()
                        diff = difflib.unified_diff(last_content, db_content)
                        with open(dest_file, 'w') as dest_f:
                            dest_f.writelines(diff)
                else:
                    shutil.copy2(db_file, dest_file)

        print(f"Reverse delta backup completed at {latest_backup_path}")

# Usage
reverse_delta_backup = ReverseDeltaBackup('/var/lib/froggy', '/mnt/backups/froggy', '/mnt/backups/froggy/last_backup')
reverse_delta_backup.backup()
