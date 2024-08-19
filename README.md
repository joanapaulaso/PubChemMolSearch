# 🧪 PubChem API App

![PubChem API App Logo](logo.png)

## 📝 Description

PubChem API App is a user-friendly tool designed to interact with the PubChem database, allowing researchers to easily retrieve chemical compound information. This application was developed by Joana Paula Oliveira, a researcher at the Integrated Laboratory of Plants Science (LIBV).

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

## 👩‍🔬 About the Developer

This app was created by Joana Paula Oliveira, a researcher at the Integrated Laboratory of Plants Science (LIBV). The work is part of ongoing research efforts to streamline chemical compound information retrieval for plant science studies.

## 🌿 Integrated Laboratory of Plants Science (LIBV)

![LIBV Logo](libv_logo.png)

The Integrated Laboratory of Plants Science (LIBV) is dedicated to advancing our understanding of plant biology through interdisciplinary research. Our work combines molecular biology, genetics, biochemistry, and bioinformatics to address crucial questions in plant science.

## 📄 License

GNU General Public License v3.0

## 📞 Contact

For questions, issues, or collaborations, please contact Joana Paula Oliveira at joanapaulasoliveira@gmail.com.

## 🙏 Acknowledgments

Special thanks to the PubChem platform for providing the API that makes this tool possible, and to the LIBV for supporting this development.