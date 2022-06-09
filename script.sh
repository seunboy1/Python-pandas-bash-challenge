#!/bin/bash

# recursively lists all files and file sizes in a directory
list_dir(){

    DIR=assets/file

    if [ -f assets/file.csv ]
    then 
        rm -rf assets/file.csv
        find "$DIR" -type f -exec stat -f '%N,%z' '{}' >> assets/file.csv +

    else
        find "$DIR" -type f -exec stat -f '%N,%z' '{}' >> assets/file.csv +
    fi

    echo "Successfully extracted directory information!!!"

}

list_dir
exit 0
