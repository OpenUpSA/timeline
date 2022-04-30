# timeline

Timeline of everything you've been up to across various tools (to figure out how to fill in your timesheet for the last month)

Install at <a href="https://slack.com/oauth/v2/authorize?client_id=3316964946246.3320974157269&scope=&user_scope=search:read"><img alt="Add to Slack" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcSet="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" /></a>

Copy the code from the the (broken) redirect URL querystring and exchange for a token at https://api.slack.com/authentication/oauth-v2#exchanging

Copy the user token into your config file like

```
{
  "slack": {
    "user_token": "...here...",
    "username": "fbloggs"
  },
  "github": {
    "github": {
      "username": "fredbloggs",
      "access_token": "...prersosnal access token"
    }
  }
}
