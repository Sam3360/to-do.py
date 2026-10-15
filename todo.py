#!/usr/bin/env python3
"""A simple command-line to-do list."""

import json
import os
from pathlib import Path

FILE = Path("tasks.json")


def load_tasks():
    if FILE.exists():
        with FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet. Add one!")
        return

    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")


def add_task(tasks):
    title = input("Enter a task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("Task added.")


def complete_task(tasks):
    show_tasks(tasks)
    try:
        number = int(input("Task number to complete: "))
        tasks[number - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as complete.")
    except (ValueError, IndexError):
        print("Invalid task number.")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        number = int(input("Task number to delete: "))
        removed = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['title']}")
    except (ValueError, IndexError):
        print("Invalid task number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
