import argparse
from . import github

def main():
    parser = argparse.ArgumentParser(description="Git Manager CLI")
    parser.add_argument("--command", default=None, choices=[None, 'init_repo', "update_repo", "auto_set"])
    parser.add_argument("--comment", default=None, help="Commit message for the update command")
    
    args = parser.parse_args()
    
    # Placeholder for command execution logic
    print(f"Executing command: {args.command}")

    if args.command is None:
        print("No command provided. Use --command to specify a command.")
        return

    handler = getattr(github, args.command, None)

    if handler:
        handler() if args.comment is None else handler(args.comment)
    else:
        print(f"Command '{args.command}' not recognized.")

    
if __name__ == "__main__":
    main()