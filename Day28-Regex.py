#!/bin/python3

import re

if __name__ == '__main__':
    N = int(input())
    name_list = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        regexString = "([a-zA-Z0-9]+)@(gmail.com)"
        x = re.search(regexString, emailID)
        if x is not None:
            name_list.append(firstName)
    name_list.sort()
    for i in range((len(name_list))):
        print(name_list[i])