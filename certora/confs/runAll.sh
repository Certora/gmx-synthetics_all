#!/bin/bash

# Get a list of all .conf files
CONF_FILES=$(ls certora/confs/*.conf)

# Iterate over each .conf file
for CONF_FILE in $CONF_FILES; do
    echo "Executing $CONF_FILE..."
    
    # Execute certoraRun with the current .conf file
    certoraRun "certora/confs/$CONF_FILE"
    
    echo "Done executing $CONF_FILE."
    echo
done

# Return to the original directory
cd -