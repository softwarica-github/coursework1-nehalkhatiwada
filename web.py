import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
from threading import Thread
import requests
import socket


root = tk.Tk()
root.title("Web Enumeration Tool")


stop_enumeration = False

def select_wordlist():
    """Open a dialog to select a wordlist file."""
    file_path = filedialog.askopenfilename(title="Select Wordlist", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    wordlist_entry.delete(0, tk.END)
    wordlist_entry.insert(0, file_path)

def resolve_dns(subdomain):
    """Resolve DNS to get IP address, if possible."""
    try:
        return socket.gethostbyname(subdomain)
    except socket.gaierror:
        return None

def enumerate_subdomains(domain, wordlist_path):
    """Enumerate subdomains from the selected wordlist with DNS resolution."""
    if not domain or not wordlist_path:
        messagebox.showerror("Error", "Domain or wordlist file is missing.")
        return
    console.delete('1.0', tk.END)
    console.insert(tk.END, "Starting subdomain enumeration...\n")
    try:
        with open(wordlist_path, 'r') as file:
            for line in file:
                if stop_enumeration:
                    console.insert(tk.END, "Enumeration stopped by user.\n")
                    break
                subdomain = line.strip()
                full_domain = f"{subdomain}.{domain}"
                ip_address = resolve_dns(full_domain)
                if ip_address:
                    console.insert(tk.END, f"Found: {full_domain} with IP {ip_address}\n")
    except FileNotFoundError:
        messagebox.showerror("Error", "Wordlist file not found.")

def enumerate_directories(url, wordlist_path):
    """Perform directory discovery on the given URL using the wordlist."""
    if not url or not wordlist_path:
        messagebox.showerror("Error", "URL or wordlist file is missing.")
        return
    console.delete('1.0', tk.END)
    console.insert(tk.END, "Starting directory discovery...\n")
    try:
        with open(wordlist_path, 'r') as file:
            for line in file:
                if stop_enumeration:
                    console.insert(tk.END, "Enumeration stopped by user.\n")
                    break
                directory = line.strip()
                full_url = f"{url.rstrip('/')}/{directory}"
                try:
                    response = requests.get(full_url, timeout=5)
                    if response.status_code == 200:
                        console.insert(tk.END, f"Found: {full_url}\n")
                except requests.RequestException:
                    pass
    except FileNotFoundError:
        messagebox.showerror("Error", "Wordlist file not found.")

def start_enumeration():
    global stop_enumeration
    stop_enumeration = False
    domain = domain_entry.get()
    url = url_entry.get()
    wordlist_path = wordlist_entry.get()
    if enumeration_type.get() == "subdomains":
        Thread(target=enumerate_subdomains, args=(domain, wordlist_path), daemon=True).start()
    elif enumeration_type.get() == "directories":
        Thread(target=enumerate_directories, args=(url, wordlist_path), daemon=True).start()

def stop_enumeration_func():
    global stop_enumeration
    stop_enumeration = True

def clear_output():
    console.delete('1.0', tk.END)


enumeration_type = tk.StringVar(value="subdomains")
tk.Radiobutton(root, text="Subdomain Enumeration", variable=enumeration_type, value="subdomains").pack(anchor=tk.W)
tk.Radiobutton(root, text="Directory Discovery", variable=enumeration_type, value="directories").pack(anchor=tk.W)


tk.Label(root, text="Target Domain:").pack(padx=10, pady=5)
domain_entry = tk.Entry(root, width=50)
domain_entry.pack(padx=10, pady=5)

tk.Label(root, text="Target URL:").pack(padx=10, pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(padx=10, pady=5)


tk.Label(root, text="Wordlist File:").pack(padx=10, pady=5)
wordlist_entry = tk.Entry(root, width=50)
wordlist_entry.pack(padx=10, pady=5)
tk.Button(root, text="Browse", command=select_wordlist).pack(pady=5)


tk.Button(root, text="Start Enumeration", command=start_enumeration).pack(pady=5)
tk.Button(root, text="Stop Enumeration", command=stop_enumeration_func).pack(pady=5)
tk.Button(root, text="Clear Output", command=clear_output).pack(pady=5)


console = scrolledtext.ScrolledText(root, height=15, width=75)
console.pack(padx=10, pady=5)

root.mainloop()
