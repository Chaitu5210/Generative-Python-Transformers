#import required 
import os
import time
from datetime import datetime                        
from github import Github 


# using the given Token
Access_Token=open("E:\Generative Python Transformers\Token.txt","r").read()
git=Github(Access_Token)


#   Phase 1 -- Collecting The Data From GitHub
end_time=time.time()
start_time=end_time-86400




start_time_str=datetime.utcfromtimestamp(start_time).strftime('%y-%m-%d')
end_time_str=datetime.utcfromtimestamp(end_time).strftime('%y-%m-%d')
query=f"language:python created:2024-01-09..2024-01-10"
print(query)
start_time=start_time-86400
end_time=end_time-86400
result=git.search_repositories(query)
print(result.totalCount)
for repo in result:
        os.system(f"git clone {repo.clone_url} UncleanedData/{repo.owner.login}/{repo.name}")

