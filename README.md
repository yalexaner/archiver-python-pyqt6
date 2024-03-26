# File Zipper

File Zipper is a Windows program that allows users to create ZIP archives for files and directories. It provides a
convenient way to compress and package files for easy sharing or storage.

### Getting Started

To get started with the File Zipper project, follow these steps:

1. Clone the repository to your local machine.

2. Create a virtual environment (venv) to isolate the project dependencies. Open a command prompt or terminal and
   navigate
   to the project directory. Run the following command to create a new virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment. Run the appropriate command based on your operating system:
    * For Windows:
        ```bash
        venv\Scripts\activate
        ```
    * For macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install the project dependencies. With the virtual environment activated, run the following command to install the
   required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the program. Once the dependencies are installed, you can start the File Zipper program by running the main.py
   file:
   ```bash
   python main.py
   ```

### Compiling to an Executable

To compile the File Zipper project into a single executable (`main.exe`) file, follow these steps:

1. Make sure you have all dependencies installed:
   ```bash
    pip install -r requirements.txt
   ```

2. Open a command prompt or terminal and navigate to the project directory.

3. Run the following command to create the executable:
   ```bash
   pyinstaller --onefile --add-data "icons:icons" --add-data "main.qml:." main.py
   ```
   This command tells PyInstaller to package the main.py file into a single executable, include the contents of the "
   icons" directory, and include the main.qml file in the root directory of the executable.

PyInstaller will analyze your code, collect the necessary dependencies, and create the executable file. Once the process
is complete, you will find the generated executable file (main.exe) in the dist directory within your project folder.

Note: If you have any other external files or resources that need to be included in the executable, you can add more
--add-data options to the PyInstaller command, specifying the source file/directory and the target location within
the executable.

### Usage

Upon running the main.py file, the File Zipper program will launch. Follow the on-screen instructions to select the
files or directories you want to compress into a ZIP archive. The program will guide you through the process and
create the ZIP archive in the specified location.

### Requirements

The File Zipper project has the following requirements:

* Python 3.x
* Windows operating system

The specific Python packages required by the project are listed in the requirements.txt file. These packages will be
automatically installed when following the installation steps mentioned above.