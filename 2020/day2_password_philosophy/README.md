## Day 2

build image with pytest

```sh
docker build -t python:aoc2020 -f ../../Dockerfile .
```

from within this directory

To run tests

```sh
docker run -it --rm=true -e LANG=C.UTF-8 -e TZ='US/Pacific' -v $PWD:$PWD -w $PWD python:aoc2020 pytest
```

To run code
```sh
docker run -it --rm=true -e LANG=C.UTF-8 -e TZ='US/Pacific' -v $PWD:$PWD -w $PWD python:aoc2020 bash -c 'cat input/real.txt | ./password_philosophy.py'
```
