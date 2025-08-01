#!/bin/bash
#set -x #debug enable/disable

# Check if user has bash
[ ${BASH_VERSINFO} -ge 3 ] || { echo "Need bash =>v3"; exit 1; }

# Check if user is on a valid OS
if [ "$(uname 2>/dev/null)" == "Darwin" ]; then
    user_OS="mac"
elif [ "$(lsb_release -is 2>/dev/null)" == "Ubuntu" ]; then
    user_OS="ubuntu"
else 
    echo -e "Unsupported OS version. Please install requirments manually.\n Exiting..."
    exit 5
fi

# Define programms array based on user OS
declare -a programs=("python3" "pip3" "unzip" "curl")
declare -a not_installed_programs=()

# Find the programs which the user has not installed
for i in "${programs[@]}"; do
    command -v "$i" >/dev/null 2>&1 || not_installed_programs+=("$i")
done

# Tell user to install the programs they need
[ "${#not_installed_programs[@]}" -ne 0 ] && { echo "Missing ${not_installed_programs[@]}"; exit 2; }

# Assume programs have been installed.
declare -r prog_name="travel-breeze"
declare -r git_rep="https://codeload.github.com/SurenMar/${prog_name}/zip/refs/heads/main"

# Get files from repo and store in zip file
curl -s -o "${prog_name}.zip" "$git_rep" || \
{ echo "Error: Could not download files"; exit 3; }

# Check if downloaded files are corrupted
unzip -t -qq "${prog_name}.zip" && { unzip -o -qq "${prog_name}.zip"; } \
				|| { echo "Some files are corrupted! Exiting..."; exit 4; }
# Clean up directory
[ -d "${prog_name}" ] && { echo -e "Directory ${prog_name} already exists. Rename or remove\n Exiting..."; exit 1; }
rm "${prog_name}.zip" && mv "${prog_name}-main" "${prog_name}"
cd "${prog_name}"

# Install, create and activate virtual environment
[ "$user_OS" == "ubuntu" ] && sudo apt-get install python3-venv -y
python3 -m venv tb_env
source tb_env/bin/activate

# Upgrade pip and install needed libraries and frameworks
python -m pip install --upgrade pip
pip install -r requirements.txt

# Migrate models
python manage.py makemigrations
python manage.py migrate

# Add execution permission to run.sh and create database file
chmod +x "tb_run.sh"

echo -e "You're all set!\nSimply type cd $prog_name and ./tb_run.sh\nEnjoy exploring!"

exit 0
