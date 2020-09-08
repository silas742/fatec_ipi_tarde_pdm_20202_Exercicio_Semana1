import sys
import traceback
from itertools import groupby

users = [
    {id: 0, "name": "Silas" },
    {
        id: 1, "name": "Jackson"
    },
    {id: 2, "name": "Erick"},
    {id: 3, "name": "Prado"},
    {id: 4, "name": "Jeff"},
    {id: 5, "name": "Andre"},
    {id: 6, "name": "Marcos"},
    {id: 7, "name": "mimi"}

]
Dicionario = [
     (2, 3), (1, 2), (4, 3), (0, 5), (1, 3), (1, 5), (5, 3), (0, 7)


]


for user in users:
    user["sexo"] = []
    user["idade"] = []

for i, j in Dicionario:
    users[i]["sexo"].append(users[j])
    users[j]["sexo"].append(users[i])

    users[i]["idade"].append(users[j])
    users[j]["idade"].append(users[i])




def number_of_idade(user):
    return len(user['idade'])

def number_of_users_sexo(user):
    return len(user['sexo'])

Conecctions = sum(number_of_idade(user) for user in users) and sum(number_of_users_sexo(user) for user in users)

num_users = len(users)
div_connections = Conecctions / num_users



