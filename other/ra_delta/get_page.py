import time
# import requests
#
#
# def get_page(category: str, page_id: int) -> str:
#     if page_id:
#         url = 'https://www.ozon.ru/brand/{0}/?page={1}'.format(category, page_id)
#     else:
#         url = 'https://www.ozon.ru/brand/{0}/'.format(category)
#     print('get url: {0}'.format(url))
#     response = requests.get(url)
#     return response.text
#
#
# def load_data():
#     category_list = ['adidas-144082850', 'puma-87235756']
#     for category in category_list:
#         for page_id in range(50):
#             text = get_page(category, page_id)
#             # обрабатываем полученный текст, сохраняем в файл/базу
#
#
# if __name__ == '__main__':
#     start_load_data = time.time()
#     load_data()
#     end_load_data = time.time()
#     print(f'Однопоточное вычисление заняло {end_load_data - start_load_data:.4f} с.')

# После
import aiohttp
import asyncio


async def get_page_new(session, category: str, page_id: int) -> str:
    url = f'https://www.ozon.ru/brand/{category}/?page={page_id}' if page_id else f'https://www.ozon.ru/brand/{category}/'
    async with session.get(url) as response:
        return await response.text()


async def load_data_new():
    category_list = ['adidas-144082850', 'puma-87235756']
    async with aiohttp.ClientSession() as session:
        tasks = []
        for category in category_list:
            for page_id in range(50):
                task = asyncio.ensure_future(get_page_new(session, category, page_id))
                tasks.append(task)
                pages = await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_load_data_new = time.time()
    asyncio.run(load_data_new())
    end_load_data_new = time.time()
    print(f'Однопоточное вычисление заняло {end_load_data_new - start_load_data_new:.4f} с.')
