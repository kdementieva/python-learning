import requests

response = requests.get('https://google.com')

if response.status_code == 200:
    print('Запрос выполнен успешно')
else:
    print('Произошла ошибка:', response.status_code)

# print(response.text)
# print(response.headers)
content_type = response.headers['Content-Type']
print(content_type)