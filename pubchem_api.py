import pubchempy as pcp
import time
import os
import json
from urllib.error import URLError

progress_file = 'progress.txt'

def get_compound_info(identifier, input_type, max_retries=3):
    for attempt in range(max_retries):
        try:
            if input_type == "CID":
                results = pcp.get_compounds(identifier, "cid", timeout=5)
            elif input_type == "Name":
                results = pcp.get_compounds(identifier, "name", timeout=5)
            elif input_type == "SMILES":
                results = pcp.get_compounds(identifier, "smiles", timeout=5)
            else:
                raise ValueError("Invalid input type")

            if not results:
                return None

            compound = results[0]
            cid = compound.cid
            molecule_name = compound.iupac_name or (compound.synonyms[0] if compound.synonyms else "")

            properties = pcp.get_properties(
                [
                    "CanonicalSMILES",
                    "InChIKey",
                    "InChI",
                    "MonoisotopicMass",
                    "MolecularFormula",
                ],
                identifier=cid,
            )

            return {
                "molecule_name": molecule_name,
                "cid": cid,
                "inchi_key": properties[0]["InChIKey"] if properties else None,
                "short_inchi_key": properties[0]["InChIKey"].split("-")[0] if properties and properties[0]["InChIKey"] else None,
                "monoisotopic_mass": properties[0]["MonoisotopicMass"] if properties else None,
                "formula": properties[0]["MolecularFormula"] if properties else None,
                "canonical_smiles": properties[0]["CanonicalSMILES"] if properties else None,
            }

        except (URLError, ConnectionError) as e:
            if attempt < max_retries - 1:
                time.sleep(5)  # Wait for 5 seconds before retrying
                continue
            else:
                print(f"Error: Unable to retrieve info for '{identifier}' after {max_retries} attempts. Error message: {e}")
                return None

    return None

def get_compound_info_list_with_progress(
    identifiers, input_type, progress_bar, root, status_var, should_continue
):
    identifiers = list(set(identifiers))  # remove duplicates
    mol_cids = []
    full_data = []

    progress_bar["maximum"] = len(identifiers)

    for index, identifier in enumerate(identifiers):
        if not should_continue():
            break

        compound_info = get_compound_info(identifier, input_type)

        if compound_info is None:
            print(f"Data for '{identifier}' could not be retrieved.")
        else:
            mol_cids.append(
                "{}: {}".format(compound_info["molecule_name"], compound_info["cid"])
            )
            data_line = "{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
                compound_info["molecule_name"],
                compound_info["cid"],
                compound_info["inchi_key"],
                compound_info["short_inchi_key"],
                compound_info["monoisotopic_mass"],
                compound_info["formula"],
                compound_info["canonical_smiles"],
            )
            print(data_line)
            full_data.append(data_line)

        progress_bar["value"] = index + 1
        truncated_identifier = identifier[:15] + "..." if len(identifier) > 15 else identifier
        status_var.set(
            f"Processing {input_type} {index + 1}/{len(identifiers)}: {truncated_identifier}"
        )
        root.update()
        time.sleep(3)

    if should_continue():
        status_var.set("Process completed")
    else:
        status_var.set("Process interrupted")

    return mol_cids, full_data

def save_progress(state):
    with open(progress_file, 'w') as file:
        json.dump(state, file)

def load_progress():
    if os.path.exists(progress_file):
        with open(progress_file, 'r') as file:
            state = json.load(file)
            if 'last_saved_time' not in state:
                state['last_saved_time'] = time.time()
            return state
    else:
        state = {"index": 0, "successful_requests": 0, "current_step": "start", "last_saved_time": time.time()}
        return state

def remove_duplicates(data_file):
    if not os.path.exists(data_file):
        return [], []  # return empty lists if the file does not exist

    with open(data_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    unique_lines = list(set(lines))
    with open(data_file, 'w', encoding='utf-8') as f:
        for line in unique_lines:
            f.write(line)

    return [], unique_lines  # Return empty list for mol_cids and unique_lines for full_data