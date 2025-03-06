import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} completed after {delay} seconds")

async def main():
    await asyncio.gather(task("Task 1", 2), task("Task 2", 3))

asyncio.run(main())
