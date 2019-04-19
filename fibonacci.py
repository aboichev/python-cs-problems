import sys
from functools import lru_cache
from decorators import print_time
import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--n', default=1, help='0 based index of a fibanacci sequence')
def recursive(n: int)-> int:
    click.echo(_recursive(n))

@print_time
def _recursive(n: int)-> int:
    if n < 2:
        return 1
    return _recursive(n-1) + _recursive(n-2)

@cli.command()
@click.option('--n', default=1, help='0 based index of a fibanacci sequence')
def recursive_cached(n: int)-> int:
    click.echo(_recursive_cached(n))

@lru_cache(maxsize=None)
@print_time
def _recursive_cached(n: int)-> int:
    if n < 2:
        return 1
    return _recursive_cached(n-1) + _recursive_cached(n-2)

@print_time
@cli.command()
@click.option('--n', default=1, help='0 based index of a fibanacci sequence')
def iterative(n: int) -> int:
    click.echo(_iterative(n))

@print_time
def _iterative(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    last = 1
    next = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

if __name__ == "__main__":
     cli()