import requests
import os

# Variables
directory_name = "MSFT Books"
list_links_url = 'http://ligman.me/2sZVmcG'
print_status = True  # Print the current status of the script

# Create a directory
if not os.path.exists(directory_name):
    os.makedirs(directory_name)
    if print_status:
        print("{} was successfully created.".format(directory_name))

# Requesting the list of links
response = requests.get(list_links_url)
loop_ls = list(response.iter_lines(decode_unicode=True))

for line in loop_ls[1:3]:
    url = line

    temp_response = requests.get(url)
    book_name = temp_response.url.split("/")[-1]

    with open('{}/{}'.format(directory_name, book_name), 'wb') as f:
        f.write(temp_response.content)

    if print_status:
        print("{} was downloaded".format(book_name))
