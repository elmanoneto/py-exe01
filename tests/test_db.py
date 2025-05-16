from example01.db import add_user, get_users, delete_user

def test_insert_and_list(connect_db):
    add_user(connect_db, "Joao")
    add_user(connect_db, "Maria")
    result = get_users(connect_db)
    nomes = [r[0] for r in result]

    assert nomes == ["Joao", "Maria"]
    
def test_delete_user(connect_db):
    add_user(connect_db, "Joao")
    add_user(connect_db, "Maria")
    add_user(connect_db, "Pedro")
    delete_user(connect_db, 2)
    result = get_users(connect_db)
    nomes = [r[0] for r in result]

    assert nomes == ["Joao", "Pedro"]