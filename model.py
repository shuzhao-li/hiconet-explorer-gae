from peewee import *
import json

DB = SqliteDatabase('test.db')
class BaseModel(Model):
    class Meta:
        database = DB
# For Network
class NetworkElement(BaseModel):
    name =  CharField(unique=True)
    classes = CharField(default = "[]")
    source = CharField(null = True)
    target = CharField(null = True)
    weight = FloatField(null = True)

    @property
    # serialize for cytoscape
    def cy_serialize(self):
        return {
            "data" : {
                "id": self.name,
                "source": self.source,
                "target": self.target,
                "weight": self.weight
            },
            "classes" : json.loads(self.classes)
        }


class Community(BaseModel):
    name = CharField()

class CommunityMember(BaseModel):
    community = ForeignKeyField(Community, backref='member')
    name = CharField()

class MemberData(BaseModel):
    member = ForeignKeyField(CommunityMember, backref='member_data')
    data = TextField()
    @property
    def serialize(self):
        return {
            'name': self.member.name,
            'data': json.loads(self.data)
        }
        
DB.connect()

# r = NetworkElement.select()
# for item in r:
#     print(json.dumps(item.cy_serialize))