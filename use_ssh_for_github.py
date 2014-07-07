from subprocess import check_output
import os
import re

def get_remote_url():
    output = check_output("git remote -v|grep push", shell=True)
    return output

def get_username_and_repository_from_http_url(url):
    result = re.search('https://github.com/(?P<username>\w+)/(?P<respository>\w+)(\.git)?', url)
    if result:
        return result.groupdict()
    return None
url = get_remote_url()
git_info = get_username_and_repository_from_http_url(url)
os.system("git remote set-url origin git@github.com:%s/%s.git" % (git_info['username'], git_info['respository']))

