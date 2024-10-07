import os


features = [
    "BalanceRewards",
    "CheckCashMakesTrustLine",
    "Checks",
    "CryptoConditionsSuite",
    "DepositAuth",
    "DepositPreauth",
    "DisallowIncoming",
    "ExpandedSignerList",
    "Flow",
    "FlowCross",
    "FlowSortStrands",
    "HardenedValidations",
    "Hooks",
    "HooksUpdate1",
    "ImmediateOfferKilled",
    "Import",
    "MultiSignReserve",
    "NegativeUNL",
    "PaychanAndEscrowForTokens",
    "RequireFullyCanonicalSig",
    "TicketBatch",
    "URIToken",
    "XRPFees",
    "XahauGenesis",
    "fix1513",
    "fix1515",
    "fix1543",
    "fix1571",
    "fix1578",
    "fix1623",
    "fix1781",
    "fixAmendmentMajorityCalc",
    "fixCheckThreading",
    "fixMasterKeyAsRegularKey",
    "fixNFTokenDirV1",
    "fixNFTokenNegOffer",
    "fixNFTokenRemint",
    "fixNonFungibleTokensV1_2",
    "fixPayChanRecipientOwnerDir",
    "fixQualityUpperBound",
    "fixRemoveNFTokenAutoTrustLine",
    "fixRmSmallIncreasedQOffers",
    "fixSTAmountCanonicalize",
    "fixTakerDryOfferRemoval",
    "fixUniversalNumber",
    "fixXahauV1",
    "Remit",
    "ZeroB2M",
    "fixXahauV2",
    "fixNSDelete",
    "fix240819",
    "fixPageCap",
    "fix240911",
]


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
            .replace("xrpllabsofficial/xrpld:1.12.0", "rippleci/rippled:2.2.0-b3")
            .replace("rippleci/rippled:2.2.0-b3", "xahauci/xahaud:latest")
            .replace("/opt/ripple/bin/rippled", "/opt/xahau/bin/xahaud")
            .replace("/opt/ripple/etc/rippled.cfg", "/opt/xahau/etc/xahaud.cfg")
            .replace("ripple", "xahau")
            .replace("rippled", "xahaud")
            .replace("RIPPLED", "XAHAUD")
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
            .replace("import xrpl.", "import xahau.")
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
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    replace_in_file(file_path)


def rename_folder(old_folder_name, new_folder_name):
    """Rename the specified folder."""
    if os.path.exists(old_folder_name):
        os.rename(old_folder_name, new_folder_name)
        print(f"Renamed folder: {old_folder_name} to {new_folder_name}")
    else:
        print(f"Folder {old_folder_name} does not exist.")


def update_features_in_config(file_path, features):
    """Update the features in the specified configuration file."""
    try:
        with open(file_path, "r") as file:
            content = file.readlines()

        # Find the index of the [features] section
        features_start_index = None
        features_end_index = None

        for i, line in enumerate(content):
            if line.strip() == "[features]":
                features_start_index = i
            elif features_start_index is not None and line.strip() == "":
                features_end_index = i
                break

        # If the [features] section was found, update it
        if features_start_index is not None:
            # Remove existing features
            if features_end_index is not None:
                content = (
                    content[: features_start_index + 1] + content[features_end_index:]
                )
            else:
                content = content[: features_start_index + 1]

            # Add new features
            new_features = "\n".join(f"{feature}" for feature in features)
            content.append(new_features + "\n")

            # Write the changes back to the file
            with open(file_path, "w") as file:
                file.writelines(content)

            print(f"Updated features in: {file_path}")
        else:
            print(f"[features] section not found in {file_path}")

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")


if __name__ == "__main__":
    rename_folder("xrpl", "xahau")
    rename_folder(".ci-config/rippled.cfg", ".ci-config/xahaud.cfg")

    folder_list = ["snippets", "tests", "tools", "xahau"]
    search_and_replace_in_folders(folder_list)

    replace_in_contrib("CONTRIBUTING.md")
    replace_in_contrib(".github/workflows/integration_test.yml")
    replace_in_contrib(".ci-config/xahaud.cfg")
    update_features_in_config(".ci-config/xahaud.cfg", features)
    replace_in_poetry(
        "pyproject.toml",
        ["Denis Angell <denis@xrpl-labs.com>", "Tequ <tequ@xrplf.com>"],
    )
    replace_in_readme("README.md")
