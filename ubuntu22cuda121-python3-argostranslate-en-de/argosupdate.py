import os

# Parse command line arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--argospath', type=str, action='store', required=True, help='Directory where the Argos Translate models are stored.')
parser.add_argument('--sourcelanguage', type=str, action='store', required=True, help='Source language code, e.g. "en"')
parser.add_argument('--targetlanguage', type=str, action='store', required=True, help='Target language code, e.g. "de"')
args = parser.parse_args()

# Check write access to directories
import sys
import os

ARGOSPACKAGEPATH = os.path.join(args.argospath, "packages")
SOURCELANGUAGECODE = args.sourcelanguage
TARGETLANGUAGECODE = args.targetlanguage

# Check existence of Packages path
if not os.access(ARGOSPACKAGEPATH, os.R_OK):
    sys.exit(f'ERROR: Cannot read Argos package directory {ARGOSPACKAGEPATH}')
print(f'Using Argos package path {ARGOSPACKAGEPATH}')

print('Updating Argos Translate')
os.environ['ARGOS_PACKAGES_DIR'] = ARGOSPACKAGEPATH

from argostranslate import package

# Update package definitions from remote
package.update_package_index()

# Load available packages from local package index
available_packages = package.get_available_packages()

# Download and install package for source and target language
for available_package in available_packages:
    if available_package.from_code == SOURCELANGUAGECODE and available_package.to_code == TARGETLANGUAGECODE:
        print(f'Installing package {available_package.from_code} - {available_package.to_code}')
        download_path = available_package.download()
        package.install_from_path(download_path)
