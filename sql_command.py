import click
import subprocess


# @click.command()
# def command_note():
#     click.echo("this is sql migrate command")


@click.command()
def sql_command():
    # run flask db migrate
    try:
        subprocess.run(["flask", "db", "migrate"], check=True)
        click.echo("Database migration successful.")
    except subprocess.CalledProcessError:
        click.echo("Database migration failed.")

    # run flask db upgrade
    try:
        subprocess.run(["flask", "db", "upgrade"], check=True)
        click.echo("Database upgrade successful.")
    except subprocess.CalledProcessError:
        click.echo("Database upgrade failed.")


if __name__ == '__main__':
    sql_command()
