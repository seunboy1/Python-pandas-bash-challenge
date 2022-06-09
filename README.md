

create a bash script that

- recursively lists all files and file sizes in an arbitrary directory
- saves this output to a file in a format that can be read by a pandas dataframe

write a python script that:

- load this file into a pandas dataframe and calcualte and print out the
   - average file size
   - the biggest file
   - the smallest file
   - histogram of file sizes


create an HTTP server in python that

   - accepts a zip file that is a directory
   - uses the previously created bash and python scripts on the uploaded directory
   - returns the output in a json format


As part of the submission, identify any architectural or security issues as well as improvements that you would like to make in the future.
