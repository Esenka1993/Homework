import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование')
    for ball in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {ball} шар')
    print(f'Силач {name} закончил соревнование')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Дима', 20))
    task2 = asyncio.create_task(start_strongman('Костя', 10))
    task3 = asyncio.create_task(start_strongman('Иван', 13))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())