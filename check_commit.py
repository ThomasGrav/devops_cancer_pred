import sys

def check_commit(commit_message, target_string):
    if target_string in commit_message:
        print(f"Le commit contient la chaîne '{target_string}'.")
        sys.exit(0)
    else:
        print(f"Le commit ne contient pas la chaîne '{target_string}'.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Utilisation: python check_commit.py <commit_message> <target_string>")
        sys.exit(1)

    commit_message = sys.argv[1]
    target_string = sys.argv[2]
    
    check_commit(commit_message, target_string)