#! /usr/bin/env python3

from brain_games.cli import welcome_user


def welcome_brain_games():
    print("Welcome to Brain Games!")


def main():
    welcome_brain_games()
    welcome_user()


if __name__ == "__main__":
    main()