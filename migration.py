import os

ripple_docker: str = "rippleci/rippled:2.2.0-b3"
xahau_docker: str = "xahauci/xahaud:2024.9.11"


def replace_in_poetry(file_path, new_authors):
    """Replace occurrences of 'xrpl' with 'xahau', 'xrp' with 'xah', and add new authors in pyproject.md."""
    try:
        with open(file_path, "r") as file:
            content = file.read()

        # Replace the text
        new_content = (
            content.replace(
                "https://github.com/XRPLF/xrpl-py", "https://github.com/Xahau/xahau-py"
            )
            .replace("xrpl", "xahau")
            .replace("xrp", "xah")
            .replace("XRP ledger", "Xahau Ledger")
        )

        # Find the authors section
        authors_start = new_content.find("authors = [") + len("authors = [")
        authors_end = new_content.find("]", authors_start)

        # Create a list of existing authors
        existing_authors = new_content[authors_start:authors_end].strip()
        existing_authors_list = [
            author.strip().strip('"')
            for author in existing_authors.split(",")
            if author.strip()
        ]

        # Combine existing and new authors
        combined_authors = existing_authors_list + [
            author.strip() for author in new_authors
        ]

        # Format the combined authors list for output
        new_authors_list_str = ",\n  ".join(
            f'"{author}"' for author in combined_authors
        )

        # Replace the entire authors section with the new list
        new_content = (
            new_content[:authors_start]
            + "\n  "
            + new_authors_list_str
            + "\n]"
            + new_content[authors_end + 1 :]
        )

        # Write the changes back to the file
        with open(file_path, "w") as file:
            file.write(new_content)
        print(f"Updated: {file_path}")

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")


def replace_in_readme(file_path):
    """Replace occurrences of 'from xrpl' with 'from xahau' in README.md."""
    try:
        with open(file_path, "r") as file:
            content = file.read()

        # Replace the text
        new_content = (
            content.replace("from xrpl", "from xahau")
            .replace("xrpl-py", "xahau-py")
            .replace("xrpl.", "xahau.")
            .replace("xrpl-announce", "xahau-announce")
            .replace("xrpl-keypairs", "xahau-keypairs")
            .replace("XRP Ledger", "Xahau Ledger")
            .replace("https://s.altnet.rippletest.net:51234", "https://xahau-test.net")
        )

        # Write the changes back to the file
        with open(file_path, "w") as file:
            file.write(new_content)
        print(f"Updated: {file_path}")

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")


def replace_in_contrib(file_path):
    """Replace occurrences of 'from xrpl' with 'from xahau' in CONTRIBUTING.md."""
    try:
        with open(file_path, "r") as file:
            content = file.read()

        # Replace the text
        new_content = (
            content.replace("from xrpl", "from xahau")
            .replace("flake8 xrpl", "flake8 xahau")
            .replace("xrpl-announce", "xahau-announce")
            .replace("../xrpl", "../xahau")
            .replace("xrpllabsofficial/xrpld:1.12.0", ripple_docker)
            .replace(ripple_docker, xahau_docker)
            .replace("/opt/ripple/bin/rippled", "/opt/xahau/bin/xahaud")
            .replace("/opt/ripple/etc/rippled.cfg", "/opt/xahau/etc/xahaud.cfg")
            .replace("ripple", "xahau")
            .replace("rippled", "xahaud")
            .replace("RIPPLED", "XAHAUD")
            .replace("[validators_file]", "# [validators_file]")
            .replace("validators.txt", "# validators.txt")
            .replace("xrpl-py", "xahau-py")
        )

        # Write the changes back to the file
        with open(file_path, "w") as file:
            file.write(new_content)
        print(f"Updated: {file_path}")

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")


def replace_in_github(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()

        # Replace the text
        new_content = (
            content.replace("[xahau]", "[main, xahau]")
            .replace("flake8 xrpl", "flake8 xahau")
            .replace("reexport xrpl", "reexport xahau")
            .replace("xrpl/", "xahau/")
            .replace("source xrpl", "source xahau")
        )

        # Write the changes back to the file
        with open(file_path, "w") as file:
            file.write(new_content)
        print(f"Updated: {file_path}")

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")


def replace_in_file(file_path):
    """Replace occurrences of 'from xrpl' with 'from xahau' in the given file."""
    try:
        with open(file_path, "r") as file:
            content = file.read()

        # Replace the text
        new_content = (
            content.replace("from xrpl", "from xahau")
            .replace("import xrpl", "import xahau")
            .replace("xrpl.utils", "xahau.utils")
            .replace("xrpl.models.", "xahau.models.")
            .replace("xrpl.core.", "xahau.core.")
            .replace("flake8 xrpl", "flake8 xahau")
            .replace("xrpl-announce", "xahau-announce")
            .replace("../xrpl", "../xahau")
            .replace("xrpllabsofficial/xrpld:1.12.0", "xahaulabsofficial/xahaud:1.12.0")
            .replace("xrpl-py", "xahau-py")
            .replace("https://s.altnet.rippletest.net:51234", "https://xahau-test.net")
            .replace("https://xrplcluster.com/", "https://xahau.network")
            .replace(
                '_TEST_FAUCET_URL: Final[str] = "https://faucet.altnet.rippletest.net/accounts"',
                '_TEST_FAUCET_URL: Final[str] = "https://xahau-test.net/accounts"',
            )
            .replace(
                '_DEV_FAUCET_URL: Final[str] = "https://faucet.devnet.rippletest.net/accounts"',
                '_DEV_FAUCET_URL: Final[str] = "https://xahau-test.net/accounts"',
            )
            .replace(
                'if "altnet" in url or "testnet" in url:',
                'if "xahau-test" in url or "testnet" in url:',
            )
            .replace(
                "https://s.devnet.rippletest.net:51234",
                "https://xahau-test.net",
            )
            .replace(
                "wss://s.altnet.rippletest.net:51233",
                "wss://xahau-test.net",
            )
            .replace(
                "wss://s.devnet.rippletest.net",
                "wss://xahau-test.net",
            )
            .replace(
                "https://testnet.xrpl-labs.com",
                "https://xahau-test.net",
            )
            .replace(
                "wss://testnet.xrpl-labs.com",
                "wss://xahau-test.net",
            )
            .replace(
                "faucet.devnet.rippletest.net",
                "xahau-test.net",
            )
            .replace(
                "wss://xahau-test.net:51233",
                "wss://xahau-test.net",
            )
            .replace(
                "_DEFAULT_API_VERSION: Final[int] = 2",
                "_DEFAULT_API_VERSION: Final[int] = 1",
            )
            .replace('"xrpl.', '"xahau.')
            .replace("XRP", "XAH")
            .replace("xrp_to_drops", "xah_to_drops")
            .replace("drops_to_xrp", "drops_to_xah")
            .replace("xrp_conversions", "xah_conversions")
            # .replace("XAHLModelException", "XRPLModelException")
            .replace("XRPLModelException", "XAHLModelException")
            .replace("xahau.models.currencies.xrp", "xahau.models.currencies.xah")
            .replace('"xrp"', '"xah"')
            .replace(
                "0000000000000000000000005852500000000000",
                "0000000000000000000000005841480000000000",
            )
            .replace(
                "test_does_account_exist_throws_for_invalid_account",
                "_test_does_account_exist_throws_for_invalid_account",
            )
            .replace(
                "test_run_faucet_tests",
                "_test_run_faucet_tests",
            )
            # DA: This Wont Work Need to Delete The Test Files
            # .replace("TestAccountDelete", "NoTestAccountDelete")
            # .replace("TestAMM", "NoTestAMM")
            # .replace("TestClawback", "NoTestClawback")
            # .replace("TestDeleteOracle", "NoTestDeleteOracle")
            # .replace("TestDID", "NoTestDID")
            # .replace("TestSetOracle", "NoTestSetOracle")
            # .replace("TestXChain", "NoTestXChain")
            # .replace("TestFeature", "NoTestFeature")
        )

        # Write the changes back to the file
        with open(file_path, "w") as file:
            file.write(new_content)
        print(f"Updated: {file_path}")

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")


def search_and_replace_in_folders(folder_paths):
    """Search for Python files in the given list of folders and replace text."""
    for folder_path in folder_paths:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".py") or file.endswith(".json"):
                    file_path = os.path.join(root, file)
                    replace_in_file(file_path)


def rename_folder(old_folder_name, new_folder_name):
    """Rename the specified folder."""
    if os.path.exists(old_folder_name):
        os.rename(old_folder_name, new_folder_name)
        print(f"Renamed folder: {old_folder_name} to {new_folder_name}")
    else:
        print(f"Folder {old_folder_name} does not exist.")


def delete_file(old_file_name):
    """Delete the specified file."""
    if os.path.exists(old_file_name):
        os.remove(old_file_name)
        print(f"Deleted file: {old_file_name}")
    else:
        print(f"File {old_file_name} does not exist.")


if __name__ == "__main__":
    rename_folder("xrpl", "xahau")
    rename_folder(".ci-config/rippled.cfg", ".ci-config/xahaud.cfg")
    rename_folder("xahau/utils/xrp_conversions.py", "xahau/utils/xah_conversions.py")
    rename_folder("xahau/models/currencies/xrp.py", "xahau/models/currencies/xah.py")

    folder_list = ["snippets", "tests", "tools", "xahau"]
    search_and_replace_in_folders(folder_list)

    replace_in_contrib("CONTRIBUTING.md")
    replace_in_contrib(".github/workflows/integration_test.yml")
    replace_in_contrib(".ci-config/xahaud.cfg")
    replace_in_github(".github/workflows/integration_test.yml")
    replace_in_github(".github/workflows/unit_test.yml")
    replace_in_github(".pre-commit-config.yaml")
    # replace_in_poetry(
    #     "pyproject.toml",
    #     ["Denis Angell <denis@xrpl-labs.com>", "Tequ <tequ@xrplf.com>"],
    # )
    replace_in_readme("README.md")
    delete_file(".github/workflows/snippet_test.yml")
