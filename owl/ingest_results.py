#!/usr/bin/env python3

import os
import pprint
import psycopg2

conn_str = os.environ["OWL_POSTGRES_CONN_STR"]
conn = psycopg2.connect(conn_str)
cur = conn.cursor()

with open("results_processed.txt", "r") as f:
    cur.copy_from(f, "owl", sep=",", columns=("strategy", "players", "owls", "actions", "suns", "won", "elapsed"))

conn.commit()

cur.close()
conn.close()
