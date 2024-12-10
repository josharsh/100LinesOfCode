# Booklet Maker

## Introduction

This quick CLI will take in a pdf and then reorder the pages so you can print it using two per page setting, allowing you to staple the pages together.

This was made because PDF readers like acrobat are expensive and Preview has no automatic booklet setting

## How it Works

This will see if your PDF is of a length of a multiple of 4, then reorders the pages in the proper format so you can print on a double sided page with 4 pages per sheet. Perfect for academic papers printed at home to save paper and ink. 

### Why 4?

4 is required since we will be separating it so each page is placed properly:

#### e.g. 12 pages

This will print with 3 sheets since 12 // 4 = 3

Sheet 1 side 1: pg 12 pg 1 `[ 12 `| 1 `]
Sheet 1 side 2: pg 2 pg 11`[ 1 `| 11 `]

Sheet 2 side 1: pg 10 pg 3 `[ 10 `| 3 `]
Sheet 2 side 2: pg 4 pg 9`[ 4 `| 9 `]

Sheet 3 side 1: pg 8 pg 5 `[ 8 `| 5 `]
Sheet 3 side 2: pg 6 pg 7`[ 6 `| 7 `] `( Center fold `)

#### Page Numbers from example in order

12, 1, 2, 11, 10, 3, 4, 9, 8, 5, 6, 7.

## How to Use

1. Make sure you have Python installed on your system. This script requires Python 3.6 or higher.

>[!TIP]
> If you are using Mac, you can easily start it off by just running setup.sh which will set up a new venv for you and install PyPDF2 and make the file executable

2. Install the required dependency by running the following command:
   ```
   pip install PyPDF2
   ```

3. Save the `bookl3t.py` script to your desired location.

4. Open a terminal or command prompt and navigate to the directory where you saved the script.
### Running the script

5. Run the script using the following command:
   ```
   python bookl3t.py input.pdf output.pdf
   ```
   Replace `input.pdf` with the path to your input PDF file, and `output.pdf` with the desired path and filename for the output booklet PDF.

   For example:
   ```
   python bookl3t.py /path/to/input.pdf /path/to/output.pdf
   ```

6. The script will process the input PDF and generate a new PDF in booklet format. The output PDF will be saved at the specified output path.

7. If the script runs successfully, you will see a message printed in the terminal:
   ```
   Booklet created successfully!
   ```

   If an error occurs during the booklet creation process, an error message will be displayed instead.

### Debugging

By default, the script prints debug information to the console, including page counts, padding pages needed, and the page arrangement for each sheet. If you don't want to see this information, you can modify the `create_booklet` function call in the script and set the `debug` parameter to `False`:

```python
create_booklet(input_path, output_path, debug=False)
```

## To Print:

To print your new file, make sure you've selected double sided (! Short Edges !), collate pages, 2 pages per sheet:
![[Pasted image 20241210173200.png]]
![[Pasted image 20241210172851.png]]

### Requirements

- Python 3.6 or higher
- PyPDF2 library

Make sure to have the necessary dependencies installed before running the script.

## Contact & License

Created by Gabriel Husain - gabe.husain [at] gmail [dot] com  
GitHub: [gabe-husain](https://github.com/gabe-husain)

This project is licensed under MIT.