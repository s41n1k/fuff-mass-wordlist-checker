import os
import subprocess
import argparse
from datetime import datetime

BANNER = r"""
  __  __                       _      __     __          __       
 |  \/  | ___  _ __ ___   __ _| |_ __ \ \   / /__  _   _| |_ ___  
 | |\/| |/ _ \| '_ ` _ \ / _` | __/ _` \ \ / / _ \| | | | __/ _ \ 
 | |  | | (_) | | | | | | (_| | || (_| |\ V / (_) | |_| | || (_) |
 |_|  |_|\___/|_| |_| |_|\__,_|\__\__,_| \_/ \___/ \__,_|\__\___/ 

   Mass Wordlist Checker with FFUF
   Author: s41n1k | @x.com/s41n1k
"""

def run_ffuf(wordlist_file, url, ffuf_args, output_file):
    print(f"[+] Running ffuf with wordlist: {os.path.basename(wordlist_file)}")

    cmd = ["ffuf", "-u", url, "-w", wordlist_file] + ffuf_args.split()

    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.stdout:
            with open(output_file, "a") as f:
                f.write(f"\n### Results for: {os.path.basename(wordlist_file)} ###\n")
                f.write(result.stdout)
                f.write("\n")
        if result.stderr:
            print(f"[!] FFUF stderr for {wordlist_file}:\n{result.stderr}")

    except Exception as e:
        print(f"[!] Error running ffuf with {wordlist_file}: {e}")


def main():
    print(BANNER)

    parser = argparse.ArgumentParser(description="Mass FFUF runner with multiple wordlists.")
    parser.add_argument("-u", "--url", required=True, help="Target URL with FUZZ keyword")
    parser.add_argument("-path", "--wordlist-path", required=True, help="Path to wordlist folder")
    parser.add_argument("-wln", "--wordlist-names", required=True, help="Comma-separated wordlist file names")
    parser.add_argument("-f", "--ffuf-args", default="-c -fc 404 -t 20", help="Additional ffuf arguments")
    parser.add_argument("-o", "--output", default="ffuf_combined_results.txt", help="Combined output file name")
    args = parser.parse_args()

    # Final output file with timestamp prefix
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = f"{timestamp}_{args.output}"
    print(f"[+] Results will be saved in: {output_file}")

    wordlist_files = [name.strip() for name in args.wordlist_names.split(",")]
    wordlist_paths = [os.path.join(args.wordlist_path, fname) for fname in wordlist_files]

    for wlist in wordlist_paths:
        if os.path.exists(wlist):
            run_ffuf(wlist, args.url, args.ffuf_args, output_file)
        else:
            print(f"[!] Wordlist not found: {wlist}")

    print(f"\n[+] Done. All results saved to: {output_file}")


if __name__ == "__main__":
    main()
