import os
import shutil
import git

def clone_repo(repo_url):
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    temp_dir = os.path.join(os.getcwd(), "temp_repos", repo_name)
    
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    
    try:
        git.Repo.clone_from(repo_url, temp_dir)
        return temp_dir
    except Exception as e:
        return None

def read_repo_content(repo_path):
    files_content = {}
    supported_extensions = ['.py', '.js', '.jsx', '.ts', '.tsx', '.java', '.cpp', '.c', '.html', '.css']
    
    for root, _, files in os.walk(repo_path):
        for file in files:
            if any(file.endswith(ext) for ext in supported_extensions):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        files_content[file] = f.read()
                except:
                    continue
                    
    return files_content

def cleanup_repo(repo_path):
    if os.path.exists(repo_path):
        try:
            shutil.rmtree(repo_path)
        except:
            pass