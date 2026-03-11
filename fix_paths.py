import os
import glob

docs_dir = r"D:\AIED2.0_docs\docs"
py_files = glob.glob(os.path.join(docs_dir, "*.py"))

for file_path in py_files:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Simple replacement
        new_content = content.replace("AIED2.0_docs/webbook", "AIED2.0_docs/docs")
        new_content = new_content.replace(r"AIED2.0_docs\webbook", r"AIED2.0_docs\docs")
        new_content = new_content.replace(r"AIED2.0_docs\\webbook", r"AIED2.0_docs\\docs")

        if "webbook" in content and content != new_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated: {os.path.basename(file_path)}")
    except Exception as e:
        print(f"Failed to update {file_path}: {e}")

print("Path fixing complete.")
