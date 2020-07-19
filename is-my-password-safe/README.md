# IS MY PASWORD SAFE

### What is it

Return how many times a password has been leaked. It uses haveibeenpwned API.

### Amazon Lambda

Send a HTTP Post to the below AWS Lambda

API link: https://1lt61j4agg.execute-api.sa-east-1.amazonaws.com/prod/check-password

#### Input
```
{
    "password": "Password1"
}
```
#### Output
```
{
    "password": "Password1",
    "occurrences": "118930",
    "sha1": "70CCD9007338D6D81DD3B6271621B9CF9A97EA00"
}
```