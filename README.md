## This is a repo for Database course weekly labs
---
### 3. Basic Operations
- Implemenented `CREATE TABLE`, `SELECT *` and `DROP TABLE` operations.

### 4. Basic table operations
- Implemented `INSERT`, `DELETE` operations, `SELECT` with `WHERE` clause and simple conditions.

### 5. No need since it is in railway

### 6. TABLE operations
- Implemented `ALTER TABLE` operation.

### 7. Primark key
- Implemented `PK` constraints for each tables.

### 8. Foreign keys
- Implemented `REFERENCES` FK to `student_courses` table.

### 9. Database Design. 
- Implemented necessary tables structure with corrresponding PK and FK constraints.

### 10. Viewing tables
- Implemented `show_students` to view the entrie `students` table.

### 11.Basic data queries
- Implemented basic `SELECT` queries with `WHERE` clause.

### 12. Querying data
- Implemented more complex `SELECT` queries with `JOIN` operations.

### 13. Aggregate functions
- Implemented `COUNT` aggregate for now.

### 14. Joining 
- Implemented `LEFT JOIN` for returning all rows. `INNER JOIN` to return only rows where there is a match in both tables.

### 15. Advanced operations
- Implemented `GROUP BY` to get all students with their courses count.

### 16. Transactions
- Implemented `UPDATE` to update user balances in another table. Here is the code:
```python
    async def add_user_balance(self, user_id, amount):
        async with self.acquire_connection() as conn:
            await conn.execute(
                "UPDATE users SET balance = balance + $1 WHERE id = $2",
                amount, user_id
            )
```

### 17. Export/Import Backup
- Not implemented in this code but did it with pgAdmin and implemented export in another database. Here is the code:
```python
    async def export_backup(self):
        async with self.acquire_connection() as conn:
            backup_lines = []
            backup_lines.append(f"-- Database Backup - {datetime.utcnow().isoformat()}")
            backup_lines.append("-- Tables: users, presentations, referats, bot_status, revenue\n")
            
            backup_lines.append("-- USERS TABLE")
            users = await conn.fetch("SELECT * FROM users ORDER BY id")
            for user in users:
                cols = ", ".join(user.keys())
                vals = []
                for v in user.values():
                    if v is None:
                        vals.append("NULL")
                    elif isinstance(v, str):
                        vals.append(f"'{v.replace(chr(39), chr(39)+chr(39))}'")
                    elif isinstance(v, datetime):
                        vals.append(f"'{v.isoformat()}'")
                    elif isinstance(v, bool):
                        vals.append("TRUE" if v else "FALSE")
                    else:
                        vals.append(str(v))
                backup_lines.append(f"INSERT INTO users ({cols}) VALUES ({', '.join(vals)}) ON CONFLICT (id) DO NOTHING;")
            
            backup_lines.append("\n-- PRESENTATIONS TABLE")
            presentations = await conn.fetch("SELECT * FROM presentations ORDER BY id")
            for pres in presentations:
                cols = ", ".join(pres.keys())
                vals = []
                for v in pres.values():
                    if v is None:
                        vals.append("NULL")
                    elif isinstance(v, str):
                        vals.append(f"'{v.replace(chr(39), chr(39)+chr(39))}'")
                    elif isinstance(v, datetime):
                        vals.append(f"'{v.isoformat()}'")
                    else:
                        vals.append(str(v))
                backup_lines.append(f"INSERT INTO presentations ({cols}) VALUES ({', '.join(vals)}) ON CONFLICT (id) DO NOTHING;")
            
            backup_lines.append("\n-- REFERATS TABLE")
            referats = await conn.fetch("SELECT * FROM referats ORDER BY id")
            for ref in referats:
                cols = ", ".join(ref.keys())
                vals = []
                for v in ref.values():
                    if v is None:
                        vals.append("NULL")
                    elif isinstance(v, str):
                        vals.append(f"'{v.replace(chr(39), chr(39)+chr(39))}'")
                    elif isinstance(v, datetime):
                        vals.append(f"'{v.isoformat()}'")
                    else:
                        vals.append(str(v))
                backup_lines.append(f"INSERT INTO referats ({cols}) VALUES ({', '.join(vals)}) ON CONFLICT (id) DO NOTHING;")
            
            backup_lines.append("\n-- BOT_STATUS TABLE")
            bot_status = await conn.fetch("SELECT * FROM bot_status ORDER BY id")
            for status in bot_status:
                cols = ", ".join(status.keys())
                vals = []
                for v in status.values():
                    if v is None:
                        vals.append("NULL")
                    elif isinstance(v, str):
                        vals.append(f"'{v.replace(chr(39), chr(39)+chr(39))}'")
                    elif isinstance(v, bool):
                        vals.append("TRUE" if v else "FALSE")
                    else:
                        vals.append(str(v))
                backup_lines.append(f"INSERT INTO bot_status ({cols}) VALUES ({', '.join(vals)}) ON CONFLICT (id) DO UPDATE SET presentations_enabled = EXCLUDED.presentations_enabled, referats_enabled = EXCLUDED.referats_enabled, gemini_model = EXCLUDED.gemini_model;")
            
            backup_lines.append("\n-- REVENUE TABLE")
            revenue_records = await conn.fetch("SELECT * FROM revenue ORDER BY id")
            for rec in revenue_records:
                cols = ", ".join(rec.keys())
                vals = []
                for v in rec.values():
                    if v is None:
                        vals.append("NULL")
                    elif isinstance(v, str):
                        vals.append(f"'{v.replace(chr(39), chr(39)+chr(39))}'")
                    elif isinstance(v, datetime):
                        vals.append(f"'{v.isoformat()}'")
                    else:
                        vals.append(str(v))
                backup_lines.append(f"INSERT INTO revenue ({cols}) VALUES ({', '.join(vals)}) ON CONFLICT (id) DO NOTHING;")
            
            return "\n".join(backup_lines)
```

---

### The final project repo is [here](https://github.com/nishonow/online-shop).