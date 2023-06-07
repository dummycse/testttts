import os
import subprocess
import git
#os.system('git clone https://github.com/mozilla/rust-code-analysis.git')
#subprocess.run(['cd','rust-code-analysis'])
print(git.Repo.clone_from('https://github.com/mozilla/rust-code-analysis.git','/home/shiva/Projects/Rust/hello/rust_code_ana'))
os.chdir('/home/shiva/Projects/Rust/hello/rust_code_ana')
print('Changed dir')
process=subprocess.run(['cargo', 'build','--workspace'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#process=subprocess.run(['cargo', 'build','-p','rust-code-analysis-cli'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print(process.stdout.decode())
print(process.stderr.decode())
