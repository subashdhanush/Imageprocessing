import asyncio
import datetime

async def task1():
    """A sample task that runs periodically."""
    while True:
        print(f"[{datetime.datetime.now()}] Task 1 is running...")
        await asyncio.sleep(5)  # Runs every 5 seconds

async def task2():
    """Another sample task with a different interval."""
    while True:
        print(f"[{datetime.datetime.now()}] Task 2 is running...")
        await asyncio.sleep(10)  # Runs every 10 seconds

async def main():
    """Main function to run multiple tasks asynchronously."""
    print("🚀 Task Scheduler Started!")
    
    # Create async tasks
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())

    # Run until manually stopped
    await asyncio.gather(t1, t2)

# Run the scheduler
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\n❌ Task Scheduler Stopped!")
