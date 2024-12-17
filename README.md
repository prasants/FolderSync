# FolderClone

FolderClone is a cross-platform directory synchronisation tool. It helps you keep two folders in perfect alignment—copying new or changed files from a source directory to a target directory, and removing files that no longer exist in the source. This makes FolderClone ideal for backups, environment mirroring, and maintaining consistent folder structures across multiple machines.

## Key Features

- **Cross-Platform Compatibility:** Works seamlessly on Windows, macOS, and Linux.
- **Simple CLI Usage:** Just point to a source and destination and run one command.
- **Dry-Run Mode:** Preview changes before committing them, ensuring safety and transparency.
- **Fast and Efficient:** Uses built-in Python modules to perform quick comparisons and synchronisation.
- **Scalable:** Works equally well for small directories or large projects with many files.

## Common Use Cases

1. **Backup and Archiving:** If you want to back up your local project directory to an external folder—perhaps on a network drive or a USB stick—you can run:

   `folderclone /Users/prasant/my_project /Volumes/external_drive/my_project_backup`

   To preview changes without applying them:

   `folderclone /Users/prasant/my_project /Volumes/external_drive/my_project_backup --dry-run`

2. **Dev/Prod Environment Sync:** If you maintain a production environment folder that needs to stay in sync with your local development setup, run:

   `folderclone /Users/prasant/dev_environment /var/www/production_site`

   This ensures newly created or modified files are copied to the production folder, and outdated files are removed, keeping the production environment aligned with your development environment.

3. **Laptop to External Drive:** To keep important documents or research data on your laptop synced to an external SSD, run:

   `folderclone ~/Documents/research_data /Volumes/ssd_backup/research_data`

   If you’re unsure about changes:

   `folderclone ~/Documents/research_data /Volumes/ssd_backup/research_data --dry-run`

   This lets you confirm what will happen before making actual changes.

4. **Shared Workspaces:** For team members who each maintain a local copy of a shared folder stored on a network drive, you can keep your local copy synced with:

   `folderclone /Volumes/team_drive/shared_docs ~/shared_docs_local`

   This ensures your local directory always mirrors the master copy on the team drive.

## Installation

FolderClone uses Python’s standard library, so no extra dependencies are required. To install, run:

`pip install folderclone`

Once installed, run FolderClone by specifying the source and destination directories:

`folderclone /path/to/source /path/to/destination`

Use `--dry-run` to preview changes without making them, ensuring you have full control and confidence in the synchronisation process.
