#!/bin/bash
# Set the path.
PATH=/sbin:/bin:/usr/bin:/usr/sbin

if [ -x /sbin/quotacheck ]; then
    echo -n "Checking quotas: "
    /sbin/quotacheck -avug 
    echo Done
fi