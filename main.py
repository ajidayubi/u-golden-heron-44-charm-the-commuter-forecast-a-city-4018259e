#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for a city
that does not exist to /output/entry.txt.

The line names an invented city, gives it weather as the whole point, and
charms a bored commuter with one turn of phrase: the buses run on time
today, so the commuter's excuses will have to walk. The weather half keeps
the rhythm of a real broadcast forecast ("drizzle till nine, then
sunshine"), bent just enough to smile.
"""

import os

FORECAST = (
    "In Drowsywick, drizzle till nine, then sunshine "
    "\u2014 the buses run on time today, "
    "so your excuses will have to walk."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORECAST + "\n")


if __name__ == "__main__":
    main()
