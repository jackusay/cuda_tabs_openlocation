# Tabs Open Location Plugin for CudaText

This CudaText plugin allows you to open the current tab's file location directly in Windows File Explorer. It adds a menu option to the tab's context menu, making it easy to locate the currently opened file.

## Features

- Adds a "Open Explorer" option to the tab's context menu in CudaText.
- Opens Windows File Explorer with the file selected.
- Displays a status message once the task is completed.
- Handles cases where the file doesn't exist.

## Installation

1. Download the plugin and place it in the `py` folder of your CudaText installation.
2. Restart CudaText.

## Usage

- Right-click on any open tab in CudaText.
- Select the "Open Explorer" option from the context menu.
- Windows File Explorer will open with the file's location selected.

## Limitations

- This plugin currently works only on Windows OS.

## Code Overview

The main functionality is provided by the `open_tab_on_explorer()` function, which retrieves the current file path from the active tab and opens the corresponding location in Windows File Explorer using the `subprocess.Popen` command.
