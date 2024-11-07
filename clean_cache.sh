#!/bin/bash

# Path to the log file in your home directory
LOG_FILE="$HOME/clear_cache.log"

# Function to log messages
log() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" >> $LOG_FILE
}

# Clear RAM Cache/Buffer
log "Starting to clear RAM Cache and Buffers..."
sync; echo 3 > /proc/sys/vm/drop_caches && log "RAM Cache cleared successfully." || log "Failed to clear RAM Cache."

# To clear the disk space consumed by SWAP:
# Make sure you have enough free RAM before executing this command! 
# Otherwise, your Linux system may completely freeze due to resource starvation.
# In case this happens, use the REISUB!
# Clear SWAP
log "Starting to clear SWAP..."
swapoff -a && swapon -a && log "SWAP cleared successfully." || log "Failed to clear SWAP."

# Completion message
log "Cleanup task completed."
cat $LOG_FILE