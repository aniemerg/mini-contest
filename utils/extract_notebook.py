import json
import sys
from pathlib import Path

def extract_notebook_content(notebook_path):
    """
    Extract code and markdown content from a Jupyter notebook.
    
    Args:
        notebook_path (str): Path to the .ipynb file
        
    Returns:
        tuple: (code_cells, markdown_cells) where each is a list of content strings
    """
    # Read the notebook file
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    code_cells = []
    markdown_cells = []
    
    # Extract content from each cell
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            # Join code lines and add to code cells
            code_content = ''.join(cell['source'])
            if code_content.strip():  # Only add non-empty cells
                code_cells.append(code_content)
        
        elif cell['cell_type'] == 'markdown':
            # Join markdown lines and add to markdown cells
            markdown_content = ''.join(cell['source'])
            if markdown_content.strip():  # Only add non-empty cells
                markdown_cells.append(markdown_content)
    
    return code_cells, markdown_cells

def save_content(cells, output_path):
    """Save extracted content to a file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        for i, cell in enumerate(cells, 1):
            f.write(f'\n# Cell {i}\n{cell}\n')

def main(notebook_path):
    """
    Main function to process notebook and save content to separate files.
    
    Args:
        notebook_path (str): Path to the .ipynb file
    """
    try:
        code_cells, markdown_cells = extract_notebook_content(notebook_path)
        
        # Create output filenames based on input notebook name
        base_path = Path(notebook_path).stem
        code_output = f"{base_path}_code.py"
        markdown_output = f"{base_path}_markdown.md"
        
        # Save code cells
        if code_cells:
            save_content(code_cells, code_output)
            print(f"Code cells saved to: {code_output}")
        else:
            print("No code cells found")
            
        # Save markdown cells
        if markdown_cells:
            save_content(markdown_cells, markdown_output)
            print(f"Markdown cells saved to: {markdown_output}")
        else:
            print("No markdown cells found")
            
    except FileNotFoundError:
        print(f"Error: Could not find notebook: {notebook_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid notebook format: {notebook_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_notebook.py path/to/notebook.ipynb")
    else:
        main(sys.argv[1])
