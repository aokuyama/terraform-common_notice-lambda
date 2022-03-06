# terraform-common_notice-lambda

archive_fileにsymlinkが使えないのでひとまずコピーで対処
https://github.com/hashicorp/terraform-provider-archive/issues/6
```
cp -r py-slack-common_notice/slack_common_notice app/slack_common_notice
```
