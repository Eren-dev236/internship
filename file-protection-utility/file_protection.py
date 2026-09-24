import base64
import os


def protect_file(filename):
    if not os.path.exists(filename):
        print("File not found.")
        return

    with open(filename, "rb") as file:
        content = file.read()

    protected_content = base64.b64encode(content)

    protected_filename = filename + ".protected"

    with open(protected_filename, "wb") as file:
        file.write(protected_content)

    print(f"File protected successfully: {protected_filename}")


def restore_file(filename):
    if not os.path.exists(filename):
        print("Protected file not found.")
        return

    with open(filename, "rb") as file:
        protected_content = file.read()

    try:
        original_content = base64.b64decode(protected_content)

        restored_filename = filename.replace(".protected", "")

        with open(restored_filename, "wb") as file:
            file.write(original_content)

        print(f"File restored successfully: {restored_filename}")

    except Exception:
        print("Unable to restore the file. The protected content may be invalid.")


print("=== File Protection Utility ===")
print("1. Protect a file")
print("2. Restore a file")

choice = input("Enter your choice (1/2): ")
filename = input("Enter the file name: ")

if choice == "1":
    protect_file(filename)

elif choice == "2":
    restore_file(filename)

else:
    print("Invalid choice.")