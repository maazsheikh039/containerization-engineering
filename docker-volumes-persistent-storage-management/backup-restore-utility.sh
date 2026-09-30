#!/bin/bash
# Production Docker Volume Backup and Restore Automation
ACTION=$1
VOLUME_NAME=$2
TARGET_PATH=${3:-$(pwd)}

if [ "$ACTION" == "backup" ]; then
    echo "[+] Creating compressed backup archive for volume: $VOLUME_NAME..."
    docker run --rm -v ${VOLUME_NAME}:/data -v ${TARGET_PATH}:/backup ubuntu:20.04 \
      tar czf /backup/${VOLUME_NAME}-backup.tar.gz -C /data .
    echo "[+] Backup saved to: ${TARGET_PATH}/${VOLUME_NAME}-backup.tar.gz"

elif [ "$ACTION" == "restore" ]; then
    NEW_VOL=$3
    ARCHIVE_FILE=$4
    echo "[+] Restoring $ARCHIVE_FILE into new volume $NEW_VOL..."
    docker volume create $NEW_VOL
    docker run --rm -v ${NEW_VOL}:/data -v $(dirname $(realpath $ARCHIVE_FILE)):/backup ubuntu:20.04 \
      bash -c "cd /data && tar xzf /backup/$(basename $ARCHIVE_FILE)"
    echo "[+] Data successfully restored to volume: $NEW_VOL"
else
    echo "Usage: ./backup-restore-utility.sh [backup|restore] [volume_name] [target_path_or_new_vol] [archive_file]"
fi
