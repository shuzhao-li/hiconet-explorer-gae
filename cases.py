#
# Not used for now
# 
# 



import datetime

# [START datastore_build_service]
from google.cloud import datastore


def create_client(project_id):
    return datastore.Client(project_id)
# [END datastore_build_service]


# [START datastore_add_entity]
def add_case(client, jid, description):
    key = client.key('Case')

    case = datastore.Entity(
        key, exclude_from_indexes=['json'])

    case.update({
        'created': datetime.datetime.utcnow(),
        'json': description,
        'jid': jid
    })

    client.put(case)

    return case.key
# [END datastore_add_entity]


# [START datastore_update_entity]
def mark_done(client, task_id):
    with client.transaction():
        key = client.key('Task', task_id)
        task = client.get(key)

        if not task:
            raise ValueError(
                'Task {} does not exist.'.format(task_id))

        task['done'] = True

        client.put(task)
# [END datastore_update_entity]


# [START datastore_retrieve_entities]
def list_tasks(client):
    query = client.query(kind='Task')
    query.order = ['created']

    return list(query.fetch())
# [END datastore_retrieve_entities]


# [START datastore_delete_entity]
def delete_task(client, task_id):
    key = client.key('Task', task_id)
    client.delete(key)
# [END datastore_delete_entity]
