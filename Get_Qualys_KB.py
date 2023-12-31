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
    'Authorization': 'Basic [BASE64 USERNAME:PASSWORD]'
}

chunk_size_calc = 20*1024
with requests.request("POST", url, stream=True, headers=headers, data=payload) as r:
    with open(f"qualys_kb_full-{current_date}.xml", "wb") as f:
        for chunk in r.iter_content(chunk_size=chunk_size_calc):
            f.write(chunk)