# Solana Vanity Address Generator 🚀  

A high-performance Python-based **Solana wallet generator** that searches for **custom prefixes and suffixes** in wallet addresses.

## Features
✅ Generate **Solana wallets** with a custom **prefix and/or suffix**  
✅ Multi-core processing for faster search  
✅ Automatically saves generated wallets without overwriting old ones  
✅ Simple **command-line interface (CLI)** for ease of use  

---

## Installation 🛠️  

### 1. Install Dependencies  
Make sure you have Python 3.8+ installed. Then, run:

```sh
pip install solders 
```

### 2. Clone the Repository
```sh
git clone https://github.com/manojos/Solana-Vanity-Address-Generator.git
cd solana-vanity-generator 
```

### 3. Run the Wallet Generator

```sh
python solana_wallet_generator.py
```

## Usage 🎯
### Generating a Custom Wallet
When you run the script, it will prompt you to enter a prefix and/or suffix:
```sh
Enter wallet prefix (optional): fun
Enter wallet suffix (optional): xyz

```
The script will keep searching until it finds a Solana address matching your pattern.

### Example Output

```sh
🚀 Searching for Solana wallet with prefix 'fun' and suffix 'xyz'...

✅ Wallet Found!
🔑 Address: funxyz123abc...
🔐 Private Key (Base58): 5vKzX3...
📝 Saved to solana_wallets.txt

Do you want to generate another wallet? (y/n): 

```
## Performance Optimization ⚡
### For Faster Searches:
Use shorter prefixes (3-4 characters max for reasonable speed).
Run the script on a high-performance CPU.
Use GPU-based tools for 5+ character searches.

### Used Programs:

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Rust](https://img.shields.io/badge/Rust-Solana--Vanity-orange)
![C%2B%2B](https://img.shields.io/badge/C%2B%2B-GPU--Acceleration-brightgreen)
![CUDA](https://img.shields.io/badge/CUDA-GPU--Support-yellow)
![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen)


## Contributing 🤝
Feel free to contribute by:
<br>
Optimizing the code
<br>
Adding GPU support
<br>
Improving the CLI

### License 📜
This project is open-source under the MIT License.

### To-Do List  
---
✅ Implement prefix and suffix search  
✅ Save wallets without overwriting  
<br>
🔲 Add GPU acceleration (WIP)  
🔲 Add support for mnemonic seed phrases  
