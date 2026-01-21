import asyncio
from database import Database
from dotenv import load_dotenv
import os

load_dotenv()
DB_URL = os.getenv('DBURL')

async def main():
    db = Database(DB_URL)
    await db.connect()

    await db.create_tables()

    # await db.add_student("Sam")
    # await db.add_student("Dean")
    # await db.add_student("Castiel")
    #
    # await db.add_course("Database")
    # await db.add_course("OOP")
    # await db.add_course("Operating Systems")

    # await db.drop_tables()
    students = await db.show_students()
    print(students)

    await db.close()

asyncio.run(main())
