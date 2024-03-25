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