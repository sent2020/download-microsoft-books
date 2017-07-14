#!/usr/bin/env python

"""
Short Python Script that downloads all the free MSFT eBooks given away by Eric Ligman on July 14th 2017.
LINK:
https://blogs.msdn.microsoft.com/mssmallbiz/2017/07/11/largest-free-microsoft-ebook-giveaway-im-giving-away-millions-of-free-microsoft-ebooks-again-including-windows-10-office-365-office-2016-power-bi-azure-windows-8-1-office-2013-sharepo/?ranMID=24542&ranEAID=lw9MynSeamY&ranSiteID=lw9MynSeamY-I4Ne4ea4zo0cBxSms1JnBg&tduid=%282fa5d78bb69907999f4defb5aa79a64b%29%28256380%29%282459594%29%28lw9MynSeamY-I4Ne4ea4zo0cBxSms1JnBg%29%28%29
"""

import requests
import os

# Variables
directory_name = "MSFT Books"
links_list_url = 'http://ligman.me/2sZVmcG'  # URL that contains url of all the books
print_status = True  # Print the current status of the script

# Create a directory
if not os.path.exists(directory_name):
    os.makedirs(directory_name)
    if print_status:
        print("{} was successfully created.".format(directory_name))

initial_response = requests.get(links_list_url)  # Requesting the list of links
loop = list(initial_response.iter_lines(decode_unicode=True))
# Creates a list of all the links using the the iter_lines method of the Response class (from Requests)

for url in loop[1:]:
    response = requests.get(url)
    book_name = response.url.split("/")[-1]  # Last part of the url is the title of the book

    with open('{}/{}'.format(directory_name, book_name), 'wb') as bin_file:  # Writing the file using open function
        bin_file.write(response.content)

    if print_status:
        print("{} was downloaded.".format(book_name))
