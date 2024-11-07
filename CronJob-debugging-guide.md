# Cron Job Debugging Guide

This guide will help you troubleshoot and debug cron job issues, specifically when executing Python scripts.

## Summary

1. [Check the cron log file](#1-check-the-cron-log-file)
2. [Add Output Redirection to Logs](#2-add-output-redirection-to-logs)
3. [Check the Full Python Path](#3-check-the-full-python-path)
4. [Permissions](#4-permissions)
5. [Check the cron environment](#5-check-the-cron-environment)
6. [Test Manually](#6-test-manually)
7. [Restart the cron service (if necessary)](#7-restart-the-cron-service-if-necessary)

---

## 1. Check the cron log file

Cron might be failing silently. To check if cron attempted to run the job, review the cron log in `/var/log/syslog` (for Debian/Ubuntu-based systems). You can search for cron-related entries with:

```bash
grep CRON /var/log/syslog
```

This will show all cron execution attempts. If the cron job failed, you'll see a message indicating the error.

[Back to Top](#summary)

## 2. Add Output Redirection to Logs

To help with debugging, add output redirection (both `stdout` and `stderr`) to a log file. This will capture any errors or messages cron is generating. Modify your cron job like this:

```plaintext
25 13 * * * /usr/bin/python3 /home/andreza/automatization_scripts/ubuntu-manage/clean_cache.py >> /home/andreza/automatization_scripts/cron_job.log 2>&1
```

This will cause cron to capture all output (both normal and errors) and save it in `/home/your-user/cron_job.log`. After the scheduled time, you can check this file to see what happened.

[Back to Top](#summary)

## 3. Check the Full Python Path

Even though you're using the full path to Python (`/usr/bin/python3`), it's a good idea to make sure cron is using the correct Python version. Check where `python3` is installed in your terminal:

```bash
which python3
```

This should return the path to the Python executable, which should match the one used in the cron job. If it's different, update the cron job line to use the correct path.

[Back to Top](#summary)

## 4. Permissions

Ensure that the script has the correct permissions to be executed, as mentioned before:

```bash
chmod u+x /home/andreza/automatization_scripts/ubuntu-manage/clean_cache.py
```

Also, if the script requires `sudo` permissions to run certain commands (such as clearing caches or disabling swap), make sure you have configured cron to run as root or have set the appropriate permissions for the user.

[Back to Top](#summary)

## 5. Check the cron environment

Cron runs in a more restricted environment than an interactive shell. Make sure your script doesn't depend on environment variables that aren't set in the cron environment. You can explicitly add environment variables within the crontab, like this:

```plaintext
25 13 * * * export PATH=$PATH:/usr/bin && /usr/bin/python3 /home/andreza/automatization_scripts/ubuntu-manage/clean_cache.py
```

This ensures that cron has the correct path for the Python executable and any other necessary commands.

[Back to Top](#summary)

## 6. Test Manually

Try running the cron job manually in the terminal with the exact command from your crontab to check if it works correctly:

```bash
/usr/bin/python3 /home/andreza/automatization_scripts/ubuntu-manage/clean_cache.py
```

If it works fine manually but not via cron, the issue might be related to the cron environment.

[Back to Top](#summary)

## 7. Restart the cron service (if necessary)

In some cases, it may help to restart the cron service to ensure changes to the crontab are applied:

```bash
sudo systemctl restart cron
```

[Back to Top](#summary)

---

After these checks, try again and see if the cron job runs as expected. If there are still issues, refer to the logs generated in the log file for more information.
