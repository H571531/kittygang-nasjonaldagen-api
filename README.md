# kittygang-nasjonaldagen-api
Shit happens

## Eksempeler
### Powershell Invoke-RestMethod
```PowerShell
$body = @{
 "who"="noen"
 "what"="noe"
} | ConvertTo-Json
Invoke-RestMethod -Uri "url:1705/register" -Method 'Post' -Body $body -ContentType application/json
```
### Curl
```Bash
curl -H 'Content-Type: application/json' -d '{ "who":"noen","what":"noe"}' -X POST http://url:1705/register
```
