#!/usr/bin/env python3

import os
import pprint
import psycopg2

conn_str = os.environ["OWL_POSTGRES_CONN_STR"]
conn = psycopg2.connect(conn_str)
cur = conn.cursor()

with open("strategies.txt", "r") as f:
    for line in f:
        line = line.strip()
        name, friendly = [x.strip() for x in line.split("|")]

        q = (f"INSERT INTO owl_strategies (name, friendly_name) "
            f"SELECT '{name}', '{friendly}' "
            f"ON CONFLICT DO NOTHING ")
        cur.execute(q)

conn.commit()

cur.close()
conn.close()
