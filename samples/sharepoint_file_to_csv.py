# pip install Office365-REST-Python-Client
from office365.runtime.auth.client_credential import ClientCredential
from office365.sharepoint.client_context import ClientContext

SHAREPOINT_CLIENT_ID = ""
SHAREPOINT_CLIENT_SECRET = ""
SHAREPOINT_SITE_URL = ""
SHAREPOINT_FILE_URL = ""

client_credentials = ClientCredential(
    client_id=SHAREPOINT_CLIENT_ID,
    client_secret=SHAREPOINT_CLIENT_SECRET)
ctx = ClientContext(SHAREPOINT_SITE_URL).with_credentials(client_credentials)

sharepoint_file = ctx.web.get_file_by_guest_url(SHAREPOINT_FILE_URL)

with open("tm1_data.csv", "wb") as file:
    sharepoint_file.download(file).execute_query()
