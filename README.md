# Froggy Database Backup System
This repository contains implementations of various backup models for the "froggy" database, including Full, Incremental, Differential, Reverse Delta, and Continuous Data Protection (CDP) backups.
## Backup Models
### Full Backup
A full backup involves copying the entire database.
Implemented in full_backup.py
### Incremental Backup
An incremental backup involves copying only the data that has changed since the last full or incremental backup.
Implemented in incremental_backup.py
### Differential Backup
A differential backup involves copying all changes made since the last full backup.
Implemented in differential_backup.py

### Reverse Delta Backup
A reverse delta backup involves keeping the latest version of the data and storing reverse deltas (differences) to reconstruct older versions.
Implemented in reverse_delta_backup.py

### Continuous Data Protection (CDP)
CDP continuously captures changes and stores them in a log file, allowing rollback to any point in time.
Implemented in cdp_backup.py

## Comparison of Backup Models
| Parameter | Full Backup | Incremental Backup | Differential Backup | Reverse Delta | CDP |
|--------------------------|-------------------|--------------------|---------------------|--------------------|------------------------|
| **Size** | Large | Small to Medium | Medium | Variable | Large |
| **Ability to Roll Back** | Limited | High | Medium | High | Very High |
| **Speed of Roll Back** | Fast | Medium | Medium | Slow to Medium | Fast to Slow |
| **Cost** | High | Medium | Medium | Variable | High |

Each backup model has its trade-offs, and the best choice depends on your specific requirements, such as storage capacity, required recovery time objectives (RTO), and recovery point objectives (RPO).



## Cost of Implementing Each Backup Model
Let's calculate the cost of implementing each backup model based on the hourly rate of $50 per hour for one specialist. We'll estimate the hours required for development, testing, and deployment for each model.
### Full Backup
**Development Time**: 4 hours
- Simple logic for copying the entire database.
**Testing Time**: 2 hours
- Verifying that the entire database is correctly copied.
**Deployment Time**: 1 hour
- Setting up cron jobs or scheduling the backups.
**Total Hours**: 7 hours
**Total Cost**: 7 hours * $50/hour = $350
### Incremental Backup
**Development Time**: 8 hours
- Implementing logic to detect changes since the last backup.
**Testing Time**: 4 hours
- Verifying that only changed data is backed up and can be correctly restored.
**Deployment Time**: 2 hours
- Setting up and configuring the backup schedules.
**Total Hours**: 14 hours
**Total Cost**: 14 hours * $50/hour = $700
### Differential Backup
**Development Time**: 6 hours
- Implementing logic to detect changes since the last full backup.
**Testing Time**: 3 hours
- Verifying that all changes since the last full backup are backed up and can be restored.
**Deployment Time**: 2 hours
- Setting up and configuring the backup schedules.
**Total Hours**: 11 hours
**Total Cost**: 11 hours * $50/hour = $550
### Reverse Delta Backup
**Development Time**: 12 hours
- Implementing logic to store the latest version and reverse deltas.
**Testing Time**: 6 hours
- Verifying that previous versions can be reconstructed accurately from reverse deltas.
**Deployment Time**: 3 hours
- Setting up and configuring the backup schedules.
**Total Hours**: 21 hours
**Total Cost**: 21 hours * $50/hour = $1050
### Continuous Data Protection (CDP)
**Development Time**: 16 hours
- Implementing continuous monitoring and logging of changes.
**Testing Time**: 8 hours
- Verifying that changes are accurately logged and can be used for rollback.
**Deployment Time**: 4 hours
- Setting up and configuring the continuous data protection system.
**Total Hours**: 28 hours
**Total Cost**: 28 hours * $50/hour = $1400
### Summary Table
| Backup Model | Development Hours | Testing Hours | Deployment Hours | Total Hours | Total Cost |
|-------------------------|-------------------|---------------|------------------|-------------|------------|
| **Full Backup** | 4 | 2 | 1 | 7 | $350 |
| **Incremental Backup** | 8 | 4 | 2 | 14 | $700 |
| **Differential Backup** | 6 | 3 | 2 | 11 | $550 |
| **Reverse Delta** | 12 | 6 | 3 | 21 | $1050 |
| **CDP** | 16 | 8 | 4 | 28 | $1400 |


