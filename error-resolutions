# ERROR RESOLUTIONS
## How to fix Password authentication was removed in Github
### Error
```
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/Parcelli/Data_Mining.git/'
```
### Solution
* Step One : Create a Personal Access Token on Github
- Click on your GitHub profile icon on the top right corner
- Click Settings
- From the menu shown on the left, click Developer Settings
- Click Personal access tokens
- Click Generate new token
- Add a note that will help you identify the scope of the access token to be generated
- Choose the Expiration period from the drop down menu (Ideally you should avoid choosing the No Expiration option)
- Finally, select the scopes you want to grant the corresponding access to the generated access token.
- Finally click Generate Token

* Step Two : Change repository URL
```
git remote set-url origin https://<githubtoken>@github.com/<username>/<repositoryname>.git
```
Replace : 
- <githubtoken> with the personal access token you have copied in the previous step
- <username> with your GitHub username
- <repositoryname> with the name of your GitHub repository

* Test that it works
Try to push changes from local to remote

```
git push -u origin main
```

