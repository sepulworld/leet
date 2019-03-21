import pytest

def numUniqueEmails(emails):
    unique_emails = set()
    
    for i in emails:
        true_handle, domain = i.split('@')
        if "+" in true_handle:
            true_handle = true_handle.split('+')[0]
        if "." in true_handle:
            true_handle = true_handle.replace('.', "")
        email = true_handle + "@" + domain
        unique_emails.add(email)
    
    return len(unique_emails)

assert numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]) == 2
