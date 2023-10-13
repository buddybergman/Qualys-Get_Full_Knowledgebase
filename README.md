This is a Python script that will pull the entire Qualys Knowledgebase.  It is based on the example provided in [this Qualys blog](https://blog.qualys.com/product-tech/2021/03/02/qualys-api-best-practices-knowledgebase-api), but of course they only put screenshots so you can't copy and paste. 

I've also adjusted it to include the current date in the output filename. 

Note that you can add/remove payload details in the code as you see fit. 

--------------------------------------------------
### BASE64 Encoding Your Username:Password

Your Qualys username and password should be used in the Authorization header field as: Basic abcDEFghiJKLmnoPQRstuVWXyz012345

You can use the online converter https://www.base64encode.org and convert the string

--------------------------------------------------

### As of 10/13/2023, the KB XML filesize is about 569MB. 

### Code:  
```
import requests
from datetime import datetime

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

url = "https://[YOUR API URL]/api/2.0/fo/knowledge_base/vuln/"

payload = {'action': 'list',
           'show_disabled_flag': '1',
           'details': 'All',
           'show_qid_change_log': '0',
           'show_supported_modules_info': '1'}

headers = {
    'X-Requested-With': 'Extract',
    'Authorization': 'Basic [BASE64 USER:PASSWORD]'
}

chunk_size_calc = 20*1024
with requests.request("POST", url, stream=True, headers=headers, data=payload) as r:
    with open(f"qualys_kb_full_{current_date}.xml", "wb") as f:
        for chunk in r.iter_content(chunk_size=chunk_size_calc):
            f.write(chunk)

```
--------------------------------------------------
