#!/usr/local/bin/python3

import click

"""
Proof of concept using Click. Different options below reflect paradigms
we need for various command line apps
"""

EPILOG='This is my custom epilog'

@click.group(chain=True, epilog=EPILOG)
def cli():
    """ Blah, blah, blah
    A foo that bars
    """

@cli.command(help='Help for Test1')
@click.argument('name', default='Dork')
def test1(name):
    print('This is Test1,', name)

@click.command(help='Help for Test2')
@click.option('--test', '-t', 'test', help='test flag')
@click.option('--verbose', '-v', 'verbose', is_flag=True, help='verbose flag')
def test2(test, verbose):
    if verbose:
        click.echo('Verbose mode...')
    if test:
        click.echo('Test mode...' + str(test))
    click.echo('This is Test2')

@click.command('testing', help='Help for Test3')
@click.password_option()
def test3(password):
    click.echo('This is Test3')
    click.echo(password)

#cli.add_command(test1)
cli.add_command(test2)
cli.add_command(test3)

class cli_test:
    def __init__(self):
        pass
    
    @click.group(chain=True)
    def cli():
        """ blah
        """

    @click.command('test', help='class click test')
    def class_test():
        click.echo('Testing from a class')
    
    cli.add_command(class_test)

#cli()
my_test = cli_test()
my_test.cli()
