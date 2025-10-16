# 🧪 PubChem API App

![PubChem API App Logo](logo.png)

## 📝 Description

PubChem API App is a user-friendly tool designed to interact with the PubChem database, allowing researchers to easily retrieve chemical compound information. This application was developed by Joana Paula Oliveira.

## ✨ Features

- 🔍 Retrieve compound information using Name, CID, or SMILES identifiers
- 🖥️ User-friendly graphical interface
- 📊 Progress tracking for batch requests
- 🗑️ Automatic removal of duplicate entries
- 💾 Export results to a text file

## 🚀 Installation

### Windows Installer

1. Download the latest release from the [Releases](https://github.com/yourusername/pubchem-api-app/releases) page.
2. Run the installer and follow the on-screen instructions.
3. Once installed, you can launch the app from your desktop or start menu.

### Python Version

If you prefer to run the Python version directly:

1. Ensure you have Python 3.7+ installed on your system.
2. Clone this repository:
   ```
   git clone https://github.com/yourusername/pubchem-api-app.git
   ```
3. Navigate to the project directory:
   ```
   cd pubchem-api-app
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the application:
   ```
   python pubchem_api_runner.py
   ```

## 🔧 Usage

1. Launch the PubChem API App.
2. Click "Browse" to select an input file containing your identifiers (one per line).
3. Choose the input type (Name, CID, or SMILES) from the dropdown menu.
4. Enter a name for the output file.
5. Click "Start Process" to begin retrieving information.
6. Use the "Restart Connection" button if you encounter any network issues.

## 📁 Example Files

For testing and demonstration purposes, we provide example input files for each type of identifier:

- `example_mol-names.txt`: Contains a list of molecule names
- `example_smiles.txt`: Contains a list of SMILES identifiers
- `example_cids.txt`: Contains a list of PubChem Compound IDs (CIDs)

These files are available in the `examples` folder of the repository and can be used to test the functionality of the app.

## 📊 Output Example

Here's an example of what the output looks like for the compound "caffeine":

```
Molecule Name    CID     InChI Key               Short InChI Key   Monoisotopic Mass   Molecular Formula   Canonical SMILES
caffeine         2519    RYYVLZVUVIJVGH-UHFFFAOYSA-N   RYYVLZVUVIJVGH   194.080376         C8H10N4O2         CN1C=NC2=C1C(=O)N(C(=O)N2C)C
```

This tab-separated output provides:
- Molecule Name: The common name of the compound
- CID: PubChem Compound ID
- InChI Key: International Chemical Identifier Key
- Short InChI Key: First 14 characters of the InChI Key
- Monoisotopic Mass: The mass of the molecule containing the most abundant isotopes of each element
- Molecular Formula: The chemical formula of the compound
- Canonical SMILES: Simplified Molecular-Input Line-Entry System representation

This comprehensive output allows for easy integration with other tools and databases in your research workflow.

## 👩‍🔬 About the Developer

This app was created by Joana Paula Oliveira. The work is part of ongoing research efforts to streamline chemical compound information retrieval for plant science studies.

## 📄 License

GNU General Public License v3.0

## 📞 Contact

For questions, issues, or collaborations, please contact Joana Paula Oliveira at joanapaulasoliveira@gmail.com.

## 🙏 Acknowledgments


Special thanks to the PubChem platform for providing the API that makes this tool possible.

