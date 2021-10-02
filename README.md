<h1 align="center">Certi-builder</h1>
<p align="center">A simple commandline app for generating bulk of certificates.</p>

<p align="center">
  <img src="https://img.shields.io/pypi/pyversions/certi-builder.svg">
  <img src="https://img.shields.io/github/repo-size/horizon733/certi-build">
</p>
<p align="center">
  <img src="https://img.shields.io/pypi/l/certi-builder">
</p>

# Features
- Supports png, jpg image templates for certificates
- Extracts names from excel file
- Makes text bold if needed
- Generates bulk certificates in minutes

# Installation
## Using Pip
```bash
  $ pip install certi-builer
```
## Manual
```bash
  $ git clone https://github.com/Horizon733/certi-build
  $ cd certi-build
  $ python setup.py install
```
# Usage
```bash
$ certi-builder build
certificate image path: <your path>
Excel file path:  <your path>
Text color: Hex color code E.g #000000
Font file path: <your path> Please use ttf fonts
Font size: Int E.g 10
Output location:  <your path>
X location: X-axis coords, These you can find in paint
Y location: Y-axis coords, These you can find in paint
```

# bold text
```bash
$ certi-builder build --bold
certificate image path: <your path>
Excel file path:  <your path>
Text color: Hex color code E.g #000000
Font file path: <your path> Please use ttf fonts
Font size: Int E.g 10
Output location:  <your path>
X location: X-axis coords, These you can find in paint
Y location: Y-axis coords, These you can find in paint
```

# For Contributors
If you have any idea please open an issue so we could discuss and if you want some inspiration have a look at Upcoming Features.<br>
Please make sure to read [contributing.md](https://github.com/Horizon733/certi-build/blob/master/contributing.md) before starting to contribute.
## Installing dependencies
- Make sure to install all dependencies in a new environment before start developing any new feature
```commandline
pip install -r requirements.txt
```
- Use black for formating and checking code quality before committing your code

# Upcoming Features
- Support for different kind of files for name extraction
- Different kinds of text formatting E.g Italic, Underline
- AI recognization for replacing name in certificate

# Screenshots
![image](https://user-images.githubusercontent.com/57827233/134798681-af82cd38-8197-43e8-ba3f-4fd97d1f8783.png)
![image](https://user-images.githubusercontent.com/57827233/134798688-ddfeced2-1dfe-4e40-8578-3d18899127ca.png)
