# -*- coding: utf-8 -*-
import requests
import json

msg = {
      "ref": "refs/heads/main",
      "before": "7c01dec1006de2e8c445502b351c77c6dfb67dbe",
      "after": "d5f4a4778c39f700622316d2d494d9e7f01ea6b8",
      "repository": {
        "id": 452578900,
        "node_id": "R_kgDOGvnOVA",
        "name": "TempRepo",
        "full_name": "Leozhanggg/TempRepo",
        "private": False,
        "owner": {
          "name": "Leozhanggg",
          "email": "31919498+Leozhanggg@users.noreply.github.com",
          "login": "Leozhanggg",
          "id": 31919498,
          "node_id": "MDQ6VXNlcjMxOTE5NDk4",
          "avatar_url": "https://avatars.githubusercontent.com/u/31919498?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/Leozhanggg",
          "html_url": "https://github.com/Leozhanggg",
          "followers_url": "https://api.github.com/users/Leozhanggg/followers",
          "following_url": "https://api.github.com/users/Leozhanggg/following{/other_user}",
          "gists_url": "https://api.github.com/users/Leozhanggg/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/Leozhanggg/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/Leozhanggg/subscriptions",
          "organizations_url": "https://api.github.com/users/Leozhanggg/orgs",
          "repos_url": "https://api.github.com/users/Leozhanggg/repos",
          "events_url": "https://api.github.com/users/Leozhanggg/events{/privacy}",
          "received_events_url": "https://api.github.com/users/Leozhanggg/received_events",
          "type": "User",
          "site_admin": False
        },
        "html_url": "https://github.com/Leozhanggg/TempRepo",
        "description": "",
        "fork": False,
        "url": "https://github.com/Leozhanggg/TempRepo",
        "forks_url": "https://api.github.com/repos/Leozhanggg/TempRepo/forks",
        "keys_url": "https://api.github.com/repos/Leozhanggg/TempRepo/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/Leozhanggg/TempRepo/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/Leozhanggg/TempRepo/teams",
        "hooks_url": "https://api.github.com/repos/Leozhanggg/TempRepo/hooks",
        "issue_events_url": "https://api.github.com/repos/Leozhanggg/TempRepo/issues/events{/number}",
        "events_url": "https://api.github.com/repos/Leozhanggg/TempRepo/events",
        "assignees_url": "https://api.github.com/repos/Leozhanggg/TempRepo/assignees{/user}",
        "branches_url": "https://api.github.com/repos/Leozhanggg/TempRepo/branches{/branch}",
        "tags_url": "https://api.github.com/repos/Leozhanggg/TempRepo/tags",
        "blobs_url": "https://api.github.com/repos/Leozhanggg/TempRepo/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/Leozhanggg/TempRepo/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/Leozhanggg/TempRepo/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/Leozhanggg/TempRepo/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/Leozhanggg/TempRepo/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/Leozhanggg/TempRepo/languages",
        "stargazers_url": "https://api.github.com/repos/Leozhanggg/TempRepo/stargazers",
        "contributors_url": "https://api.github.com/repos/Leozhanggg/TempRepo/contributors",
        "subscribers_url": "https://api.github.com/repos/Leozhanggg/TempRepo/subscribers",
        "subscription_url": "https://api.github.com/repos/Leozhanggg/TempRepo/subscription",
        "commits_url": "https://api.github.com/repos/Leozhanggg/TempRepo/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/Leozhanggg/TempRepo/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/Leozhanggg/TempRepo/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/Leozhanggg/TempRepo/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/Leozhanggg/TempRepo/contents/{+path}",
        "compare_url": "https://api.github.com/repos/Leozhanggg/TempRepo/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/Leozhanggg/TempRepo/merges",
        "archive_url": "https://api.github.com/repos/Leozhanggg/TempRepo/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/Leozhanggg/TempRepo/downloads",
        "issues_url": "https://api.github.com/repos/Leozhanggg/TempRepo/issues{/number}",
        "pulls_url": "https://api.github.com/repos/Leozhanggg/TempRepo/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/Leozhanggg/TempRepo/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/Leozhanggg/TempRepo/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/Leozhanggg/TempRepo/labels{/name}",
        "releases_url": "https://api.github.com/repos/Leozhanggg/TempRepo/releases{/id}",
        "deployments_url": "https://api.github.com/repos/Leozhanggg/TempRepo/deployments",
        "created_at": 1643267762,
        "updated_at": "2022-01-27T07:16:02Z",
        "pushed_at": 1643274711,
        "git_url": "git://github.com/Leozhanggg/TempRepo.git",
        "ssh_url": "git@github.com:Leozhanggg/TempRepo.git",
        "clone_url": "https://github.com/Leozhanggg/TempRepo.git",
        "svn_url": "https://github.com/Leozhanggg/TempRepo",
        "homepage": "",
        "size": 0,
        "stargazers_count": 0,
        "watchers_count": 0,
        "language": "",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": False,
        "forks_count": 0,
        "mirror_url": "",
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": "",
        "allow_forking": True,
        "is_template": False,
        "topics": [
    
        ],
        "visibility": "public",
        "forks": 0,
        "open_issues": 0,
        "watchers": 0,
        "default_branch": "main",
        "stargazers": 0,
        "master_branch": "main"
      },
      "pusher": {
        "name": "Leozhanggg",
        "email": "31919498+Leozhanggg@users.noreply.github.com"
      },
      "sender": {
        "login": "Leozhanggg",
        "id": 31919498,
        "node_id": "MDQ6VXNlcjMxOTE5NDk4",
        "avatar_url": "https://avatars.githubusercontent.com/u/31919498?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/Leozhanggg",
        "html_url": "https://github.com/Leozhanggg",
        "followers_url": "https://api.github.com/users/Leozhanggg/followers",
        "following_url": "https://api.github.com/users/Leozhanggg/following{/other_user}",
        "gists_url": "https://api.github.com/users/Leozhanggg/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/Leozhanggg/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/Leozhanggg/subscriptions",
        "organizations_url": "https://api.github.com/users/Leozhanggg/orgs",
        "repos_url": "https://api.github.com/users/Leozhanggg/repos",
        "events_url": "https://api.github.com/users/Leozhanggg/events{/privacy}",
        "received_events_url": "https://api.github.com/users/Leozhanggg/received_events",
        "type": "User",
        "site_admin": False
      },
      "created": False,
      "deleted": False,
      "forced": False,
      "base_ref": "",
      "compare": "https://github.com/Leozhanggg/TempRepo/compare/7c01dec1006d...d5f4a4778c39",
      "commits": [
        {
          "id": "d5f4a4778c39f700622316d2d494d9e7f01ea6b8",
          "tree_id": "baf76e071e02bc2a5289e111b7da67cf76d397bf",
          "distinct": True,
          "message": "Update README.md",
          "timestamp": "2022-01-27T17:11:47+08:00",
          "url": "https://github.com/Leozhanggg/TempRepo/commit/d5f4a4778c39f700622316d2d494d9e7f01ea6b8",
          "author": {
            "name": "Leozhanggg",
            "email": "278869269@qq.com",
            "username": "Leozhanggg"
          },
          "committer": {
            "name": "Leozhanggg",
            "email": "278869269@qq.com",
            "username": "Leozhanggg"
          },
          "added": [
    
          ],
          "removed": [
    
          ],
          "modified": [
            "README.md"
          ]
        }
      ],
      "head_commit": {
        "id": "d5f4a4778c39f700622316d2d494d9e7f01ea6b8",
        "tree_id": "baf76e071e02bc2a5289e111b7da67cf76d397bf",
        "distinct": True,
        "message": "Update README.md",
        "timestamp": "2022-01-27T17:11:47+08:00",
        "url": "https://github.com/Leozhanggg/TempRepo/commit/d5f4a4778c39f700622316d2d494d9e7f01ea6b8",
        "author": {
          "name": "Leozhanggg",
          "email": "278869269@qq.com",
          "username": "Leozhanggg"
        },
        "committer": {
          "name": "Leozhanggg",
          "email": "278869269@qq.com",
          "username": "Leozhanggg"
        },
        "added": [
    
        ],
        "removed": [
    
        ],
        "modified": [
          "README.md"
        ]
      }
    }


def gitpush(msg):
    # print(msg)
    repository = msg['repository']['full_name']
    branch = msg['ref'].split('/')[-1]
    pusher = msg['pusher']['name']
    compare_url = msg['compare']
    commit_num = len(msg['commits'])
    timestamp = msg['head_commit']['timestamp']
    # head_id = msg['head_commit']['id'][:8]
    # head_msg = msg['head_commit']['message']
    # title = "【github】{} 提交了 {} 个更新到 {}".format(pusher, num, repository)
    # first_line = "[branch]: {}".format(branch)
    # second_line = "[{}]: {}".format(head_id, head_msg)
    # body = {
    #     "msg_type": "post",
    #     "content": {
    #         "post": {
    #             "zh_cn": {
    #                 "title": title,
    #                 "content": [
    #                     [{"tag": "text", "text": first_line}],
    #                     [{"tag": "text", "text": second_line}],
    #                     [{"tag": "a", "text": "更多>>>", "href": link}]
    #                 ]
    #             }
    #         }
    #     }
    # }

    content = "**{} 提交了 {} 个更新到 {}**".format(pusher, commit_num, repository)
    update_content = "**分支：{}\t时间：{}**".format(branch, timestamp)
    for commit in msg['commits']:
        message = "\n\n[{}]({}) {}".format(commit['id'][:7], commit['url'], commit['message'])
        update_content += message

    body = {
        "msg_type": "interactive",
        "card": {
            "config": {
                "wide_screen_mode": True
            },
            "elements": [
                {
                    "tag": "div",
                    "text": {
                        "content": content,
                        "tag": "lark_md"
                    }
                },
                {
                    "tag": "hr"
                },
                {
                    "tag": "div",
                    "text": {
                        "content": update_content,
                        "tag": "lark_md"
                    }
                },
                {
                    "tag": "hr"
                },
                {
                    "actions": [
                        {
                            "tag": "button",
                            "text": {
                                "content": "查看详情",
                                "tag": "plain_text"
                            },
                            "type": "primary",
                            "url": compare_url
                        }
                    ],
                    "tag": "action"
                }
            ],
            "header": {
                "template": "blue",
                "title": {
                    "content": "【GitHub】",
                    "tag": "plain_text"
                }
            }
        }
    }

    print(body)
    headers = {'Content-Type': 'application/json'}
    url = 'https://open.feishu.cn/open-apis/bot/v2/hook/fd8e512f-93d6-4d93-9ad6-f66988fbfdbb'
    rr = requests.post(url, headers=headers, data=json.dumps(body))
    print(rr.text)
    return body


if '__main__' == __name__:
    gitpush(msg)

