✅ All Features:
```
-u – Target URL (with FUZZ)
-path – Wordlist folder path
-wln – Comma-separated wordlist file names (e.g., admin.txt,php.txt)
-f – FFUF flags (e.g., -fc 404 -t 30 even all ffuf cmd)
-o – Output file (combined)
```
✅ Clean UX Example:
```
python3 ffuf-mass-wrdChecker.py \
  -u https://target.com/FUZZ \
  -path /root/wrdList/Bug-Bounty-Wordlists \
  -wln admin.txt,phpmyadmin.txt,backup.txt \
  -f "-fc 404 -t 40 -c" \
  -o final_result.txt
```
  ✅ Usage:
  
  `massffuf.py -u https://site/FUZZ -path wordlist-path -wln admin.txt,php.txt -f "-fc 404"`
