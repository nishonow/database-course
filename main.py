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

    # await db.update_student(1, "Crowley")
    # students = await db.show_students()
    # print(students)

    # await db.add_student_course(1,2)
    # await db.add_student_course(1,3)

    # students_courses = await db.show_students_courses(1)
    # print(students_courses)

    # students_count = await db.count_students()
    # courses_count = await db.count_courses()
    # print(students_count, courses_count)

    # all_students_with_courses = await db.get_all_students_with_courses()
    # print(all_students_with_courses)

    get_student_course_count = await db.get_student_course_count()
    print(get_student_course_count)
    await db.close()

asyncio.run(main())
