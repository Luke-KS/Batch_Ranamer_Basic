import os

# to be replaced string and file extension filter


search = "file"
replace = "document"

# get all files from current directory
dir_content = os.listdir('.')
docs = [doc for doc in dir_content if os.path.isfile(doc)]
renamed = 0

print(f"{len(docs)} of {len(dir_content)} elements are files")

# go through all the files and check if they match the search pattern
for doc in docs:
    # check if search text us ub doc name
    if search in doc:

        # replace with the given text
        new_name = doc.replace(search, replace)
        # os.rename(doc, new_name)
        renamed += 1

        print(f"Renamed file {doc} to {new_name}.")