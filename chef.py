import whois
import sys
import os
import subprocess

def Check(domains,org):
    errors = []
    for domain in domains:
        try:
            whois=GetWhois(domain)
            if(org.lower() in whois.org.lower()):
                print domain       
        except:
            errors.append(domain)
    return errors


def GetWhois(domain):
    return whois.whois(domain)


def OpenFile(fileName):
    with open(fileName) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        return content  

def main():
    if len(sys.argv) != 3:
        print ('[+] usage: <filename> <org>')       
        sys.exit(-1)

    filename = sys.argv[1]
    org = sys.argv[2]
    domains = OpenFile(filename)
    errors = Check(domains,org)
    print('\n\n')
    print("[+] ERRORS:" )
    print errors


if __name__ == "__main__":     
    main()
