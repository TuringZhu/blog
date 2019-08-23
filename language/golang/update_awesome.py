#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
# -*- coding: utf-8 -*-

"""
Date: 2019-08-09 08:17
Author: Turing Zhu
File: update_awesome.py
Desc:

问题描述: 自己整理的自己见过的, 可能用的到的 awesome 列表, 定期更新 star 量

格式:

* [Learn Go with TDD](https://github.com/quii/learn-go-with-tests) - Learn Go with test-driven development.  `star 17888` | `fork 2342` |  `issue 2344 open 2344 closed 23243` | `PR 133` | `Commit 534`
"""

import re
import requests
import time
from random import randint


file_path = "./go-awesome.md"
TOKEN = "94831b637be5b5058d7b1b9c599eb7967dbb5b14"


def get_repo_info(string: str) -> dict:
    result = dict()
    regex = re.compile(r"https://github.com/([\w\-]+)/([\w+\-]+)")
    match = regex.search(string.strip())
    if not match:
        return dict()
    result["author"] = match.group(1)
    result["respository"] = match.group(2)

    headers = {
        "Authorization": "token {}".format(TOKEN)
    }
    params = {
        "q": "repo:{}/{}".format(match.group(1),match.group(2))
    }
    url = 'https://api.github.com/search/repositories'

    response = requests.get(url=url, params=params, headers=headers, timeout=30)
    if response.status_code != 200:
        print("status code is not 200" + response.text + match.group(1))
        return result
    if len(response.json()['items']) == 0:
        print("items is 0" + match.group(1))
        return result
    json = response.json()['items'][0]
    result.update({
        "fork": json["forks"],
        "watchers": json["watchers"],
        "star": json["stargazers_count"],
        "desc": json["description"],
        "full_name": json["full_name"],
        "url": json["html_url"],
        "issue": 0,
        "open_issue": json["open_issues"],
        "close_issue": 0,
        "pr": 0,
        "commit": 0
    })
    time.sleep(randint(3, 10))
    return result


def main():
    contents = list()
    with open(file_path) as fp:
        lines = fp.readlines()
        for line in lines:
            info = get_repo_info(line.strip())
            if not info:
                contents.append(line)
                continue
            contents.append(
                "- [{name}]({url}) -  `star {star}` | `fork {fork}` |  "
                "`issue {issue} open {open_issue} closed {close_issue}` | `PR {pr}` | `Commit {commit}`\n".format(
                    name=info["full_name"],
                    url=info["url"],
                    star=info["star"],
                    fork=info["fork"],
                    issue=info["issue"],
                    open_issue=info["open_issue"],
                    close_issue=info["close_issue"],
                    pr=info["pr"],
                    commit=info["commit"])
            )
    with open(file_path, "w") as fp:
        fp.writelines(contents)


if __name__ == '__main__':
    main()
