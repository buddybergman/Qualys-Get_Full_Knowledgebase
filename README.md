>[!NOTE]
>You need an active Qualys subscription to proceed with the information below

------------------------------------------------

This is a Python script that will pull the entire Qualys Knowledgebase.  It is based on the example provided in [this Qualys blog](https://blog.qualys.com/product-tech/2021/03/02/qualys-api-best-practices-knowledgebase-api), but of course they only put screenshots so you can't copy and paste. 

I've also adjusted it to include the current date in the output filename. 

As of 10/13/2023, the KB XML filesize is about 569MB.

--------------------------------------------------

### Determine your API URL

You can get your API URL here: https://www.qualys.com/platform-identification/

Update the "url" line of the script with the correct one for you.

--------------------------------------------------

### BASE64 Encoding Your Username:Password

Your Qualys username and password should be used in the Authorization header field in the script as: 
```
Basic abcDEFghiJKLmnoPQRstuVWXyz012345
```

You can use the online converter https://www.base64encode.org to convert the string

Replace **[BASE64 USER:PASSWORD]** in the script with **[your BASE64 String]**

