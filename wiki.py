"""download wiki files from the API and write them to the source_documents folder"""
import os
import json
from urllib.request import Request, urlopen
from dotenv import load_dotenv

load_dotenv()

HEADERS = {
    'X-BOT-IMPERSONATING': os.getenv("DISCORD_ADMIN_USER_ID"),
    'X-BOT-TOKEN': os.getenv("DISCORD_BOT_TOKEN"),
}

# fetch the list of articles from the API
CAMPAIGN = "axis-srd"
DOMAIN = "nerdrage.dev"
DOC_TYPE = "articles"
FIELDS = ["name", "slug", "jsx", "createdBy", "lastUpdatedBy"]

# create a request with headers
query = Request(
  url=f"https://{CAMPAIGN}.{DOMAIN}/api/{DOC_TYPE}?fields={','.join(FIELDS)}",
  headers=HEADERS
)

# fetch the data
with urlopen(query) as request:
  articles = json.load(request)
  print(articles)

# iterate over the list of articles and write out an HTML file for each entry
for article in articles:
  f = open(f"./source_documents/{article['slug']}.html", "w", encoding="utf-8")
  f.write(f"""
<html>
  <head><title>{article['name']}</title></head>
  <body>{article['jsx']}</body>
</html>""")
  f.close()
