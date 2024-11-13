def get_absolute_url(url, *args, **kwargs):
    url = url + '/'
    if args:
        url = '/'.join([url.rstrip('/')] + list(args)) 
    if kwargs:
        query_params = '&'.join([f'{key}={value}' for key, value in kwargs.items()])
        url = f'{url}?{query_params}'
    return url

print(get_absolute_url('www.yandex.ru', 'posts', 'news'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))
print(get_absolute_url("www.google.com", id="24"))

