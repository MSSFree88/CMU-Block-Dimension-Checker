import sys
import tkinter as tk

def run_gui():
    import gui_app

def run_cli():
    import cli_app

def stdin_available():
    return sys.stdin and sys.stdin.isatty()

def has_console():
    try:
        return sys.stdout.isatty()
    except Exception:
        return False

def print_help():
    print("""
CMU Block Dimension Checker

Usage:
  main.exe [--gui | --cli | --help]

Options:
  --gui     Launch GUI explicitly.
  --cli     Run in command-line mode.
  --help    Show this help message.

Behavior:
  - If launched with --cli or --gui, follows the flag.
  - If built WITH console (main_cli.exe), defaults to CLI.
  - If built WITHOUT console (main_gui.exe), defaults to GUI.
""")

if __name__ == "__main__":
    args = [arg.lower() for arg in sys.argv[1:]]

    if "--help" in args:
        print_help()
        sys.exit(0)

    if "--cli" in args:
        if stdin_available():
            run_cli()
        else:
            print("⚠️ CLI mode unavailable (no console detected).")
            sys.exit(1)

    elif "--gui" in args:
        try:
            run_gui()
        except (tk.TclError, RuntimeError) as e:
            print(f"⚠️ GUI could not start: {e}")
            sys.exit(1)

    else:
        # --- Default behavior ---
        if has_console():
            # This is likely the CLI build
            run_cli()
        else:
            # This is likely the GUI build (no console)
            try:
                run_gui()
            except (tk.TclError, RuntimeError) as e:
                # GUI failed and we can’t fall back
                sys.exit(1)