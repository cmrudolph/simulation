#!/usr/bin/env python3

import os
import pprint
import psycopg2

conn_str = os.environ["OWL_POSTGRES_CONN_STR"]
conn = psycopg2.connect(conn_str)
cur = conn.cursor()

with open("results.txt", "r") as fin:
    with open("results_processed.txt", "w") as fout:
        cur.execute("SELECT name, id FROM owl_strategies")
        db_strats = cur.fetchall()
        lookup = {x[0]:x[1] for x in db_strats}

        for line in fin:
            v = line.strip().split(",")
            v[0] = str(lookup[v[0]])
            v[5] = "true" if v[5] == "1" else "false"
            fout.write(",".join(v) + "\n")

cur.close()
conn.close()
