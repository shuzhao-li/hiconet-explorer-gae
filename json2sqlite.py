### dump json data into SQL server
import redis
import json
from model import *

NetworkElement.drop_table()
Community.drop_table()
CommunityMember.drop_table()
MemberData.drop_table()
DB.create_tables([NetworkElement, Community, CommunityMember, MemberData])

with open('result.json') as IN:
    data = IN.readline()
data = json.loads(data)

for e in data['elements']:
    item = e['data']
    E = NetworkElement(name=item['id'])
    if 'classes' in e:
        classes = json.dumps(e['classes'])
        E.classes = classes
    else:
        E.source = item['source']
        E.target = item['target']
        E.weight = item['weight']
    E.save()

for c in data['list_communities']:
    C = Community(name=c)
    C.save()

for c, members in data['community_members'].items():
    for m in members:
        M = CommunityMember(name=m, community=Community.get(Community.name == c))
        M.save()

for c, member_data in data['community_data'].items():
    for item in member_data:
        name = item['name']
        data = json.dumps(item['data'])
        md = MemberData(data = data, member=CommunityMember.get(CommunityMember.name == name))
        md.save()

# HOST = 'localhost'
# PORT = 6379

# r = redis.Redis(host=HOST, port=PORT, db=0)
# with open('result.json') as IN:
#     data = IN.readline()
# data = json.loads(data)
# r.set("elements", json.dumps(data['elements']))
# r.set("list_communities", json.dumps(data['list_communities']))
# r.set()

# # print(data['elements'])
# r.hmset('results', {
#     "elements": json.dumps(data['elements']),
#     "list_communities": json.dumps(data['list_communities']),
#     "community_members": json.dumps(data['community_members']),
# })
# r.set('foo', 'bar')
# print(json.dumps(data['elements']))