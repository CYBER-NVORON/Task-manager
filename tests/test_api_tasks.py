def login(client):
    client.post('/login', data={
        'username': 'testuser',
        'password': 'password'
    })


def test_create_task(client):
    login(client)

    response = client.post('/api/tasks', json={
        'title': 'Test Task'
    })

    assert response.status_code == 201
    assert response.json['title'] == 'Test Task'


def test_get_tasks(client):
    login(client)

    response = client.get('/api/tasks')

    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_update_task(client):
    login(client)

    task = client.post('/api/tasks', json={'title': 'Old'})
    task_id = task.json['id']

    response = client.put(f'/api/tasks/{task_id}', json={
        'title': 'New',
        'done': True
    })

    assert response.status_code == 200


def test_delete_task(client):
    login(client)

    task = client.post('/api/tasks', json={'title': 'Delete me'})
    task_id = task.json['id']

    response = client.delete(f'/api/tasks/{task_id}')

    assert response.status_code == 200
