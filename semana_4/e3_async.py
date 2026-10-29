
import asyncio
import httpx
import time

start = time.time()

async def get_data(client, key, url):
    try:
        response = await asyncio.wait_for(client.get(url), timeout=5)
        print(f'{key} : {response.json()} ')
        return response.json()

    except asyncio.TimeoutError:
        print('La petición tardó más de 5 segundos')


async def main():
    urls = {
        'ip': 'https://httpbin.org/ip',
        'headers': 'https://httpbin.org/headers',
        'user': 'https://jsonplaceholder.typicode.com/users/1',
    }

    async with httpx.AsyncClient() as client:
        result = await asyncio.gather(
            *[get_data(client, keys, url) for keys, url in urls.items()]
        )
    return result

asyncio.run(main())

end = time.time()
print(f'Tiempo: {end - start:.2f} segundos')