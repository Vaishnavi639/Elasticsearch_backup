import json
import glob
import os

# Configuration
INDEX_NAME = "products_index"  # Change this to your desired index name

def fix_bulk_files():
    # Find all bulk_part_* files
    files = glob.glob("bulk_part_*")
    files.sort()
    
    print(f"Fixing index names in bulk files...")
    print(f"Adding index name: {INDEX_NAME}")
    print()
    
    for file_path in files:
        print(f"Processing {file_path}...")
        
        # Read the original file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Process lines
        fixed_lines = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Check if this is an index action line
            if line.startswith('{"index":'):
                try:
                    # Parse the JSON
                    action = json.loads(line)
                    # Add the index name
                    action['index']['_index'] = INDEX_NAME
                    # Convert back to JSON
                    fixed_lines.append(json.dumps(action))
                except json.JSONDecodeError:
                    # If parsing fails, keep the original line
                    fixed_lines.append(line)
            else:
                # This is a document line, keep as is
                fixed_lines.append(line)
        
        # Write back to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            for line in fixed_lines:
                f.write(line + '\n')
        
        print(f"Fixed {file_path}")
    
    print()
    print(f"All files processed. Index name '{INDEX_NAME}' added to all bulk actions.")
    print("You can now run the upload command again.")

if __name__ == "__main__":
    fix_bulk_files()
