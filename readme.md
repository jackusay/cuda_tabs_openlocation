# Tabs Open Location Plugin for CudaText

This plugin for CudaText adds a convenient option to the tab's context menu, allowing you to open the file's location in Windows Explorer.

## Features

- Adds a "Open Explorer" option to the tab's context menu in CudaText.
- Opens Windows File Explorer with the file selected.
- Displays a status message once the task is completed.

## Installation

1. Download the plugin and place it in the `py` folder of your CudaText installation.
2. Restart CudaText.

## Usage

1. Open a file in CudaText.
2. Right-click the tab of the file you want to locate.
3. Select the "Open Explorer" option from the menu.
4. Windows File Explorer will open with the selected file.

## Limitations

- This plugin currently works only on Windows OS.

## Code Overview

The core functionality is handled by the `open_tab_on_explorer()` function. This function fetches the current file path and uses `subprocess.Popen` to open the location in Windows File Explorer.
